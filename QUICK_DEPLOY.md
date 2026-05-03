# 🚀 Resume Analyzer - Quick Deploy Guide

## ⚡ 30-Second Deploy to Railway

### **Step 1: Create GitHub Repo**

```bash
git init
git add .
git commit -m "Resume Analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/resume-analyzer.git
git push -u origin main
```

### **Step 2: Deploy to Railway**

**Option A: Using deploy script (Windows)**

```bash
deploy.bat
```

**Option B: Using deploy script (Mac/Linux)**

```bash
bash deploy.sh
```

**Option C: Manual (all platforms)**

1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Choose your `resume-analyzer` repository
5. Railway auto-deploys! ✅

### **Step 3: Get Your Live URL**

- Check Railway dashboard
- Copy the public URL
- Share with anyone!

---

## 📋 What's Being Deployed

```
Your App
├── FastAPI Backend (app/)
├── Frontend (static/)
├── Ollama LLM (runs in Docker)
└── All configured for production
```

---

## ✅ Pre-Deployment Checklist

- [ ] All files committed to GitHub
- [ ] Dockerfile present (auto-created)
- [ ] requirements.txt updated
- [ ] app/services/ai_engine.py uses OLLAMA_HOST env variable
- [ ] No hardcoded localhost (127.0.0.1)
- [ ] README.md present for documentation

---

## 📦 Files Added for Deployment

| File                 | Purpose                             |
| -------------------- | ----------------------------------- |
| `Dockerfile`         | Container configuration for Railway |
| `docker-compose.yml` | Local Docker development            |
| `railway.json`       | Railway deployment config           |
| `deploy.bat`         | One-click deploy (Windows)          |
| `deploy.sh`          | One-click deploy (Mac/Linux)        |
| `DEPLOYMENT.md`      | Detailed deployment guide           |

---

## 🌍 Access Your App

After deployment:

```
https://resume-analyzer-YOUR-RAILWAY-RANDOM-ID.railway.app
```

Share this URL with anyone!

---

## 📊 Expected Performance

| Metric              | Time                              |
| ------------------- | --------------------------------- |
| Build time          | 2-3 minutes                       |
| First startup       | 5-10 minutes (Ollama loads model) |
| First analysis      | 20-30 seconds (model warming up)  |
| Subsequent analyses | 10-15 seconds                     |

---

## 💰 Costs

- **Free Tier**: $5/month Railway credit (usually enough for testing)
- **Paid**: ~$15-30/month for continuous hosting
- **Ollama**: Runs in same container (no extra cost)

---

## 🆘 If Deployment Fails

**Check logs:**

```bash
railway logs
```

**Common issues:**

- Dockerfile syntax error → Fix Dockerfile
- Port conflict → Change PORT environment variable
- Memory error → Upgrade Railway plan
- Git issues → Ensure code is pushed to GitHub

**Contact Railway support:**

- Discord: https://discord.gg/railway
- Docs: https://docs.railway.app

---

## 🔄 Update Deployed App

Make changes locally:

```bash
git add .
git commit -m "Update message"
git push origin main
```

Railway auto-redeplooys! No manual action needed.

---

## 🎯 Next Steps

1. ✅ Deploy to Railway (follow above)
2. 🧪 Test the live app
3. 📤 Share URL with users
4. 📊 Monitor performance in Railway dashboard
5. 🔄 Update as needed

---

**Your app is now live on the internet!** 🎉
