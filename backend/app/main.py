from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager

# Import routers (will be created later)
# from app.api.v1.router import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up Photography Gallery API...")
    yield
    # Shutdown
    print("Shutting down Photography Gallery API...")

app = FastAPI(
    title="Photography Gallery API",
    description="Backend API for a modern photography gallery website",
    version="1.0.0",
    lifespan=lifespan
)

# Security middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
# app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Photography Gallery API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "photography-gallery-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
