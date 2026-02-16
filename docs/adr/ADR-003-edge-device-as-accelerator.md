# ADR-003: Edge Device as Accelerator

## Status
Accepted

## Date
2026-02-16

## Context

With phone-first architecture (ADR-001) and offline-first design (ADR-002), we've established that mobile devices must work independently. However, in some environments, local infrastructure (edge devices) may be available.

The question: What role should edge devices play in the architecture?

Options considered:
1. **Required Gateway**: All mobile devices must connect through edge
2. **Optional Sync Hub**: Edge provides coordination and caching
3. **Pure Accelerator**: Edge enhances performance but isn't required
4. **No Edge Devices**: Mobile-only architecture

Considerations:
- Some schools have or can acquire edge hardware
- Edge devices could provide value (caching, acceleration)
- But many environments have no infrastructure
- Architecture must work without edge devices
- Adding edge shouldn't break mobile-only deployments

## Decision

**Edge devices are optional accelerators that enhance performance and capabilities but are never required for core functionality.**

Role of edge devices:
1. **ML Acceleration**: Run heavier ML models with results sent to mobile
2. **Content Caching**: Cache content for efficient local distribution
3. **Sync Aggregation**: Batch sync from multiple devices to cloud
4. **Classroom Orchestration**: Teacher dashboard and coordination
5. **Network Optimization**: Efficient bandwidth usage

Architecture principle:
- **Mobile works without edge**: All features available
- **Mobile discovers edge**: Auto-detect when available
- **Transparent enhancement**: Mobile app works same way with or without edge
- **Graceful fallback**: If edge fails, mobile continues independently

## Consequences

### Positive
- **Deployment Flexibility**: Can start without edge devices
- **Cost Efficiency**: Infrastructure is optional investment
- **Resilience**: No single point of failure
- **Scalability**: Can add edge devices as needed
- **Progressive Enhancement**: Infrastructure adds value when available
- **Backward Compatibility**: Mobile-only deployments remain valid

### Negative
- **Complexity**: Must handle both scenarios (with/without edge)
- **Discovery Logic**: Need auto-discovery mechanism
- **Dual Testing**: Test with and without edge devices
- **Feature Parity**: Must maintain feature parity
- **Code Paths**: Multiple execution paths to maintain

### Neutral
- **Architecture Complexity**: More sophisticated than single-tier
- **Development Cost**: More scenarios to implement
- **Documentation**: Need to explain both modes

## Compliance

### Aligns With
- **Constraint**: Cannot assume infrastructure availability
- **Vision**: Works in any environment
- **User Need**: Sarah has no edge device available
- **Deployment Modes**: Supports Mode 1 (mobile-only) through Mode 4 (with edge)
- **Architecture**: Phone-first (ADR-001)

### Enables
- Classroom deployments with edge devices (Modes 2-4)
- Performance enhancement where infrastructure exists
- Teacher dashboards and orchestration
- Efficient content distribution in schools

### Requires
- Service discovery mechanism
- Fallback logic throughout app
- Feature flags for edge-enhanced features
- Testing both scenarios

## Related Decisions
- ADR-001: Phone-First Architecture (foundational)
- ADR-002: Offline-First Design (complementary)

## Notes

### Edge Device Capabilities

#### What Edge Devices Provide

**1. ML Inference Acceleration**
- Mobile sends data to edge for inference
- Edge runs larger/better models
- Results returned to mobile
- Fallback: Mobile uses on-device models

**2. Content Distribution**
- Edge caches content packages
- Mobile downloads from local edge (faster, free)
- Fallback: Mobile uses pre-loaded or cloud content

**3. Sync Aggregation**
- Edge collects sync data from multiple mobiles
- Batches uploads to cloud
- More efficient bandwidth usage
- Fallback: Mobile syncs directly to cloud

**4. Classroom Features**
- Teacher dashboard shows student progress
- Real-time classroom status
- Content assignment and management
- Fallback: These features unavailable

#### What Edge Devices Don't Provide
- Required functionality (all optional)
- User authentication (handled on mobile)
- Primary data storage (mobile is source of truth)
- Content authoring (separate tool)

### Architecture Patterns

#### Service Discovery
```
Mobile App Starts
    ↓
Check for Edge Device (mDNS/local network scan)
    ↓
    ├─ Found → Register with edge, enable enhancements
    └─ Not Found → Continue with mobile-only mode
```

#### Feature Enhancement
```
User Action (e.g., run ML inference)
    ↓
Edge Available?
    ├─ Yes → Send to edge, wait for result
    │         ├─ Success → Use result
    │         └─ Timeout/Error → Fallback to mobile
    └─ No → Run on mobile
```

#### Graceful Degradation
- All features have mobile fallback
- Timeout handling for edge requests
- Automatic failover to mobile processing
- No error messages about missing edge

### Testing Requirements
1. All features work without edge device
2. Enhanced performance with edge device
3. Failover scenarios (edge goes offline)
4. Network partition scenarios
5. Load testing with and without edge

### Implementation Guidelines

**Mobile App**:
- Never assume edge is available
- Always have fallback path
- Timeout edge requests quickly
- Fail gracefully and transparently

**Edge Device**:
- Stateless where possible
- No required state for mobile operation
- Can restart without affecting mobile
- Publish capabilities via discovery

### Alternative Considered: Required Gateway

**Why Rejected**:
- Excludes mobile-only deployments
- Creates single point of failure
- Violates phone-first principle
- Conflicts with offline-first design
- Increases deployment complexity

### Alternative Considered: No Edge Devices

**Why Rejected**:
- Misses opportunity for enhancement
- Limits performance in equipped schools
- Reduces value of infrastructure investment
- Doesn't serve all deployment scenarios

### Success Criteria
- 100% of features work without edge device
- Edge device improves performance/capabilities when present
- Transition between modes is seamless
- Users unaware whether edge is present or not
- Mobile-only deployments are fully supported

### Review Date
After initial edge device deployment in pilot schools (12 months)
