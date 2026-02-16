# System Overview

## Introduction

The Mobile Adaptive System (MaS) is designed as a distributed learning platform that prioritizes mobile devices as the primary computing platform, with optional edge devices providing acceleration capabilities.

## High-Level Architecture

```
┌─────────────────┐
│  Learner Mobile │ ◄─── Primary Platform
└────────┬────────┘
         │
         │ (Optional)
         ▼
┌─────────────────┐
│ School Edge Node│ ◄─── Accelerator
└─────────────────┘
```

## Core Components

### 1. Learner Mobile Application
- Primary user interface
- Offline-first design
- Local data storage
- Content delivery and interaction
- Progress tracking

### 2. School Edge Node (Optional)
- Model inference acceleration
- Content caching and distribution
- Device orchestration
- Local synchronization hub

## Design Principles

1. **Phone-First**: Mobile devices are the primary platform, not clients
2. **Offline-First**: All core functionality works without connectivity
3. **Progressive Enhancement**: Edge devices enhance but don't enable functionality
4. **Resource Conscious**: Designed for low-spec devices and limited connectivity

## Data Flow

1. Content is packaged and distributed offline
2. Mobile app operates independently
3. Edge node provides acceleration when available
4. Sync happens opportunistically

## Technology Stack

- Mobile: Cross-platform framework (TBD)
- Edge: Lightweight server (TBD)
- Models: Optimized for mobile inference
- Data: Local-first with eventual sync

## Related Documents

- [Phone Architecture](phone-architecture.md)
- [Edge Device Architecture](edge-device-architecture.md)
- [Deployment Modes](deployment-modes.md)
