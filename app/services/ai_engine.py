import ollama
from ollama import Client
import signal
import sys
import os

# Use environment variable for Ollama host, default to localhost
ollama_host = os.getenv('OLLAMA_HOST', 'http://127.0.0.1:11434')
client = Client(host=ollama_host)

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Analysis request timed out")

def get_intelligent_analysis(resume_text, jd_text, timeout_seconds=240):
    """Sends resume and JD to local LLM for deep analysis."""
    
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
    
    try:
        response = client.chat(model='qwen2.5:1.5b', messages=[
            {'role': 'user', 'content': prompt},
        ])
        
        full_text = response['message']['content']
        
        # Logic to split the score from the text for the UI
        if "MATCH SCORE:" in full_text:
            parts = full_text.split("ANALYSIS:")
            score = parts[0].replace("MATCH SCORE:", "").strip()
            analysis = parts[1].strip() if len(parts) > 1 else "Analysis pending..."
        else:
            score = "N/A"
            analysis = full_text

        return score, analysis
    except TimeoutError:
        return "Timeout", "The AI analysis took too long. Please try again."
    except ConnectionError:
        return "Error", "Could not connect to Ollama. Make sure Ollama is running (ollama serve)"
    except Exception as e:
        error_msg = str(e)
        print(f"Ollama Error: {error_msg}")
        return "Error", f"Analysis failed: {error_msg}"