# Resume Analyzer - Complete Workflow Explanation

## 🚀 How It All Works: Step-by-Step

### **PHASE 1: Starting the Application**

```
User runs: python -m app.main
           ↓
app/main.py starts FastAPI server
           ↓
Server listens on http://127.0.0.1:8000
           ↓
User opens browser to http://127.0.0.1:8000
```

---

## 📁 File Structure & Responsibilities

### **1. app/main.py** - The Web Server

```
ROLE: Server setup and configuration
PURPOSE: Initialize FastAPI and serve everything
```

**What it does:**

- ✅ Creates the FastAPI application
- ✅ Enables CORS (allows frontend to talk to backend)
- ✅ Sets up error handling middleware (catches request errors)
- ✅ Registers the analyzer routes from `app/api/analyzer.py`
- ✅ Mounts static files (HTML, CSS, JS) from the `static/` folder
- ✅ Starts the Uvicorn web server on port 8000

**Key lines:**

```python
app = FastAPI()                                    # Create server
app.include_router(analyzer_router)               # Register API routes
app.mount("/", StaticFiles(...), name="static")  # Serve HTML/CSS/JS
uvicorn.run(app, host="127.0.0.1", port=8000)   # Start server
```

---

### **2. static/index.html** - The User Interface

```
ROLE: Frontend - what the user sees
PURPOSE: Display the form and results
```

**What it contains:**

- ✅ HTML form with two inputs:
  - Textarea for Job Description
  - File upload for Resume (PDF)
- ✅ "Analyze Now" button
- ✅ Results area (hidden until analysis completes)
- ✅ Links to CSS styling and JavaScript logic

**Flow in HTML:**

```html
<textarea id="jd">...</textarea>
<!-- Job Description Input -->
<input type="file" id="resumeFile" />
<!-- Resume Upload -->
<button onclick="analyzeResume()">
  <!-- Click triggers JS function -->
  <div id="resultsArea" class="hidden"><!-- Results shown here --></div>
</button>
```

---

### **3. static/js/script.js** - The Frontend Logic

```
ROLE: Handles user interaction and communication with backend
PURPOSE: Manage form submission and display results
```

**What it does:**

**Step 1 - Button Click Detection:**

```javascript
async function analyzeResume() {
    // Get data from HTML form
    const jd = document.getElementById("jd").value;                   // Get job description
    const fileInput = document.getElementById("resumeFile");          // Get PDF file
```

**Step 2 - Validation:**

```javascript
if (!fileInput.files[0] || !jd) {
  alert("Please provide both..."); // Check if both fields filled
  return;
}
```

**Step 3 - Show Loading State:**

```javascript
btn.disabled = true; // Disable button
btnText.innerText = "AI is thinking..."; // Show loading message
loader.classList.remove("hidden"); // Show spinner
```

**Step 4 - Send Data to Backend:**

```javascript
const formData = new FormData();
formData.append("job_description", jd); // Add job description
formData.append("resume", fileInput.files[0]); // Add resume file

const response = await fetch("/analyze", {
  // Send to /analyze endpoint
  method: "POST",
  body: formData,
});
```

**Step 5 - Handle Response:**

```javascript
const data = await response.json(); // Parse response
document.getElementById("matchScore").innerText = data.match_score; // Show score
document.getElementById("aiFeedback").innerHTML = data.analysis; // Show analysis
resultsArea.classList.remove("hidden"); // Display results
```

**Key Feature - Timeout Handling:**

```javascript
const controller = new AbortController();
const timeout = setTimeout(() => controller.abort(), 300000); // 5 minute timeout
// Prevents hanging requests if backend is slow
```

---

### **4. static/css/style.css** - The Styling

```
ROLE: Make the UI beautiful
PURPOSE: Visual design and animations
```

**What it styles:**

- ✅ Glassmorphism background (frosted glass effect)
- ✅ Form inputs (textarea, file upload)
- ✅ Buttons and hover effects
- ✅ Loading spinner animation
- ✅ Results card display
- ✅ Responsive mobile design

---

### **5. app/api/analyzer.py** - The API Endpoint

```
ROLE: Receives requests from frontend, orchestrates the analysis
PURPOSE: Main coordinator between frontend and backend services
```

**What it does:**

**Endpoint Definition:**

```python
@router.post("/analyze")
async def analyze_resume(job_description: str = Form(...), resume: UploadFile = File(...)):
```

- ✅ Listens for POST requests to `/analyze`
- ✅ Receives form data (job_description and resume file)

**Processing Pipeline:**

```python
# Step 1: Extract text from PDF
content = await resume.read()                              # Read uploaded PDF file
resume_text = extract_text(content)                        # Extract text (uses parser.py)

# Step 2: Send to AI for analysis
score, analysis = get_intelligent_analysis(               # Get AI analysis (uses ai_engine.py)
    resume_text,
    job_description
)

# Step 3: Return results to frontend
return {
    "match_score": score,        # e.g., "87%"
    "analysis": analysis         # e.g., "3 Key Strengths: ..."
}
```

**Error Handling:**

```python
try:
    # ... processing ...
except Exception as e:
    return {"match_score": "Error", "analysis": f"Server error: {str(e)}"}
```

---

### **6. app/services/parser.py** - The PDF Extractor

```
ROLE: Extract text from PDF files
PURPOSE: Convert PDF → Text
```

**What it does:**

```python
def extract_text(file_bytes):
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        # Reads each page in the PDF
        # Extracts text from each page
        # Joins all pages together
        text = " ".join([page.extract_text() for page in pdf.pages])
        return text.strip()
```

**Example:**

```
Input:  Resume.pdf (binary file)
           ↓
Process: Extract all text from all pages
           ↓
Output: "John Doe, Software Engineer, Python, Java, AWS..."
```

**Error Handling:**

```python
except Exception as e:
    print(f"Extraction Error: {e}")
    return ""  # Return empty string if PDF is corrupt
```

---

### **7. app/services/ai_engine.py** - The AI Analyzer

```
ROLE: Send data to Ollama LLM for analysis
PURPOSE: Generate intelligent match score and analysis
```

**What it does:**

**Step 1 - Create Prompt:**

```python
prompt = f"""
You are an expert technical recruiter. Analyze the following Resume against the Job Description.

Provide the output in this EXACT format:
MATCH SCORE: [0-100]%

ANALYSIS:
- 3 Key Strengths: (List 3 things that match well)
- 3 Missing Skills/Gaps: (List 3 missing technologies or experiences)
- Advice: (One sentence on how to improve the resume for this specific role)

JOB DESCRIPTION:
{jd_text}

RESUME:
{resume_text}
"""
```

**Step 2 - Send to Ollama (Local AI):**

```python
response = client.chat(model='mistral', messages=[
    {'role': 'user', 'content': prompt},
])
```

- ✅ Connects to Ollama running on `http://127.0.0.1:11434`
- ✅ Uses Mistral LLM model
- ✅ Sends the prompt with both resume and job description
- ✅ Gets back AI-generated analysis

**Step 3 - Parse Response:**

```python
full_text = response['message']['content']

if "MATCH SCORE:" in full_text:
    parts = full_text.split("ANALYSIS:")
    score = parts[0].replace("MATCH SCORE:", "").strip()      # Extract score
    analysis = parts[1].strip()                               # Extract analysis
else:
    score = "N/A"
    analysis = full_text
```

**Example:**

```
LLM Response:
"MATCH SCORE: 85%

ANALYSIS:
- 3 Key Strengths: Python, REST APIs, 3+ years experience
- 3 Missing Skills/Gaps: Kubernetes, Go, Docker
- Advice: Learn Kubernetes to strengthen your application."

Result Parsed:
score = "85%"
analysis = "- 3 Key Strengths: ...\n- 3 Missing Skills/Gaps: ...\n- Advice: ..."
```

**Error Handling:**

```python
except ConnectionError:
    return "Error", "Could not connect to Ollama. Make sure Ollama is running"
except Exception as e:
    return "Error", f"Analysis failed: {str(e)}"
```

---

## 🔄 Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER BROWSER                              │
│  (http://127.0.0.1:8000)                                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                    ┌──────────────────┐
                    │ static/           │
                    │ index.html        │ ← Shows form
                    │ style.css         │ ← Beautifies it
                    └──────────────────┘
                              ↓
                    User fills form:
                    1. Paste Job Description
                    2. Upload Resume PDF
                    3. Click "Analyze Now"
                              ↓
            ┌─────────────────────────────────────┐
            │ static/js/script.js                  │
            │ (analyzeResume function triggered)  │
            │                                      │
            │ ✅ Validates inputs                  │
            │ ✅ Shows loading spinner             │
            │ ✅ Disables button                   │
            │ ✅ Creates FormData                  │
            │ ✅ POSTs to /analyze                 │
            └─────────────────────────────────────┘
                              ↓
                    ┌──────────────────────┐
                    │ Backend Server       │
                    │ (app/main.py)        │
                    │ Listening on :8000   │
                    └──────────────────────┘
                              ↓
                    Request arrives at
                    POST /analyze
                              ↓
            ┌──────────────────────────────────┐
            │ app/api/analyzer.py              │
            │ @router.post("/analyze")         │
            │                                  │
            │ Receives:                        │
            │ - job_description (string)       │
            │ - resume (PDF file)              │
            └──────────────────────────────────┘
                              ↓
                    ┌──────────────────────┐
                    │ Step 1: Parse PDF    │
                    │ app/services/        │
                    │ parser.py            │
                    │                      │
                    │ extract_text()       │
                    │ Input:  PDF binary   │
                    │ Output: Text string  │
                    └──────────────────────┘
                              ↓
                    ┌──────────────────────────┐
                    │ Step 2: AI Analysis      │
                    │ app/services/            │
                    │ ai_engine.py             │
                    │                          │
                    │ get_intelligent_analysis │
                    │ Input:  resume_text,     │
                    │         job_description  │
                    │ Process: Connect to      │
                    │          Ollama LLM      │
                    │ Output: score,           │
                    │         analysis         │
                    └──────────────────────────┘
                              ↓
                    ┌──────────────────────┐
                    │ External: Ollama     │
                    │ (Local AI Model)     │
                    │                      │
                    │ Model: Mistral       │
                    │ Endpoint: :11434     │
                    │                      │
                    │ Analyzes:            │
                    │ Resume vs Job Desc   │
                    │ Returns: Analysis    │
                    └──────────────────────┘
                              ↓
                    ┌──────────────────────┐
                    │ Step 3: Format        │
                    │ Response              │
                    │                       │
                    │ Parse Ollama output   │
                    │ Extract score         │
                    │ Extract analysis      │
                    │ Return as JSON        │
                    └──────────────────────┘
                              ↓
                    Response sent back
                    {
                      "match_score": "87%",
                      "analysis": "..."
                    }
                              ↓
            ┌──────────────────────────────────┐
            │ static/js/script.js              │
            │ Receives response                │
            │                                  │
            │ ✅ Hide loading spinner           │
            │ ✅ Enable button                  │
            │ ✅ Show results area              │
            │ ✅ Display score                  │
            │ ✅ Display analysis               │
            └──────────────────────────────────┘
                              ↓
            ┌──────────────────────────────────┐
            │ Browser displays:                │
            │ - Match Score: 87%               │
            │ - Analysis with feedback         │
            │ - Suggestions for improvement    │
            └──────────────────────────────────┘
```

---

## 📊 Data Flow Summary

### **Frontend → Backend**

```
User Input (HTML)
    ↓
JavaScript validation
    ↓
FormData (job_description + resume file)
    ↓
POST /analyze
    ↓
Backend receives
```

### **Backend Processing**

```
PDF file
    ↓ (parser.py)
Extract text
    ↓ (analyzer.py)
Prepare AI prompt
    ↓ (ai_engine.py)
Send to Ollama LLM
    ↓ (Ollama service)
Get AI response
    ↓ (ai_engine.py)
Parse score & analysis
    ↓ (analyzer.py)
Return JSON response
```

### **Backend → Frontend**

```
JSON Response
    ↓
JavaScript processes
    ↓
Update DOM
    ↓
User sees results
```

---

## 🔑 Key Technologies & Their Role

| Technology     | File                      | Purpose                       |
| -------------- | ------------------------- | ----------------------------- |
| **FastAPI**    | app/main.py               | Web framework & routing       |
| **Uvicorn**    | app/main.py               | ASGI server (runs FastAPI)    |
| **pdfplumber** | app/services/parser.py    | Extract text from PDFs        |
| **Ollama**     | app/services/ai_engine.py | Local LLM (AI model)          |
| **Mistral**    | app/services/ai_engine.py | The AI model (language model) |
| **HTML**       | static/index.html         | User interface                |
| **CSS**        | static/css/style.css      | Visual styling                |
| **JavaScript** | static/js/script.js       | Interactive frontend logic    |

---

## 🚀 Complete Startup Flow

```
1. User runs: python -m app.main
   ↓
2. app/main.py initializes FastAPI
   ↓
3. app/main.py starts Uvicorn server on :8000
   ↓
4. User opens browser: http://127.0.0.1:8000
   ↓
5. Browser requests GET /
   ↓
6. app/main.py serves static/index.html
   ↓
7. Browser loads HTML + CSS + JavaScript
   ↓
8. User sees the form ready for input
   ↓
9. User interaction triggers analyzeResume() in script.js
   ↓
10. JavaScript sends POST /analyze with form data
    ↓
11. analyzer.py receives request
    ↓
12. parser.py extracts text from PDF
    ↓
13. ai_engine.py sends to Ollama LLM
    ↓
14. Ollama returns AI analysis
    ↓
15. analyzer.py formats and returns response
    ↓
16. script.js displays results on screen
```

---

## 💡 Summary

**Think of it like a team working together:**

1. **HTML** = The application's face (what user sees)
2. **CSS** = The application's makeup (how it looks)
3. **JavaScript** = The application's hands (what it does when clicked)
4. **main.py** = The application's backbone (holds everything together)
5. **analyzer.py** = The application's brain (makes decisions)
6. **parser.py** = The application's eyes (reads the resume)
7. **ai_engine.py** = The application's expert advisor (analyzes via AI)
8. **Ollama** = The external AI (the actual thinking happens here)

**Each piece is essential and contributes to making the whole system work!**
