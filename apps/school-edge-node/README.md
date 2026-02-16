# School Edge Node

## Overview

The School Edge Node is an **optional** accelerator that enhances the mobile experience but is never required for core functionality.

## Purpose

The edge device provides:
- ML model inference acceleration
- Content caching and distribution
- Local synchronization hub
- Bandwidth optimization
- Classroom orchestration

## Architecture Principle

**Mobile works without edge** - This is critical:
- All features available on mobile alone
- Edge provides performance enhancement
- Graceful fallback when edge unavailable
- No feature gating on edge presence

## Key Services

### 1. Model Inference Service
- Accelerated ML inference
- Batch processing
- Model caching
- Fallback to mobile if unavailable

### 2. Content Distribution
- Local content caching
- Efficient distribution to mobile devices
- Version management
- Bandwidth optimization

### 3. Synchronization Hub
- Aggregate mobile device sync
- Batch uploads to cloud
- Conflict resolution
- Connection pooling

### 4. Classroom Orchestration
- Teacher dashboard
- Student progress monitoring
- Content assignment
- Real-time status

## Hardware Requirements

### Minimum
- CPU: 4 cores
- RAM: 4GB
- Storage: 500GB
- Network: WiFi AP capability

### Recommended
- CPU: 8 cores (with GPU)
- RAM: 8GB
- Storage: 1TB SSD
- Network: Dual WiFi (AP + WAN)

## Technology Stack

**Current Implementation**: Python with FastAPI
- FastAPI for REST API endpoints
- Uvicorn ASGI server
- Pydantic for data validation
- Easy deployment and remote management
- Container-ready (Docker support)

## Deployment Modes

1. **Classroom Node**: ~30 devices
2. **School Hub**: ~300 devices
3. **District Server**: ~3000 devices

## Development

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup
```bash
# Navigate to the school-edge-node directory
cd apps/school-edge-node

# Install dependencies
pip install -r requirements.txt
```

### Running

#### Development Mode
```bash
# Run the API server
python api_server.py
```

The API will be available at:
- API Root: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/health
- Discovery Endpoint: http://localhost:8000/api/v1/discover

#### Production Mode
```bash
# Run with uvicorn directly
uvicorn api_server:app --host 0.0.0.0 --port 8000 --workers 4
```

### Testing
```bash
# Test the API endpoints
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/discover
curl http://localhost:8000/api/v1/services
```

## Project Structure

```
school-edge-node/
├── services/
│   ├── inference/       # ML inference service
│   ├── content/         # Content distribution
│   ├── sync/            # Sync coordination
│   └── orchestration/   # Classroom management
├── tests/
└── docs/
```

## Graceful Degradation

If edge node is unavailable:
- Mobile devices continue full functionality
- Direct cloud sync when connected
- No loss of core features
- Automatic failover

## Related Documents

- [Edge Device Architecture](../../docs/architecture/edge-device-architecture.md)
- [Deployment Modes](../../docs/architecture/deployment-modes.md)
- [ADR-003: Edge Device as Accelerator](../../docs/adr/ADR-003-edge-device-as-accelerator.md)
