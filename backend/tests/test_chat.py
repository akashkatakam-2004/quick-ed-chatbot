import os
import sys
from pathlib import Path

# Deterministic retrieval-only mode so tests do not depend on the LLM.
os.environ["GROQ_API_KEY"] = ""

sys.path.append(str(Path(__file__).resolve().parent.parent))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

CASES = [
    ("what courses do you offer", "python full stack"),
    ("what are the course fees", "contact admissions"),
    ("who teaches genai", "akash katam"),
    ("what is the refund policy", "not published"),
    ("do you have weekend batches", "does not publish"),
    ("do you provide placement support", "placement"),
    ("what tools will I learn", "langchain"),
    ("what cources do u have", "java full stack"),
    ("were are you located", "street address"),
    ("are classes online or offline", "online or offline"),
    ("quantum chromodynamics", "couldn't find verified"),
    ("tell me a joke", "couldn't find verified"),
]


def run():
    health = client.get("/health").json()
    assert health["status"] == "ok" and health["chunks"] > 0, health
    for question, expected in CASES:
        answer = client.post("/api/chat", json={"message": question}).json()["answer"]
        assert expected in answer.lower(), (question, answer[:300])
    print(f"{len(CASES)} chat checks + health passed")


def test_cases():
    run()


if __name__ == "__main__":
    run()
