from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from core.config import ALLOWED_ORIGINS
from api.routes import router, get_retriever

app = FastAPI(title="Quick Ed Solutions Chatbot API")
app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS, allow_methods=["*"], allow_headers=["*"])
app.include_router(router, prefix="/api")
app.mount("/static", StaticFiles(directory=Path(__file__).resolve().parent / "static"), name="static")


@app.get("/widget.js")
def widget_js():
    return FileResponse(Path(__file__).resolve().parent / "static" / "widget.js", media_type="application/javascript")


@app.on_event("startup")
def warm():
    get_retriever()


@app.get("/health")
def health():
    return {"status": "ok", "chunks": len(get_retriever().chunks)}
