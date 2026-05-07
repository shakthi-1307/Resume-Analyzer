# 🚀 Groq API Setup Guide

## ✅ Step 1: Get Your Groq API Key

### **Free Setup** (No credit card required!)

1. **Go to Groq Console:**
   - Visit: https://console.groq.com/keys
   - Sign up with email/GitHub

2. **Create API Key:**
   - Click "Create New API Key"
   - Copy the key (looks like: `gsk_...`)
   - Save it safely

---

## 🔧 Step 2: Configure Locally

### **On Your Machine (Local Testing)**

1. **Set Environment Variable:**

   **Windows (PowerShell):**
   ```powershell
   $env:GROQ_API_KEY = "gsk_your_api_key_here"
   ```

   **Windows (CMD):**
   ```cmd
   set GROQ_API_KEY=gsk_your_api_key_here
   ```

   **Mac/Linux:**
   ```bash
   export GROQ_API_KEY="gsk_your_api_key_here"
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Locally:**
   ```bash
   python -m app.main
   ```

4. **Test:**
   - Open http://127.0.0.1:8000
   - Upload a resume and job description
   - Click "Analyze Now"
   - Should work instantly! ⚡

---

## ☁️ Step 3: Deploy to Railway with Groq

### **Set API Key in Railway**

1. **Go to Railway Dashboard:**
   - https://railway.app/dashboard

2. **Select Your Project:** "Resume-Analyzer"

3. **Go to Variables Tab:**
   - Click **Settings** → **Variables**

4. **Add Environment Variable:**
   - Name: `GROQ_API_KEY`
   - Value: `gsk_your_api_key_here`
   - Click "Save"

5. **Redeploy:**
   - Railway automatically redeploys with the new variable
   - Wait 2-3 minutes for deployment
   - Check logs to confirm it's working

---

## 🧪 Testing

### **Local Test:**
```bash
# After setting GROQ_API_KEY environment variable
python -m app.main
# Go to http://127.0.0.1:8000
# Upload resume and test
```

### **Production Test:**
1. Go to your Railway app URL
2. Upload resume PDF
3. Paste job description
4. Click "Analyze Now"
5. Should get results in 5-10 seconds! ⚡

---

## 📊 Groq API Benefits

| Feature | Details |
|---------|---------|
| **Speed** | <2 seconds for most analyses |
| **Cost** | Free tier: 30 requests/minute, 7,000/day |
| **Quality** | Mixtral 8x7B - production-grade LLM |
| **Reliability** | 99.9% uptime SLA |
| **No Setup** | Cloud-based, no local installation |

---

## ⚠️ Rate Limits (Free Tier)

- **30 requests per minute**
- **7,000 requests per day**
- **Perfect for academic use!**

To upgrade: https://console.groq.com/billing/limits

---

## 🆘 Troubleshooting

### **"GROQ_API_KEY not set" Error**

**Solution:** Make sure environment variable is set before running:

```bash
# Check if set (Windows PowerShell)
echo $env:GROQ_API_KEY

# Check if set (Mac/Linux)
echo $GROQ_API_KEY
```

### **"Rate Limit Exceeded" Error**

**Solution:** 
- Free tier: 30 requests/minute limit
- Wait a minute and try again
- Or upgrade your Groq plan

### **"Invalid API Key" Error**

**Solution:**
- Make sure key starts with `gsk_`
- Check you copied the full key
- Regenerate key if needed: https://console.groq.com/keys

### **App Works Locally but Not on Railway**

**Solution:**
1. Check Railway Variables are set
2. View Railway logs for errors
3. Restart Railway deployment
4. Wait 30 seconds for changes to apply

---

## 📝 Important Notes

- ✅ Free tier is more than enough for academic projects
- ✅ Groq is **much faster** than Ollama
- ✅ No more resource constraints on Railway
- ✅ Instant API responses (no model loading time)
- ✅ Production-ready infrastructure

---

## 🔐 Security Best Practices

- ❌ **Never** commit API key to GitHub
- ✅ Use Railway environment variables
- ✅ Use `.env` files locally (add to .gitignore)
- ✅ Regenerate keys if exposed

---

## 📞 Support

**Groq Documentation:** https://console.groq.com/docs
**Railway Variables:** https://docs.railway.app/reference/variables
**Common Issues:** https://console.groq.com/docs/faq

---

**Your app is now using Groq - instant, free, and production-ready!** 🎉
