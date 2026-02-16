# ADR-002: Offline-First Design

## Status
Accepted

## Date
2026-02-16

## Context

Given our phone-first architecture (ADR-001), we must decide how to handle the relationship between offline and online functionality. Traditional approaches include:

1. **Online-First**: Assume connectivity, add offline caching
2. **Offline-Capable**: Core features work online, some work offline
3. **Offline-First**: Design for offline, treat connectivity as enhancement

Our users face:
- Unpredictable connectivity (available only periodically)
- High latency when connected (>500ms)
- Expensive data costs
- Low bandwidth (2G speeds)

The key question: Should we design assuming connectivity is available or unavailable?

## Decision

**We will adopt an offline-first design philosophy where offline is the default operating mode and connectivity is treated as an enhancement.**

This means:
1. All core user journeys work completely offline
2. Connectivity is used only for sync, updates, and enhancements
3. Online features are progressive enhancements
4. App feels the same whether online or offline
5. Network failures never block user actions

Implementation principles:
- **Local-First Data**: All data stored locally first
- **Eventual Sync**: Data syncs when possible, not required
- **Optimistic UI**: Show results immediately, sync later
- **Queue Operations**: Network requests queued if offline
- **Graceful Degradation**: Online features fail gracefully

## Consequences

### Positive
- **Reliable Experience**: Works consistently regardless of connectivity
- **Performance**: No network latency for core operations
- **Data Costs**: Minimal data usage
- **User Confidence**: Users trust it will work
- **Resilience**: Network issues don't block learning
- **Privacy**: Less data transmitted
- **Accessibility**: Works in areas with no connectivity

### Negative
- **Sync Complexity**: Must handle conflicts and eventual consistency
- **Storage Requirements**: More local storage needed
- **Stale Data**: Local data may be outdated
- **Testing Complexity**: Must test all offline scenarios
- **Cache Management**: Need strategy for managing local data
- **Collaboration Limits**: Real-time collaboration is harder

### Neutral
- **Mental Model**: Different from typical online apps
- **Architecture Pattern**: Requires specific patterns (CQRS, event sourcing)
- **Development Approach**: Must always consider offline case

## Compliance

### Aligns With
- **Constraint**: Unreliable connectivity
- **Vision**: Works anywhere, anytime
- **User Need**: Sarah has no home internet
- **Design Principle**: Resilient by design
- **Architecture**: Phone-first (ADR-001)

### Enables
- All core features work offline
- Minimal data requirements
- Consistent user experience
- Battery efficiency (less network usage)

### Requires
- Local database with full schema
- Sync queue and conflict resolution
- Content packaging for offline distribution
- Local-first state management

## Related Decisions
- ADR-001: Phone-First Architecture (foundational)
- ADR-003: Edge Device as Accelerator (sync target)

## Notes

### Implementation Strategy

#### Core Offline Features
1. **Content Access**: All lessons available locally
2. **Assessment Taking**: Complete quizzes offline
3. **Progress Tracking**: Track completion locally
4. **Navigation**: Full app navigation
5. **Search**: Search local content

#### Sync Strategy
1. **When Connected**: Background sync of changes
2. **Prioritization**: User data > analytics > content updates
3. **Conflict Resolution**: Last-write-wins with user override
4. **Bandwidth Awareness**: Adapt to connection quality
5. **Scheduled Sync**: Allow user to control when sync happens

#### Data Architecture
```
Local Device State (Source of Truth)
        ↓
    Sync Queue
        ↓
    When Connected → Edge/Cloud
        ↓
    Conflict Resolution
        ↓
    Update Local State
```

### What Requires Connectivity

**Nice-to-Have Online Features**:
- Progress sync to cloud
- Content updates
- Teacher communication
- Collaborative features
- Real-time leaderboards
- Social features

**Does NOT Require Connectivity**:
- Accessing content
- Taking assessments
- Tracking progress
- Viewing history
- Earning badges
- Searching content

### Alternative Considered: Online-First with Offline Mode

**Why Rejected**: 
- Treats offline as exception, not norm
- Features often broken in offline mode
- Users feel second-class when offline
- Doesn't match user reality
- Leads to poor offline experience

### Alternative Considered: Offline-Capable

**Why Rejected**:
- Ambiguous which features work offline
- Often leads to partial functionality
- Confusing user experience
- Doesn't go far enough for our users

### Testing Requirements
1. All tests must pass with network disabled
2. Test sync in various network conditions
3. Test conflict resolution scenarios
4. Test with network disconnecting mid-operation
5. Performance tests must not depend on network

### Success Criteria
- 100% of core user journeys work offline
- No "you're offline" error messages for core features
- Users can go weeks without connectivity and still use app fully
- Network failures are invisible to users

### Review Date
Continuous - offline-first is a permanent design principle
