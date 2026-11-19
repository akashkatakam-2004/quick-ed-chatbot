# Quick Ed Solutions — AI Chatbot

Standalone chatbot-only project extracted from the Quick Ed full-stack website. It contains the React chat widget, FastAPI RAG backend, Groq integration, knowledge base, tests, and Windows launch scripts. It does not contain the marketing website.

## Project structure

```text
quick-ed-chatbot/
├── frontend/                     React 19 + Vite 8 chatbot demo
│   ├── src/components/
│   │   ├── ChatWidget.jsx        Chat UI and API communication
│   │   └── ChatWidget.css        Scoped chatbot styles
│   ├── src/assets/               Quick Ed logo used by the widget
│   └── .env.example              VITE_CHAT_API_URL
├── backend/                      FastAPI + RAG API
│   ├── api/routes.py             POST /api/chat and rate limiting
│   ├── rag/                      Hybrid retrieval and grounded Groq answers
│   ├── ingestion/                XLSX/PDF loaders and chunk builder
│   ├── QuickEd_Knowledge_Base/   14 Quick Ed source spreadsheets
│   ├── static/                   Optional embeddable JavaScript widget
│   ├── tests/test_chat.py        Retrieval and health checks
│   └── .env.example              Backend configuration
├── start-backend.bat             Set up and start the API
├── start-frontend.bat            Install dependencies and start the chat UI
└── start-all.bat                 Start both in separate windows
```

## Requirements

- Python 3.11+ (developed on 3.12)
- Node.js 22.12+ (developed on 24)
- A Groq API key for LLM answers; an empty key runs retrieval-only mode

## Run on Windows

1. Copy `backend/.env.example` to `backend/.env` and set `GROQ_API_KEY`.
2. Double-click `start-all.bat`, or run it from a VS Code terminal:

   ```bat
   start-all.bat
   ```

3. Open http://127.0.0.1:5173. The chatbot opens automatically.

The first backend start creates `backend/.venv`, installs dependencies, and may download the embedding model. The first frontend start runs `npm install`.

To start the apps separately, use `start-backend.bat` and `start-frontend.bat`.

## Manual start

```bat
REM Backend terminal
cd backend
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env
.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000

REM Frontend terminal
cd frontend
npm install
npm run dev
```

The frontend defaults to `http://127.0.0.1:8000`. To use another API URL, copy `frontend/.env.example` to `frontend/.env` and change `VITE_CHAT_API_URL`.

## Verify

```bat
cd backend
.venv\Scripts\python.exe tests\test_chat.py

cd ..\frontend
npm run lint
npm run build
```

API endpoints:

- `GET /health` — API status and loaded knowledge-base chunk count
- `POST /api/chat` — accepts `{ "message": "...", "history": [] }` and returns an answer with sources
- `GET /widget.js` — optional standalone JavaScript widget
- `GET /static/demo.html` — optional JavaScript widget preview

## Merge into another React website

1. Copy the complete `backend/` folder and configure its `.env`.
2. Copy these frontend files:
   - `frontend/src/components/ChatWidget.jsx`
   - `frontend/src/components/ChatWidget.css`
   - `frontend/src/assets/quick-ed-logo.webp`
3. Import and render the widget inside the existing app:

   ```jsx
   import ChatWidget from './components/ChatWidget';

   <ChatWidget />
   ```

   `<ChatWidget />` shows the floating launcher. `<ChatWidget initialOpen />` opens the panel immediately.

4. Set `VITE_CHAT_API_URL` to the backend URL and add the website origin to the backend's `ALLOWED_ORIGINS`.

The component uses scoped `qed-chat-*` class names and needs only React; it does not depend on the removed website components, Swiper, or React Icons.

## Knowledge base and answer rules

The backend answers from the 14 spreadsheets in `backend/QuickEd_Knowledge_Base/`. After editing them, restart the backend to rebuild the cached retriever.

Unpublished fees, batch dates, timings, training mode, address, refunds, and similar details must remain marked as unpublished. The assistant must direct those questions to admissions instead of inventing information.

## Security

Never commit `.env` files or API keys. The included `.gitignore` excludes local environments, dependencies, virtual environments, caches, and build output. After cloning, each developer creates their own `backend/.env` from `.env.example`.
