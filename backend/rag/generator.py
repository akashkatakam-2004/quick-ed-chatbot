import time

import httpx
from core.config import GROQ_API_KEY, GROQ_MODEL

CONTACT = "Please contact our admissions team at +91 83748 52001 or admissions@quickedsolutions.com."
NOT_FOUND = "I couldn't find verified information about that in our Quick Ed Solutions data. " + CONTACT

SYSTEM = f"""You are the Quick Ed Solutions website assistant.
Rules:
- Answer ONLY from the CONTEXT given. Never guess or invent fees, dates, discounts, trainers, seats or placement promises.
- If the context does not contain the answer, reply exactly: "{NOT_FOUND}"
- The user may write in broken English, Hinglish or with typos. Infer the intended question instead of refusing.
- Quick Ed Solutions offers five flagship programs: Java Full Stack Development, Python Full Stack Development, GenAI & Large Language Models, Cybersecurity & Ethical Hacking, and Software Testing & QA Automation.
- The CONTEXT covers the whole website: programs, trainers, tools and frameworks, why-choose-us, the founder, brochures, enrollment, contact details, social links and policies.
- If asked about fees, batches or timings without naming a course, share what the context says for all five programs instead of asking.
- Fees, batch dates, class timings, weekend schedules, training mode, address, refunds and certificate details are not published on the website. Say the information is not published and direct the user to admissions; never fill the gap with a guess.
- Placement is support and mentorship only, never a job guarantee. Do not quote placement statistics. The brochure advertises a 500+ hiring partners list; present that figure only as stated in the brochure.
- Keep answers short (2-5 sentences), friendly, plain text. Use ₹ for fees when a fee is present.
- Use earlier chat turns for follow-ups."""


def generate(question: str, history: list, hits: list):
    context = "\n\n".join(f"({c['source']}, {c['ref']})\n{c['text']}" for c, *_ in hits)
    if not GROQ_API_KEY:  # retrieval-only fallback
        return "(no LLM key set - showing best match)\n\n" + "\n\n".join(c["text"] for c, *_ in hits[:3])
    msgs = [{"role": "system", "content": SYSTEM}]
    msgs += [{"role": m["role"], "content": m["content"]} for m in history[-6:]]
    msgs.append({"role": "user", "content": f"CONTEXT:\n{context}\n\nQUESTION: {question}"})
    try:
        for attempt in range(2):
            r = httpx.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                json={"model": GROQ_MODEL, "messages": msgs, "temperature": 0.2, "max_tokens": 400},
                timeout=30,
            )
            if r.status_code == 429 and attempt == 0:  # tokens-per-minute limit
                time.sleep(min(float(r.headers.get("retry-after", "2")), 10))
                continue
            r.raise_for_status()
            answer = r.json()["choices"][0]["message"]["content"]
            return answer.translate({0xA0: " ", 0x202F: " ", 0x2009: " "}).replace("**", "").strip()
    except Exception as exc:
        print(f"LLM error: {exc}")
        return "Sorry, I'm having trouble answering right now. " + CONTACT
