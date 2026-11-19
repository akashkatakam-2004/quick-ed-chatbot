import re
import time
from collections import defaultdict, deque
from functools import lru_cache
from typing import List
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from core.config import DATA_DIR, TOP_K, MIN_SCORE, RATE_LIMIT_PER_MIN, MAX_MESSAGE_CHARS
from ingestion.indexer import build_chunks
from rag.retriever import Retriever
from rag.generator import generate, NOT_FOUND

TOPIC = re.compile(
    r"\b(fees?|cost|price|charges?|batch|timing|time|seats?|trainer|teach\w*|refund|cancel\w*|"
    r"placement|jobs?|projects?|demo|certificate|admission|attendance|location|contact|duration|syllabus|owner|"
    r"hostel|courses?|programs?|programmes?|training|curriculum)\b",
    re.I,
)
PRONOUN = re.compile(r"\b(it|its|that|this|them|those|there)\b", re.I)

router = APIRouter()
_hits = defaultdict(deque)


@lru_cache(maxsize=1)
def get_retriever():
    return Retriever(build_chunks(DATA_DIR))


class Turn(BaseModel):
    role: str = Field(pattern="^(user|assistant)$")
    content: str = Field(max_length=2000)


class ChatIn(BaseModel):
    message: str = Field(min_length=1, max_length=MAX_MESSAGE_CHARS)
    history: List[Turn] = []


def _limit(ip):
    now, q = time.time(), _hits[ip]
    while q and now - q[0] > 60:
        q.popleft()
    if len(q) >= RATE_LIMIT_PER_MIN:
        raise HTTPException(429, "Too many requests. Please wait a minute.")
    q.append(now)


@router.post("/chat")
def chat(body: ChatIn, request: Request):
    _limit(request.client.host if request.client else "x")
    hist = [t.model_dump() for t in body.history]
    msg = body.message
    prev_user = [t["content"] for t in hist if t["role"] == "user"][-2:]
    # Only reword bare follow-ups; prefixing real questions buries the actual topic
    needs_context = len(msg.split()) < 5 and (PRONOUN.search(msg) or not TOPIC.search(msg))
    query = " ".join(prev_user + [msg]) if needs_context else msg
    hits = get_retriever().search(query, TOP_K)
    if not hits or max(h[2] for h in hits) < MIN_SCORE:
        return {"answer": NOT_FOUND, "sources": []}
    answer = generate(body.message, hist, hits)
    sources = sorted({h[0]["source"] for h in hits[:3]})
    return {"answer": answer, "sources": sources}
