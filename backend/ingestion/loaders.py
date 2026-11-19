import re
from pathlib import Path
import pdfplumber
from openpyxl import load_workbook

COURSE_KEYS = {
    "python": ("python full stack",),
    "java": ("java full stack",),
    "genai": ("genai", "generative ai"),
    "cybersecurity": ("cybersecurity",),
    "testing": ("software testing", "qa automation"),
}


def detect_course(text: str):
    t = text.lower()
    hits = [c for c, keys in COURSE_KEYS.items() if any(k in t for k in keys)]
    return hits[0] if len(hits) == 1 else None


def _fmt(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return f"{v:,.0f}" if float(v).is_integer() else str(v)
    return str(v).replace("\n", "; ")


def load_xlsx(path: Path):
    wb = load_workbook(path, data_only=True)
    chunks = []
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        if len(rows) < 2:
            continue
        hdr = [str(h) for h in rows[0]]
        for i, r in enumerate(rows[1:], start=2):
            if not any(v not in (None, "") for v in r):
                continue
            lines = [f"{h}: {_fmt(v)}" for h, v in zip(hdr, r) if v not in (None, "")]
            text = f"[{path.stem} / {ws.title}]\n" + "\n".join(lines)
            chunks.append({"text": text, "source": path.name, "ref": f"sheet '{ws.title}', row {i}"})
    return chunks


def _split_long(text, limit=1000):
    if len(text) <= limit:
        return [text]
    parts, cur = [], ""
    for s in re.split(r"(?<=[.!?])\s+", text):
        if len(cur) + len(s) > limit and cur:
            parts.append(cur.strip())
            cur = ""
        cur += s + " "
    if cur.strip():
        parts.append(cur.strip())
    return parts


def load_pdf(path: Path):
    """Split by heading using font size / bold detection."""
    lines = []
    with pdfplumber.open(path) as pdf:
        for pno, page in enumerate(pdf.pages, start=1):
            words = page.extract_words(extra_attrs=["fontname", "size"])
            rows = {}
            for w in words:
                rows.setdefault(round(w["top"] / 3), []).append(w)
            for key in sorted(rows):
                ws = sorted(rows[key], key=lambda w: w["x0"])
                lines.append({
                    "text": " ".join(w["text"] for w in ws),
                    "size": max(w["size"] for w in ws),
                    "bold": "Bold" in ws[0]["fontname"],
                    "page": pno,
                })
    title, h2, h3 = path.stem, None, None
    buf, page0, chunks = [], 1, []

    def flush():
        nonlocal buf
        body = " ".join(buf).strip()
        if body:
            head = " > ".join(x for x in (title, h2, h3) if x)
            for part in _split_long(body):
                chunks.append({"text": f"[{head}]\n{part}", "source": path.name, "ref": f"page {page0}"})
        buf = []

    prev_title = False
    for ln in lines:
        ln["text"] = ln["text"].replace("(cid:127)", "-")
        if ln["size"] >= 17:
            title = (title + " " + ln["text"]) if prev_title else ln["text"]
            prev_title = True
            continue
        prev_title = False
        if False:
            pass
        elif ln["size"] >= 11.5:
            flush(); h2, h3 = ln["text"], None; page0 = ln["page"]
        elif ln["bold"] and 9.2 <= ln["size"] < 11.5:
            flush(); h3 = ln["text"]; page0 = ln["page"]
        else:
            buf.append(ln["text"])
    flush()
    return chunks
