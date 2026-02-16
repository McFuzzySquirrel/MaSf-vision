"""
School Edge Node API Gateway

Provides REST API endpoints for mobile devices to interact with the edge node.
This enables:
- Service discovery
- Content distribution
- Model inference acceleration
- Synchronization coordination
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="MaSf-vision Edge Node API",
    description="API Gateway for school edge node services",
    version="1.0.0"
)

# Configure CORS for mobile device access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify mobile app origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class EdgeNodeInfo(BaseModel):
    """Information about the edge node"""
    node_id: str
    node_name: str
    version: str
    status: str
    capabilities: List[str]
    timestamp: str

class ServiceStatus(BaseModel):
    """Status of edge node services"""
    service_name: str
    status: str
    available: bool

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    timestamp: str
    services: List[ServiceStatus]


# API Endpoints

@app.get("/", tags=["Info"])
async def root():
    """Root endpoint - API information"""
    return {
        "name": "MaSf-vision Edge Node API",
        "version": "1.0.0",
        "status": "operational",
        "documentation": "/docs"
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Health check endpoint for monitoring
    
    Returns the operational status of the edge node and its services.
    """
    services = [
        ServiceStatus(
            service_name="api_gateway",
            status="healthy",
            available=True
        ),
        ServiceStatus(
            service_name="content_distribution",
            status="not_implemented",
            available=False
        ),
        ServiceStatus(
            service_name="model_inference",
            status="not_implemented",
            available=False
        ),
        ServiceStatus(
            service_name="sync_coordination",
            status="not_implemented",
            available=False
        )
    ]
    
    return HealthResponse(
        status="operational",
        timestamp=datetime.utcnow().isoformat(),
        services=services
    )


@app.get("/api/v1/discover", response_model=EdgeNodeInfo, tags=["Discovery"])
async def discover():
    """
    Service discovery endpoint
    
    Mobile devices use this to discover edge node capabilities and services.
    This is the primary endpoint that other repositories should call.
    """
    return EdgeNodeInfo(
        node_id="edge-node-001",
        node_name="School Edge Node",
        version="1.0.0",
        status="operational",
        capabilities=[
            "api_gateway",
            "service_discovery",
            # Future capabilities:
            # "content_distribution",
            # "model_inference",
            # "sync_coordination",
            # "classroom_orchestration"
        ],
        timestamp=datetime.utcnow().isoformat()
    )


@app.get("/api/v1/services", tags=["Services"])
async def list_services():
    """
    List available services on this edge node
    
    Returns a list of services and their status.
    """
    return {
        "services": [
            {
                "name": "API Gateway",
                "endpoint": "/api/v1",
                "status": "operational",
                "description": "REST API for mobile device integration"
            },
            {
                "name": "Service Discovery",
                "endpoint": "/api/v1/discover",
                "status": "operational",
                "description": "Discover edge node capabilities"
            },
            {
                "name": "Content Distribution",
                "endpoint": "/api/v1/content",
                "status": "not_implemented",
                "description": "Local content caching and distribution"
            },
            {
                "name": "Model Inference",
                "endpoint": "/api/v1/inference",
                "status": "not_implemented",
                "description": "Accelerated ML model inference"
            },
            {
                "name": "Sync Coordination",
                "endpoint": "/api/v1/sync",
                "status": "not_implemented",
                "description": "Device synchronization hub"
            }
        ]
    }


@app.get("/api/v1/status", tags=["Status"])
async def node_status():
    """
    Get detailed edge node status
    
    Provides comprehensive status information for monitoring.
    """
    return {
        "node_id": "edge-node-001",
        "uptime": "unknown",
        "connected_devices": 0,
        "services_running": 2,
        "services_total": 5,
        "storage_available": "unknown",
        "load_average": "unknown",
        "last_updated": datetime.utcnow().isoformat()
    }


# Content Distribution Endpoints (Stubs for future implementation)

@app.get("/api/v1/content/packages", tags=["Content"])
async def list_content_packages():
    """List available content packages (not implemented)"""
    raise HTTPException(
        status_code=501,
        detail="Content distribution service not yet implemented"
    )


@app.get("/api/v1/content/packages/{package_id}", tags=["Content"])
async def get_content_package(package_id: str):
    """Download content package (not implemented)"""
    raise HTTPException(
        status_code=501,
        detail="Content distribution service not yet implemented"
    )


# Model Inference Endpoints (Stubs for future implementation)

@app.post("/api/v1/inference", tags=["Inference"])
async def run_inference():
    """Run model inference (not implemented)"""
    raise HTTPException(
        status_code=501,
        detail="Model inference service not yet implemented"
    )


# Sync Coordination Endpoints (Stubs for future implementation)

@app.post("/api/v1/sync/upload", tags=["Sync"])
async def upload_sync_data():
    """Upload sync data (not implemented)"""
    raise HTTPException(
        status_code=501,
        detail="Sync coordination service not yet implemented"
    )


def main():
    """Start the API server"""
    print("Starting MaSf-vision Edge Node API Gateway...")
    print("API Documentation: http://0.0.0.0:8000/docs")
    print("Health Check: http://0.0.0.0:8000/health")
    print("Discovery Endpoint: http://0.0.0.0:8000/api/v1/discover")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )


if __name__ == "__main__":
    main()
