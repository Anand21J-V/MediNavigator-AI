"""
MedConcierge — FastAPI Application Entry Point
feature/anand/project-setup
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

from config import settings

app = FastAPI(
    title="MedConcierge API",
    description="AI Medical Concierge for Travelers in India",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routers import chat, doctors, insurance  # noqa: E402

app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(doctors.router, prefix="/api", tags=["doctors"])
app.include_router(insurance.router, prefix="/api", tags=["insurance"])


@app.get("/health", tags=["system"])
async def health_check():
    """Liveness probe. Railway and UptimeRobot ping this every 5 min."""
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "service": "medconcierge-api",
            "version": "1.0.0",
            "timestamp": int(time.time()),
        },
    )


@app.get("/", tags=["system"])
async def root():
    return {"message": "MedConcierge API is running. Visit /docs for API reference."}