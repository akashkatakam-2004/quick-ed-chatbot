@echo off
setlocal
cd /d "%~dp0backend"

if not exist ".venv\Scripts\python.exe" (
  echo [Quick Ed] Creating Python virtual environment...
  python -m venv .venv
  if errorlevel 1 goto :error
  ".venv\Scripts\python.exe" -m pip install --upgrade pip
  ".venv\Scripts\python.exe" -m pip install -r requirements.txt
  if errorlevel 1 goto :error
)

if not exist ".env" (
  copy ".env.example" ".env" >nul
  echo [Quick Ed] Created backend\.env - add your GROQ_API_KEY for AI answers.
)

echo [Quick Ed] Starting API on http://127.0.0.1:8000 ...
".venv\Scripts\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8000
goto :eof

:error
echo [Quick Ed] Setup failed. Install Python 3.11+ and make sure "python" is on PATH.
pause
