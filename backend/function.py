import functions_framework
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from typing import Dict, Any
import os
from google.cloud import storage
from google.cloud import secretmanager

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
    allow_origins=[
        "http://localhost:3000", 
        "https://hts-copilot.vercel.app",
        "https://hts-copilot-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Google Cloud clients
storage_client = storage.Client()
secret_client = secretmanager.SecretManagerServiceClient()

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
        "version": "0.1.0",
        "platform": "Google Cloud Functions"
    }

@app.get("/api/status")
async def api_status() -> Dict[str, Any]:
    """API status endpoint"""
    return {
        "status": "operational",
        "platform": "Google Cloud Functions",
        "endpoints": {
            "health": "/health",
            "upload": "/api/upload",
            "analyze": "/api/analyze",
            "results": "/api/results/{id}",
            "experiments": "/api/experiments"
        }
    }

@app.get("/api/storage/test")
async def test_storage() -> Dict[str, Any]:
    """Test Google Cloud Storage connectivity"""
    try:
        bucket_name = os.getenv("GCS_BUCKET_NAME", "hts-copilot-uploads")
        bucket = storage_client.bucket(bucket_name)
        
        # Check if bucket exists
        if bucket.exists():
            return {
                "status": "success",
                "message": "Google Cloud Storage connected",
                "bucket": bucket_name
            }
        else:
            return {
                "status": "warning",
                "message": "Bucket does not exist",
                "bucket": bucket_name
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Storage connection failed: {str(e)}"
        }

# Google Cloud Functions entry point
@functions_framework.http
def hts_copilot_api(request):
    """HTTP Cloud Function entry point for HTS Co-pilot API"""
    import asyncio
    from fastapi import Request
    from fastapi.responses import Response
    
    # Convert Google Cloud Function request to FastAPI request
    async def handle_request():
        # Create a mock FastAPI request
        scope = {
            "type": "http",
            "method": request.method,
            "path": request.path,
            "headers": [(k.lower(), v) for k, v in request.headers.items()],
            "query_string": request.query_string.encode(),
        }
        
        # Route to appropriate FastAPI endpoint
        if request.path == "/":
            return await root()
        elif request.path == "/health":
            return await health_check()
        elif request.path == "/api/status":
            return await api_status()
        elif request.path == "/api/storage/test":
            return await test_storage()
        else:
            return {"error": "Endpoint not found", "path": request.path}
    
    # Run the async function
    result = asyncio.run(handle_request())
    
    # Convert FastAPI response to Google Cloud Function response
    import json
    return Response(
        json.dumps(result),
        status=200,
        headers={"Content-Type": "application/json"}
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
        log_level="info"
    ) 