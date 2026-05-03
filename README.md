# AI Resume Analyzer

A smart resume analyzer that uses local LLM (Ollama) to match resumes against job descriptions using semantic analysis.

## Features

- 🤖 AI-powered resume matching using Ollama
- 📄 PDF resume extraction and analysis
- 🎯 Match score calculation with detailed feedback
- 🎨 Modern glassmorphism UI with animations
- ⚡ Real-time analysis with loading states
- 🔒 Local processing - no data sent to external APIs

## Prerequisites

Before running this application, you need:

1. **Python 3.8+** - [Download](https://www.python.org/)
2. **Ollama** - [Download](https://ollama.ai/)
3. **Mistral Model** - Run `ollama pull mistral` in terminal

## Installation

1. **Clone/Extract the repository**

   ```bash
   cd resume-analyzer
   ```

2. **Create a virtual environment (optional but recommended)**

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

### Step 1: Start Ollama Service

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
