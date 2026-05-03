#!/bin/bash
# Quick deployment to Railway

echo "=========================================="
echo "Resume Analyzer - Railway Deployment"
echo "=========================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "[*] Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - Resume Analyzer"
else
    echo "[OK] Git repository already initialized"
fi

echo ""
echo "[*] Installing Railway CLI..."
npm install -g @railway/cli

echo ""
echo "[*] Logging into Railway..."
railway login

echo ""
echo "[*] Creating Railway project..."
railway init

echo ""
echo "[*] Setting environment variables..."
railway variables set OLLAMA_HOST=http://localhost:11434
railway variables set PORT=8000

echo ""
echo "[*] Deploying to Railway..."
railway up

echo ""
echo "=========================================="
echo "Deployment complete!"
echo "Your app is now live on Railway!"
echo "Run: railway open"
echo "=========================================="
