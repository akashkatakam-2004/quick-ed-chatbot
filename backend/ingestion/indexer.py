from pathlib import Path
from .loaders import load_pdf, load_xlsx, detect_course


def _kv(chunk):
    return dict(line.split(": ", 1) for line in chunk["text"].splitlines()[1:] if ": " in line)


def _catalogue_overview(chunks):
    rows = []
    for c in chunks:
        if not c["source"].startswith("02_"):
            continue
        kv = _kv(c)
        if "Course Name" not in kv:
            continue
        fees = kv.get("Fees") or kv.get("Fees (₹)") or "not published"
        level = f" ({kv['Level']})" if kv.get("Level") else ""
        rows.append(f"{kv['Course Name']}{level}: {kv.get('Duration', '')}, fees {fees}. {kv.get('Tagline', '')}".strip())
    if not rows:
        return []
    text = "[02_Course_Catalogue / Courses]\nCourses offered by Quick Ed Solutions:\n" + "\n".join(rows)
    return [{"text": text, "source": "02_Course_Catalogue.xlsx", "ref": "sheet 'Courses', all rows", "kind": "overview"}]


def _fee_overview(chunks):
    rows = []
    for c in chunks:
        if not c["source"].startswith("05_"):
            continue
        kv = _kv(c)
        if "Course" in kv and ("Fees" in kv or "Fees (₹)" in kv):
            rows.append(f"{kv['Course']}: {kv.get('Fees') or kv.get('Fees (₹)')}")
    if not rows:
        return []
    text = "[05_Fee_Structure / Course Fees]\nCourse fees:\n" + "\n".join(rows)
    return [{"text": text, "source": "05_Fee_Structure.xlsx", "ref": "sheet 'Course Fees', all rows", "kind": "overview"}]


def build_chunks(data_dir: Path):
    chunks = []
    for f in sorted(Path(data_dir).iterdir()):
        if f.suffix.lower() == ".xlsx":
            chunks += load_xlsx(f)
        elif f.suffix.lower() == ".pdf":
            chunks += load_pdf(f)
    chunks += _catalogue_overview(chunks)
    chunks += _fee_overview(chunks)
    for i, c in enumerate(chunks):
        c["id"] = i
        c["course"] = detect_course(c["text"])
    return chunks
