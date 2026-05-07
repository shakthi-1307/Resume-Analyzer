# 🚀 Complete Setup Guide - Groq API Migration

## ✅ What Changed

**Old:** Ollama (local AI, required Ollama installation, resource-heavy)
**New:** Groq API (cloud-based, instant, free tier available) ⚡

---

## 📋 Complete Setup (Step-by-Step)

### **Phase 1: Get Groq API Key** (5 minutes)

#### Step 1a: Create Groq Account
1. Go to: https://console.groq.com/signup
2. Sign up with email or GitHub
3. Verify your email

#### Step 1b: Create API Key
1. Go to: https://console.groq.com/keys
2. Click **"Create New API Key"**
3. Copy the key (starts with `gsk_`)
4. **Save it somewhere safe** ⚠️

```
Your API Key should look like:
gsk_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

### **Phase 2: Run Locally (Test)** (5 minutes)

#### Step 2a: Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY = "gsk_your_key_here"
```

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=gsk_your_key_here
```

**Mac/Linux:**
```bash
export GROQ_API_KEY="gsk_your_key_here"
```

#### Step 2b: Install & Run
```bash
cd d:\resume-analyzer
pip install -r requirements.txt
python -m app.main
```

#### Step 2c: Test It
1. Open: http://127.0.0.1:8000
2. Paste a job description
3. Upload a resume PDF
4. Click "Analyze Now"
5. **Should get results in 5-10 seconds!** ✨

---

### **Phase 3: Deploy to Railway** (10 minutes)

#### Step 3a: Set API Key in Railway

1. Go to Railway Dashboard: https://railway.app/dashboard
2. Click **"Resume-Analyzer"** project
3. Click your service in the middle
4. Go to **"Settings"** tab (top right)
5. Go to **"Variables"** section
6. Add new variable:
   - **Key:** `GROQ_API_KEY`
   - **Value:** `gsk_your_key_here`
7. Click **"Save"**

#### Step 3b: Wait for Redeploy
- Railway automatically redeploys with the new variable
- Takes 2-3 minutes
- Check **Deployments** tab to see build progress

#### Step 3c: Test on Railway
1. Get your Railway URL from the dashboard
2. Open it in browser
3. Test upload and analyze
4. **Should work instantly!** ⚡

---

## ✨ What You Get Now

| Feature | Ollama | Groq |
|---------|--------|------|
| **Speed** | 30-60 sec | 5-10 sec |
| **Setup** | Complex (local install) | Simple (API key only) |
| **Cost** | Free (local) | Free tier: 7,000 req/day |
| **Reliability** | Depends on your PC | 99.9% uptime |
| **Deployment** | Heavy (~4GB resource) | Lightweight |
| **Works Offline** | Yes | No (cloud-based) |

---

## 📝 Files Changed

**Modified:**
- `app/services/ai_engine.py` → Now uses Groq instead of Ollama
- `requirements.txt` → `groq` instead of `ollama`
- `static/index.html` → Updated UI text
- `README.md` → Updated documentation
- `Dockerfile` → Simplified (no Ollama)
- `docker-compose.yml` → Only app service

**Added:**
- `GROQ_SETUP.md` → Detailed Groq setup
- `.env.example` → Environment variable template

---

## 🔐 Security Notes

- ✅ **Never** commit API key to GitHub
- ✅ Use Railway environment variables for production
- ✅ Use `.env` files locally (already in `.gitignore`)
- ✅ Regenerate key if accidentally exposed: https://console.groq.com/keys

---

## 🆘 Quick Troubleshooting

### **Local Testing Issues**

| Problem | Solution |
|---------|----------|
| `GROQ_API_KEY not set` | Set environment variable before running |
| `Invalid API key` | Key should start with `gsk_` |
| `Rate limit exceeded` | Free tier: 30 req/min, 7,000 req/day |
| Module not found | Run `pip install -r requirements.txt` |

### **Railway Deployment Issues**

| Problem | Solution |
|---------|----------|
| App crashes after deploy | Check Variables are set in Railway |
| Still showing Ollama error | Wait 2-3 min, then refresh Railway |
| No changes after push | Check Deployments tab for build status |
| API key not working | Verify key is correct in Railway Variables |

---

## 🎯 Next Steps

1. ✅ Get Groq API key (https://console.groq.com/keys)
2. ✅ Test locally with the key
3. ✅ Set API key in Railway Variables
4. ✅ Wait for auto-redeploy (2-3 min)
5. ✅ Test on live URL
6. ✅ Done! 🎉

---

## 📊 Performance Expectations

**Local Testing:**
- First run: 10-15 seconds (model warmup)
- Subsequent: 5-10 seconds

**Railway Production:**
- All requests: 5-10 seconds ⚡
- No warmup needed
- Instant response

---

## 💬 Verification Checklist

Before marking as complete:

- [ ] Groq API key obtained from https://console.groq.com/keys
- [ ] Local testing works (GROQ_API_KEY set)
- [ ] Can upload resume and get results
- [ ] API key added to Railway Variables
- [ ] Railway redeploy complete (check Deployments tab)
- [ ] Live URL shows instant results
- [ ] No "Could not connect to Ollama" errors
- [ ] Disclaimer shows "Powered by Groq"

---

## 📞 Need Help?

- **Groq API Issues:** https://console.groq.com/docs/faq
- **Railway Issues:** https://docs.railway.app/
- **Code Issues:** Check GROQ_SETUP.md and README.md

---

**Your Resume Analyzer now uses Groq - instant, powerful, and free!** 🚀

**Total Setup Time: ~15-20 minutes**
