import os
from pathlib import Path
from dotenv import load_dotenv

# httpx rejects IPv6-bracketed entries like [::1] in NO_PROXY
_no_proxy = os.environ.get("NO_PROXY", "")
if "[" in _no_proxy:
    os.environ["NO_PROXY"] = ",".join(p for p in _no_proxy.split(",") if "[" not in p)

BASE = Path(__file__).resolve().parent.parent
load_dotenv(BASE / ".env")

_data_dir = Path(os.getenv("DATA_DIR", "QuickEd_Knowledge_Base"))
DATA_DIR = _data_dir if _data_dir.is_absolute() else BASE / _data_dir
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")]
EMBED_MODEL = os.getenv("EMBED_MODEL", "BAAI/bge-small-en-v1.5")
TOP_K = int(os.getenv("TOP_K", "5"))
MIN_SCORE = float(os.getenv("MIN_SCORE", "0.07"))
RATE_LIMIT_PER_MIN = int(os.getenv("RATE_LIMIT_PER_MIN", "20"))
MAX_MESSAGE_CHARS = 500
