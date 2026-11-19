import re
import numpy as np
from fastembed import TextEmbedding
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from core.config import EMBED_MODEL

_model = None


def get_model() -> TextEmbedding:
    global _model
    if _model is None:
        _model = TextEmbedding(EMBED_MODEL)
    return _model


def _normalize(v):
    norm = np.linalg.norm(v, axis=-1, keepdims=True)
    return v / np.where(norm == 0, 1, norm)


SYNONYMS = [
    (r"\b(split|part payment|pay in parts|in parts|emi|instalments?)\b", "installment"),
    (r"\b(cost|price|charge)\b", "fees"),
    (r"\b(teacher|faculty|tutor|instructor)\b", "trainer"),
    (r"\b(vacancy|vacancies)\b", "available seats"),
    (r"\b(cources?|corses?|couse)\b", "courses"),
    (r"\bprogram(me)?s?\b", "course"),
]


def expand(q: str) -> str:
    for pattern, word in SYNONYMS:
        q = re.sub(pattern, word, q, flags=re.I)
    return q


def query_course(q: str):
    t = q.lower()
    if re.search(r"\bjava\b", t):
        return "java"
    if "python" in t or "pythn" in t:
        return "python"
    if "genai" in t or "generative ai" in t or re.search(r"\bllms?\b", t):
        return "genai"
    if "cyber" in t or "ethical hacking" in t:
        return "cybersecurity"
    if "testing" in t or re.search(r"\bqa\b", t):
        return "testing"
    return None


class Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        texts = [c["text"] for c in chunks]
        self.char = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True)  # typo-tolerant
        self.word = TfidfVectorizer(ngram_range=(1, 2), stop_words="english", sublinear_tf=True)
        self.Xc = self.char.fit_transform(texts)
        self.Xw = self.word.fit_transform(texts)
        self.D = _normalize(np.array(list(get_model().embed(texts)), dtype=np.float32))

    def search(self, query: str, k: int = 5):
        lexical_query = expand(query)
        sc = cosine_similarity(self.char.transform([lexical_query]), self.Xc)[0]
        sw = cosine_similarity(self.word.transform([lexical_query]), self.Xw)[0]
        lex = 0.5 * sc + 0.5 * sw

        qv = _normalize(np.array(list(get_model().query_embed(query))[0], dtype=np.float32))
        sem_raw = self.D @ qv
        sem = (sem_raw - sem_raw.min()) / (sem_raw.max() - sem_raw.min() + 1e-9)
        lex_n = lex / (lex.max() + 1e-9)

        score = 0.45 * lex_n + 0.55 * sem
        qc = query_course(query)
        if qc:
            for i, c in enumerate(self.chunks):
                if c["course"] == qc:
                    score[i] += 0.12
                elif c["course"]:
                    score[i] -= 0.08
        if re.search(r"\b(cour\w*|cource\w*|progra\w*|train\w*|curricul\w*)\b", query, re.I):
            for i, c in enumerate(self.chunks):
                if c.get("kind") == "overview":
                    score[i] += 0.35
        idx = np.argsort(-score)[:k]
        return [(self.chunks[i], float(score[i]), float(lex[i]), float(sem_raw[i])) for i in idx]
