@echo off
setlocal
cd /d "%~dp0frontend"

if not exist "node_modules" (
  echo [Quick Ed] Installing frontend dependencies...
  call npm install
  if errorlevel 1 goto :error
)

echo [Quick Ed] Starting chatbot on http://127.0.0.1:5173 ...
call npm run dev
goto :eof

:error
echo [Quick Ed] Setup failed. Install Node.js 18+ and make sure "npm" is on PATH.
pause
