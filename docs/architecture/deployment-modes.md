# Deployment Modes

## Overview

MaS supports multiple deployment modes to accommodate different contexts and resource availability.

## Mode 1: Mobile-Only (Minimum Viable)

### Description
Students use only mobile devices with no edge infrastructure.

### Characteristics
- Fully offline capable
- Content pre-loaded via USB/SD card or initial download
- Progress syncs when internet available
- Peer-to-peer content sharing (optional)

### Use Cases
- Remote/rural areas
- Home learning
- Individual learners
- Emergency/displacement scenarios

### Requirements
- Mobile device with app installed
- Content packages
- Optional: periodic internet access

## Mode 2: Classroom Edge Node

### Description
Single edge device serving one classroom of ~30 students.

### Characteristics
- Local WiFi network
- Faster content distribution
- Accelerated ML inference
- Real-time teacher dashboard
- Aggregated sync

### Use Cases
- Standard classroom
- Computer lab
- Training center

### Requirements
- Edge device (mini PC or similar)
- WiFi router/AP
- Mobile devices
- Optional: internet connection

## Mode 3: School Hub

### Description
Central edge device serving entire school (~300 students).

### Characteristics
- School-wide WiFi
- Centralized content management
- Cross-classroom coordination
- School-level analytics
- Efficient bandwidth usage

### Use Cases
- Primary/secondary schools
- Multi-classroom facilities
- Learning centers

### Requirements
- Robust edge server
- School network infrastructure
- Multiple mobile devices
- Reliable internet (recommended)

## Mode 4: District Server

### Description
Large-scale deployment across multiple schools.

### Characteristics
- District-level coordination
- Centralized content distribution
- Aggregate analytics
- Multiple school synchronization

### Use Cases
- School districts
- Large educational organizations
- Government deployments

### Requirements
- Server infrastructure
- Network connectivity between schools
- Fleet management tools
- Dedicated IT support

## Mode 5: Hybrid Cloud

### Description
Cloud-first deployment with mobile edge caching.

### Characteristics
- Always-connected assumption
- Cloud-based services
- Mobile apps as thin clients
- Local caching for resilience

### Use Cases
- Urban areas with reliable internet
- Pilot programs
- Development/testing

### Requirements
- Reliable internet connectivity
- Cloud infrastructure
- Mobile devices

## Migration Paths

### Scaling Up
1. Mobile-Only → Classroom Edge → School Hub → District Server
2. Gradual infrastructure investment
3. Backward compatible at each stage

### Scaling Down
- All modes support graceful degradation
- System adapts to available resources
- Core functionality always available

## Decision Matrix

| Mode | Infrastructure | Connectivity | Capacity | Cost |
|------|----------------|-------------|----------|------|
| Mobile-Only | None | Optional | 1-∞ | $ |
| Classroom | Edge device | Local WiFi | ~30 | $$ |
| School Hub | Server | School network | ~300 | $$$ |
| District | Data center | WAN | ~3000 | $$$$ |
| Hybrid Cloud | Cloud | Always-on | Unlimited | $$-$$$$ |

## Related Documents

- [System Overview](system-overview.md)
- [Phone Architecture](phone-architecture.md)
- [Edge Device Architecture](edge-device-architecture.md)
