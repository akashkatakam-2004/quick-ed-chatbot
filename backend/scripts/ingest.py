"""Check what gets extracted: python scripts/ingest.py"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from core.config import DATA_DIR
from ingestion.indexer import build_chunks

chunks = build_chunks(DATA_DIR)
print(f"{len(chunks)} chunks from {DATA_DIR}\n")
for c in chunks:
    print(f"#{c['id']} [{c['course']}] {c['source']} ({c['ref']})\n{c['text'][:160]}...\n")
