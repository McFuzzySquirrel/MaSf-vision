# Edge Device Architecture

## Overview

The edge device is an **optional accelerator** that enhances the mobile experience but is not required for core functionality. It serves as a local hub for a classroom or school.

## Purpose

The edge device provides:
- ML model inference acceleration
- Content caching and distribution
- Local synchronization hub
- Bandwidth optimization
- Classroom orchestration

## Architecture

```
┌─────────────────────────────────┐
│      API Gateway                │
│   (Mobile Device Interface)     │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│    Service Layer                │
│  - Model Inference              │
│  - Content Distribution         │
│  - Sync Coordination            │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│    Storage Layer                │
│  - Content Cache                │
│  - Model Storage                │
│  - Sync State                   │
└─────────────────────────────────┘
```

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

### Minimum Configuration
- CPU: 4 cores
- RAM: 4GB
- Storage: 500GB
- Network: WiFi AP capability

### Recommended Configuration
- CPU: 8 cores (with GPU)
- RAM: 8GB
- Storage: 1TB SSD
- Network: Dual WiFi (AP + WAN)

## Software Stack

- OS: Linux (Ubuntu/Debian)
- Runtime: Docker containers
- Services: Microservices architecture
- Database: PostgreSQL for state

## Deployment Modes

1. **Classroom Node**: Single classroom, ~30 devices
2. **School Hub**: Multiple classrooms, ~300 devices
3. **District Server**: Multiple schools, ~3000 devices

## Network Architecture

```
Internet ◄─── [Edge Node] ◄─── Mobile Devices
              (Optional)        (Primary)
```

## Graceful Degradation

If edge node is unavailable:
- Mobile devices continue full functionality
- Direct cloud sync when connected
- No loss of core features
- Automatic failover

## Related Documents

- [System Overview](system-overview.md)
- [Deployment Modes](deployment-modes.md)
