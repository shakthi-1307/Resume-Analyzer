# Resume Analyzer - Railway Deployment Guide

## 🚀 Deployment Steps

### **Option 1: Deploy with Docker (Recommended)**

#### Prerequisites

- GitHub account (to push code)
- Railway account (free at https://railway.app)
- Git installed

#### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository called `resume-analyzer`
3. Clone it locally and copy your project files:
   ```bash
   cd resume-analyzer
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

#### Step 2: Deploy to Railway

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub"**
4. Authorize Railway to access your GitHub
5. Select the `resume-analyzer` repository
6. Railway will auto-detect the Dockerfile and deploy!

#### Step 3: Configure Environment Variables

In Railway dashboard:

1. Go to your project
2. Click on the service
3. Go to **Variables** tab
4. Add:
   ```
   OLLAMA_HOST=http://localhost:11434
   PORT=8000
   ```

#### Step 4: Wait for Deployment

Railway will:

- Build the Docker image (2-3 minutes)
- Download and initialize Ollama (5-10 minutes on first run)
- Start the FastAPI server

Your app will be available at the Railway-provided URL!

---

### **Option 2: Deploy without Docker (Quick Start)**

#### Prerequisites

- Railway account (https://railway.app)
- Python 3.9+

#### Step 1: Push to GitHub (same as above)

#### Step 2: Connect Railway

1. Go to Railway.app
2. Click **"New Project"** → **"Deploy from GitHub"**
3. Select your repository

#### Step 3: Manual Configuration

Railway should auto-detect a Python project. If not:

1. In Railway dashboard, click **"Environment"**
2. Add start command:
   ```bash
   python -m app.main
   ```

#### Note: Limitations

- **Ollama won't work** without Docker (not easily installable on Railway)
- Consider using an **external AI API** instead (OpenAI, HuggingFace, etc.)

---

### **Option 3: Alternative Platforms**

#### **Render.com** (Easy, has free tier)

1. Push to GitHub
2. Go to render.com
3. Click "New" → "Web Service"
4. Connect GitHub repo
5. Set environment:
   - Build: `pip install -r requirements.txt`
   - Start: `python -m app.main`
   - Port: 8000

#### **PythonAnywhere.com** (Python-specific)

1. Upload files via FTP or GitHub
2. Set up web app
3. Configure WSGI (needs modification for FastAPI)
4. Same Ollama limitation

#### **Replit.com** (Browser-based, instant)

1. Go to replit.com
2. Click "Import from GitHub"
3. Paste your repo URL
4. Click "Run"
5. That's it!

---

## 📦 Production Considerations

### **Memory & CPU**

- **Ollama + Mistral**: Requires 4GB+ RAM
- **Railway**: Free tier has 512MB shared memory
- **Solution**: Upgrade to paid plan or use external API

### **Model Loading**

- First request will take 30-60 seconds (model loads)
- Subsequent requests are faster

### **API Keys** (if using external AI)

- Store in Railway environment variables
- Never commit to GitHub

### **Custom Domain**

1. In Railway dashboard: Settings → Domain
2. Add custom domain (requires DNS setup)
3. Railway provides SSL certificate automatically

---

## 🔧 Post-Deployment Checklist

After deployment:

- [ ] Test the app in browser
- [ ] Try uploading a resume
- [ ] Verify AI analysis works
- [ ] Check logs for errors
- [ ] Monitor memory usage
- [ ] Set up alerts for crashes

---

## 📝 Environment Variables Reference

```bash
# Required for Ollama
OLLAMA_HOST=http://localhost:11434

# FastAPI
PORT=8000
HOST=0.0.0.0

# Optional
LOG_LEVEL=INFO
```

---

## 🆘 Troubleshooting Deployment

### **"Connection refused" error**

- Ollama isn't running
- Check service logs in Railway dashboard

### **"Out of memory" error**

- Your plan doesn't have enough RAM
- Upgrade to paid Railway plan
- Or switch to external AI API

### **"502 Bad Gateway"**

- App crashed
- Check logs: click service → View logs
- Look for Python errors

### **Model not downloading**

- Railway storage is full
- Not enough memory during download
- Use external API instead

### **Slow response times**

- First request loads model (normal)
- Check server specs (may need upgrade)

---

## 💡 Cost Estimation

| Platform       | Free Tier       | Paid Starting | Notes                  |
| -------------- | --------------- | ------------- | ---------------------- |
| Railway        | $5/month credit | $5+ monthly   | Best for Docker        |
| Render         | Limited         | $7/month      | Good alternative       |
| PythonAnywhere | Yes             | $5/month      | Limited Ollama support |
| Replit         | Yes             | $7/month      | Browser-based          |

---

## 🌍 Making It Public

### **Share Your App**

1. Get the Railway URL from dashboard
2. Share it with anyone
3. They can use it without installing anything!

### **Custom Domain**

1. Buy domain from GoDaddy, Namecheap, etc.
2. In Railway: Settings → Domain → Add custom domain
3. Follow DNS setup instructions

---

## 🚀 Next Steps

1. **Create GitHub repository** → Push your code
2. **Sign up for Railway** → https://railway.app
3. **Connect GitHub repo** → Railway auto-deploys
4. **Wait for build** → Monitor in dashboard
5. **Get public URL** → Share with others!

---

## 📞 Support

**If deployment fails:**

1. Check Railway logs (Dashboard → Service → Logs)
2. Look for specific error messages
3. Verify Dockerfile is in root directory
4. Ensure all files are pushed to GitHub
5. Try redeploying from Railway dashboard

**For Railway help:**

- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway
