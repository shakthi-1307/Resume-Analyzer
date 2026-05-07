from groq import Groq
import os

# Initialize Groq client with API key from environment
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set. Please set your Groq API key.")

client = Groq(api_key=api_key)

def get_intelligent_analysis(resume_text, jd_text):
    """Sends resume and JD to Groq's LLM for deep analysis."""
    
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
        # Use Groq's fast inference with mixtral-8x7b model
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="mixtral-8x7b-32768",  # Fast, powerful free model from Groq
            temperature=0.7,
            max_tokens=1024,
        )
        
        full_text = chat_completion.choices[0].message.content
        
        # Logic to split the score from the text for the UI
        if "MATCH SCORE:" in full_text:
            parts = full_text.split("ANALYSIS:")
            score = parts[0].replace("MATCH SCORE:", "").strip()
            analysis = parts[1].strip() if len(parts) > 1 else "Analysis pending..."
        else:
            score = "N/A"
            analysis = full_text

        return score, analysis
        
    except Exception as e:
        error_msg = str(e)
        print(f"Groq API Error: {error_msg}")
        
        if "api_key" in error_msg.lower():
            return "Error", "Groq API key not configured. Contact administrator."
        elif "rate_limit" in error_msg.lower():
            return "Error", "Rate limit exceeded. Please try again in a moment."
        else:
            return "Error", f"Analysis failed: {error_msg}"