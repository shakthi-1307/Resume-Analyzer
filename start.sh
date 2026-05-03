#!/bin/bash

echo "========================================"
echo "Resume Analyzer Startup Script"
echo "========================================"
echo ""

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "ERROR: Ollama is not installed or not in PATH"
    echo "Please download Ollama from https://ollama.ai"
    exit 1
fi

# Check if Ollama is running
if ! curl -s http://127.0.0.1:11434/api/tags > /dev/null; then
    echo "[*] Starting Ollama service..."
    ollama serve &
    sleep 5
    echo "[OK] Ollama started"
else
    echo "[OK] Ollama is already running"
fi

echo ""
echo "[*] Checking if mistral model is available..."
if ! ollama list | grep -q "mistral"; then
    echo "[!] Mistral model not found. Pulling now (this may take a few minutes)..."
    ollama pull mistral
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to pull mistral model"
        exit 1
    fi
fi

echo "[OK] Mistral model is available"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

echo "[*] Installing/updating dependencies..."
pip install -r requirements.txt > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    pip install -r requirements.txt
    exit 1
fi

echo "[OK] Dependencies installed"
echo ""
echo "========================================"
echo "Starting FastAPI Server..."
echo "========================================"
echo ""
echo "The application will be available at:"
echo "http://127.0.0.1:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

python3 -m app.main

if [ $? -ne 0 ]; then
    echo "ERROR: FastAPI server failed to start"
fi
