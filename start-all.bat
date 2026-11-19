@echo off
echo Starting Quick Ed Assistant (API + chatbot) in separate windows...
start "Quick Ed API" cmd /k "%~dp0start-backend.bat"
timeout /t 3 >nul
start "Quick Ed Chatbot" cmd /k "%~dp0start-frontend.bat"
