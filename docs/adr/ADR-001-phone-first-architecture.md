# ADR-001: Phone-First Architecture

## Status
Accepted

## Date
2026-02-16

## Context

The primary challenge in serving learners in resource-constrained environments is the assumption that infrastructure (servers, networks, reliable power) is available. Traditional e-learning platforms are designed as client-server architectures where:
- Mobile devices are "thin clients"
- Core functionality requires server connectivity
- Content delivery assumes reliable internet
- Edge devices are assumed to be always available

However, our target users face:
- Unreliable or no internet connectivity
- Limited or no local server infrastructure
- Power outages and infrastructure failures
- Low-cost, low-spec mobile devices as primary computing platform

The question is: What should be the primary computing platform for the MaS system?

## Decision

**We will adopt a phone-first architecture where mobile devices are the primary computing platform, not clients.**

Specifically:
1. All core functionality must work on the mobile device alone
2. The mobile app contains complete business logic
3. Content is fully stored and processed on-device
4. Offline operation is the default, not an exception
5. Edge devices and cloud services are optional enhancers, not requirements

This means:
- Mobile app has complete feature set
- Local database and storage on device
- Content packages are self-contained
- Sync is opportunistic, not required
- Edge devices accelerate but don't enable

## Consequences

### Positive
- **True Offline Capability**: Works anywhere without connectivity
- **Resilience**: No single point of failure
- **Cost Efficiency**: No mandatory infrastructure costs
- **Deployment Flexibility**: Can start with just mobile devices
- **User Empowerment**: Learners are not dependent on external systems
- **Scalability**: Scales horizontally with each device
- **Privacy**: Data stays on user's device by default

### Negative
- **Increased App Complexity**: More logic in mobile app
- **Storage Requirements**: Must store more data locally
- **Sync Complexity**: Conflict resolution needed
- **App Size**: Larger app with more features
- **Device Requirements**: Need sufficient mobile specs
- **Update Challenges**: Can't force immediate updates

### Neutral
- **Development Focus**: More mobile development, less backend
- **Testing Scope**: Need extensive offline testing
- **Architecture Pattern**: Different from typical mobile apps

## Compliance

### Aligns With
- **Constraint**: Works without reliable connectivity
- **Vision**: Democratize access regardless of infrastructure
- **User Need**: Sarah (rural learner) has no internet at home
- **Design Principle**: Offline-first design

### Enables
- **Deployment Mode 1**: Mobile-only deployment
- **Progressive Enhancement**: Edge devices as optional accelerators
- **Graceful Degradation**: System works in worst-case scenario

### Requires
- Careful mobile app architecture
- Efficient local storage
- Smart content packaging
- Robust sync strategy

## Related Decisions
- ADR-002: Offline-First Design (complementary)
- ADR-003: Edge Device as Accelerator (dependent on this)

## Notes

### Implementation Implications
1. Need robust local database (SQLite or similar)
2. Content must be packaged for offline distribution
3. ML models must be mobile-optimized
4. Sync queue for deferred operations
5. Conflict resolution strategy needed

### Alternative Considered: Client-Server Architecture
**Why Rejected**: Requires infrastructure that may not exist in target environments. Would exclude our primary users (like Sarah) who have no reliable connectivity.

### Alternative Considered: Progressive Web App (PWA)
**Why Rejected**: While PWAs offer some offline capability, they:
- Have limited offline storage
- Require initial connectivity
- Have less device integration
- Perform worse on low-end devices

### Success Criteria
- App functions 100% offline for core features
- No degradation in primary use cases without connectivity
- Users like Sarah can complete full learning cycle without ever connecting

### Review Date
To be reviewed after initial pilot deployment (6 months)
