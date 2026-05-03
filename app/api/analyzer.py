from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser import extract_text
from app.services.ai_engine import get_intelligent_analysis

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(job_description: str = Form(...), resume: UploadFile = File(...)):
    try:
        # 1. Read PDF
        content = await resume.read()
        resume_text = extract_text(content)
        
        if not resume_text:
            return {"match_score": "0%", "analysis": "Error: Could not read PDF."}
        
        # 2. Run AI Analysis
        score, analysis = get_intelligent_analysis(resume_text, job_description)
        
        return {
            "match_score": score,
            "analysis": analysis
        }
    except Exception as e:
        return {"match_score": "Error", "analysis": f"Server error: {str(e)}"}