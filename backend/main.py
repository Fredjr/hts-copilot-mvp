from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from typing import Dict, Any

# Create FastAPI app instance
app = FastAPI(
    title="HTS Co-pilot API",
    description="Backend API for HTS Co-pilot - High Throughput Screening Analysis",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://hts-copilot.vercel.app"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint - API health check"""
    return {"message": "HTS Co-pilot API is running", "status": "healthy"}

@app.get("/health")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint for deployment monitoring"""
    return {
        "status": "healthy",
        "service": "hts-copilot-api",
        "version": "0.1.0"
    }

@app.get("/api/status")
async def api_status() -> Dict[str, Any]:
    """API status endpoint"""
    return {
        "status": "operational",
        "endpoints": {
            "health": "/health",
            "upload": "/api/upload",
            "analyze": "/api/analyze",
            "results": "/api/results/{id}",
            "experiments": "/api/experiments"
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 