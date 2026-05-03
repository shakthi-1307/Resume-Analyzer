@echo off
echo ========================================
echo Resume Analyzer Startup Script
echo ========================================
echo.

REM Check if Ollama is installed
where ollama >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ERROR: Ollama is not installed or not in PATH
    echo Please download Ollama from https://ollama.ai
    pause
    exit /b 1
)

REM Check if Ollama is already running
tasklist /FI "IMAGENAME eq ollama.exe" 2>NUL | find /I /N "ollama.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo [OK] Ollama is already running
) else (
    echo [*] Starting Ollama service...
    start cmd /k ollama serve
    timeout /t 5 /nobreak
    echo [OK] Ollama started
)

echo.
echo [*] Checking if mistral model is available...
ollama list | find "mistral" >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [!] Mistral model not found. Pulling now (this may take a few minutes)...
    ollama pull mistral
    if %ERRORLEVEL% neq 0 (
        echo ERROR: Failed to pull mistral model
        pause
        exit /b 1
    )
)

echo [OK] Mistral model is available
echo.

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [*] Installing/updating dependencies...
pip install -r requirements.txt >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to install dependencies
    pip install -r requirements.txt
    pause
    exit /b 1
)

echo [OK] Dependencies installed
echo.
echo ========================================
echo Starting FastAPI Server...
echo ========================================
echo.
echo The application will be available at:
echo http://127.0.0.1:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python -m app.main

if %ERRORLEVEL% neq 0 (
    echo ERROR: FastAPI server failed to start
    pause
)

pause
