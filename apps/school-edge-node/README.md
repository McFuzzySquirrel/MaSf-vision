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

**To Be Determined** - Will be selected based on:
- Linux compatibility
- Container support
- Resource efficiency
- Easy deployment
- Remote management

Candidates:
- Node.js services
- Python services
- Go services
- Docker/Kubernetes orchestration

## Deployment Modes

1. **Classroom Node**: ~30 devices
2. **School Hub**: ~300 devices
3. **District Server**: ~3000 devices

## Development

### Prerequisites
(To be added)

### Setup
(To be added)

### Running
(To be added)

### Testing
(To be added)

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
