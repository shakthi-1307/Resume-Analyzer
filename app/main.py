from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from app.api.analyzer import router as analyzer_router
from pathlib import Path
import os

app = FastAPI(title="Resume Analyzer", version="1.0.0")

# 1. Enable CORS (Must be before routes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add timeout middleware
@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        print(f"Request error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": f"Server error: {str(e)}"}
        )

# 2. Include the Router (This is the professional way)
# This connects the @router.post("/analyze") from analyzer.py to your app
app.include_router(analyzer_router)

# 3. Serve Static Files
# Use absolute path to ensure it works from any directory
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv('PORT', 8000))
    host = os.getenv('HOST', '0.0.0.0')  # 0.0.0.0 for production, 127.0.0.1 for local
    uvicorn.run(
        app, 
        host=host, 
        port=port
    )