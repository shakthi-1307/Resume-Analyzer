# AI Resume Analyzer

A smart resume analyzer powered by Groq AI that matches resumes against job descriptions using advanced semantic analysis. **No installation needed - works instantly!**

## Features

- 🤖 AI-powered resume matching using Groq's Mixtral LLM
- ⚡ **Instant analysis** - results in 5-10 seconds
- 📄 PDF resume extraction and analysis
- 🎯 Match score calculation with detailed feedback
- 🎨 Modern glassmorphism UI with animations
- ☁️ Cloud-based - no local setup required
- 🆓 Free tier available (7,000 requests/day)

## Quick Start (3 Steps)

### **Step 1: Get Groq API Key** (Free, 1 minute)
1. Go to https://console.groq.com/keys
2. Sign up with email/GitHub
3. Create API key (starts with `gsk_`)
4. Copy it

### **Step 2: Set API Key**

**Locally:**
```bash
# Windows PowerShell
$env:GROQ_API_KEY = "gsk_your_key_here"

# Mac/Linux
export GROQ_API_KEY="gsk_your_key_here"
```

**On Railway:** Add to Variables tab (see GROQ_SETUP.md)

### **Step 3: Run It**
```bash
pip install -r requirements.txt
python -m app.main
```

Open http://127.0.0.1:8000 and start analyzing! 🚀

---

## Prerequisites

- **Python 3.8+** - [Download](https://www.python.org/)
- **Groq API Key** - [Free signup](https://console.groq.com/keys)
- **No Ollama needed!** ✅

## Installation

1. **Clone/Extract the repository**
   ```bash
   cd resume-analyzer
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Step 1: Set Your Groq API Key
See detailed setup: [GROQ_SETUP.md](GROQ_SETUP.md)

**Quick version:**
```bash
# Windows
set GROQ_API_KEY=gsk_your_key_here

# Mac/Linux
export GROQ_API_KEY="gsk_your_key_here"
```

### Step 2: Start the Server
```bash
python -m app.main
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 3: Open in Browser
Go to: http://127.0.0.1:8000

---

## Usage

1. **Paste Job Description** - Copy the job posting
2. **Upload Resume** - Select a PDF file
3. **Click Analyze** - Wait 5-10 seconds for results
4. **View Results** - See match score and detailed analysis

---

## Project Structure

```
resume-analyzer/
├── app/
│   ├── main.py              # FastAPI setup
│   ├── api/
│   │   └── analyzer.py      # API endpoints
│   └── services/
│       ├── ai_engine.py     # Groq LLM integration
│       └── parser.py        # PDF parsing
├── static/
│   ├── index.html           # Frontend
│   ├── css/style.css        # Styling
│   └── js/script.js         # Interactions
├── requirements.txt         # Dependencies
└── README.md               # This file
```

---

## Technology Stack

- **Backend:** FastAPI, Uvicorn, Groq API
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **PDF Processing:** pdfplumber
- **AI Model:** Mixtral 8x7B (via Groq)
- **Deployment:** Docker, Railway

---

## Troubleshooting

### "GROQ_API_KEY not set"
→ Set environment variable before running (see Quick Start above)

### "Rate limit exceeded"
→ Free tier: 30 req/min, 7,000 req/day. Upgrade on https://console.groq.com/billing

### "Invalid API key"
→ Key must start with `gsk_`. Regenerate at https://console.groq.com/keys

### "Could not read PDF"
→ Ensure file is a valid PDF, not corrupted

---

## Deployment

### Deploy to Railway (Free)

1. Push to GitHub
2. Go to https://railway.app
3. Connect GitHub repo
4. Add `GROQ_API_KEY` to Variables
5. Deploy! ✨

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed steps

---

## Performance

| Metric | Details |
|--------|---------|
| **Speed** | 5-10 seconds per analysis |
| **Model** | Mixtral 8x7B (128k token context) |
| **Accuracy** | Production-grade LLM |
| **Availability** | 99.9% uptime |
| **Free Tier** | 7,000 requests/day |

---

## API Reference

### Analyze Resume
```bash
POST /analyze

Form Data:
- job_description (string): Job posting text
- resume (file): PDF resume file

Response:
{
  "match_score": "87%",
  "analysis": "3 Key Strengths: ...\n3 Missing Skills: ..."
}
```

---

## Academic Use

✅ This project was built for **academic and learning purposes**
✅ Perfect for students and researchers
✅ Free tier sufficient for educational use
⚠️ Use responsibly - ensure compliance with your institution's policies

---

## License

MIT License - Feel free to use and modify!

---

## Support

- **Groq Docs:** https://console.groq.com/docs
- **FastAPI:** https://fastapi.tiangolo.com
- **Railway:** https://docs.railway.app

---

**Ready to analyze resumes? Get your free Groq API key and start in minutes!** 🚀

Make sure Ollama is running on your machine:

```bash
ollama serve
```

The Ollama service should be accessible at `http://127.0.0.1:11434`

### Step 2: Start FastAPI Server

In a new terminal:

```bash
python -m app.main
```

You should see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 3: Open the Application

Open your browser and go to:

```
http://127.0.0.1:8000
```

## Usage

1. **Paste Job Description** - Copy the job posting and paste it in the "Job Description" field
2. **Upload Resume** - Select a PDF file of your resume
3. **Click Analyze** - Wait for the AI to analyze the match
4. **View Results** - See your match score and detailed analysis

## Project Structure

```
resume-analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app setup
│   ├── api/
│   │   ├── __init__.py
│   │   └── analyzer.py      # API endpoints
│   └── services/
│       ├── __init__.py
│       ├── ai_engine.py     # Ollama LLM integration
│       └── parser.py        # PDF parsing
├── static/
│   ├── index.html           # Frontend HTML
│   ├── css/
│   │   └── style.css        # Styling
│   └── js/
│       └── script.js        # Frontend logic
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technology Stack

- **Backend:** FastAPI, Uvicorn
- **AI/ML:** Ollama, Mistral LLM
- **PDF Processing:** pdfplumber
- **Frontend:** HTML, CSS, JavaScript
- **Styling:** Glassmorphism design with modern CSS

## Troubleshooting

### "Could not connect to Ollama"

- Make sure Ollama is running: `ollama serve`
- Verify it's accessible at `http://127.0.0.1:11434`
- Run `ollama list` to confirm models are installed

### "Error: Could not read PDF"

- Ensure the uploaded file is a valid PDF
- Try with a different PDF file to test

### "Could not connect to the backend"

- Verify FastAPI server is running
- Check if `http://127.0.0.1:8000` is accessible
- Check browser console for detailed errors (F12)

### Port Already in Use

If port 8000 is already in use:

```bash
python -m app.main --port 8080
```

## Performance Notes

- First analysis may take 15-30 seconds as the model processes the text
- Subsequent analyses are faster as Ollama caches the model
- Performance depends on your system's CPU/GPU

## Future Improvements

- [ ] Support for multiple resume formats (DOCX, TXT)
- [ ] Batch analysis for multiple resumes
- [ ] Historical analysis tracking
- [ ] Export results as PDF
- [ ] Custom model selection
- [ ] API authentication

## License

MIT License - Feel free to use and modify!

## Support

For issues or questions, check the browser console (F12) for error details.
