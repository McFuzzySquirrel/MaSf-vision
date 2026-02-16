# AI Agent Instructions

## Overview

This document provides instructions for AI coding agents working on the MaS project. Follow these guidelines to ensure your contributions align with project goals and standards.

## Project Context

### What We're Building
MaS (Mobile Adaptive System) is a phone-first, offline-capable learning platform designed for resource-constrained environments. The mobile device is the primary platform, with optional edge devices serving as accelerators.

### Core Principles
1. **Offline-First**: All features must work offline
2. **Phone-First**: Mobile is primary, not a client
3. **Progressive Enhancement**: Edge devices enhance but don't enable
4. **Keep It Simple**: Avoid over-engineering
5. **Resilient**: Handle failures gracefully

## Before You Start

### Understand the Context
1. Read [Vision](../product/vision.md) to understand goals
2. Read [Constraints](../product/constraints.md) to understand limitations
3. Review relevant [ADRs](../adr/) for architectural decisions
4. Check [Coding Principles](coding-principles.md) for standards

### Key Architecture Decisions
- **ADR-001**: Phone-first architecture - mobile works independently
- **ADR-002**: Offline-first design - offline is default, online is enhancement
- **ADR-003**: Edge as accelerator - optional, not required

## Decision-Making Guidelines

### When Making Architectural Decisions

#### Always Consider:
1. **Does this work offline?** If not, it's not acceptable for core features
2. **Does this work on low-end devices?** Target 2GB RAM, Android 8+
3. **Is there a simpler solution?** Prefer simple over clever
4. **What if the edge device fails?** Must work without it
5. **What if there's no connectivity?** Must handle gracefully

#### Red Flags:
- ❌ Requires internet for core functionality
- ❌ Assumes edge device is available
- ❌ Only works on high-end devices
- ❌ Complex when simple would work
- ❌ Adds unnecessary dependencies

#### Green Lights:
- ✅ Works completely offline
- ✅ Degrades gracefully
- ✅ Simple and maintainable
- ✅ Tested on low-end devices
- ✅ Clear error handling

### Technology Choices

#### Prefer:
- Proven, stable technologies
- Lightweight solutions
- Open source with active maintenance
- Good offline support
- Mobile-optimized

#### Avoid:
- Bleeding-edge, unstable tech
- Heavy frameworks
- Server-dependent solutions
- Desktop-first tools
- Excessive dependencies

### Feature Implementation

#### For Every Feature:
1. **Design offline-first**: How does it work with no connectivity?
2. **Plan fallbacks**: What happens if enhancement fails?
3. **Consider constraints**: Memory, storage, battery, bandwidth
4. **Test on target devices**: Low-end Android, old iOS
5. **Document tradeoffs**: Why this approach vs alternatives

## Code Contribution Guidelines

### Before Writing Code

1. **Search existing code**: Understand patterns and conventions
2. **Check for similar features**: Reuse existing solutions
3. **Plan minimal changes**: Smallest change to achieve goal
4. **Consider test strategy**: How will you test this?

### While Writing Code

#### Structure
```
- Keep functions small (< 50 lines)
- Use clear, descriptive names
- Follow existing patterns
- Comment complex logic only
- Avoid premature optimization
```

#### Testing
```
- Write tests for business logic
- Test offline scenarios
- Test with network failures
- Test on low-spec devices
- Test sync conflicts
```

#### Error Handling
```javascript
// Always handle errors gracefully
try {
  await operation();
} catch (error) {
  logger.error('Operation failed', { error, context });
  showUserFriendlyMessage();
  fallbackToBasicOperation();
}
```

### After Writing Code

1. **Self-review**: Read your code as if you're reviewing someone else's
2. **Test offline**: Disable network and test thoroughly
3. **Check performance**: Profile on low-end device
4. **Update docs**: Document what you changed and why
5. **Write commit message**: Clear description of changes

## Common Patterns

### Local-First Data Pattern
```javascript
// Always read from local storage first
async function getData(id) {
  // 1. Get from local DB
  const local = await localDB.get(id);
  if (local) return local;
  
  // 2. Queue for sync if not local
  syncQueue.add({ action: 'fetch', id });
  
  // 3. Throw error (don't wait for network)
  throw new Error('Data not available locally');
}

// Save local first, sync later
async function saveData(data) {
  // 1. Save locally immediately
  await localDB.save(data);
  
  // 2. Update UI immediately
  updateUI(data);
  
  // 3. Queue for background sync
  syncQueue.add({ action: 'save', data });
}
```

### Edge Device Enhancement Pattern
```javascript
async function processData(data) {
  // Try enhanced path if available
  if (edgeDevice.isAvailable()) {
    try {
      return await edgeDevice.process(data);
    } catch (error) {
      logger.warn('Edge processing failed, using mobile fallback');
    }
  }
  
  // Fallback to mobile processing
  return await mobileProcessor.process(data);
}
```

### Graceful Degradation Pattern
```javascript
async function loadContent(id) {
  try {
    // Try optimized version
    return await loadOptimizedContent(id);
  } catch (error) {
    logger.warn('Optimized load failed, using basic version');
    try {
      return await loadBasicContent(id);
    } catch (error) {
      // Last resort
      return getCachedContent(id);
    }
  }
}
```

## Testing Checklist

### For Every Feature:
- [ ] Works with airplane mode enabled
- [ ] Handles network disconnection mid-operation
- [ ] Tested on Android 8 emulator with 2GB RAM
- [ ] No memory leaks in profiler
- [ ] Reasonable battery usage
- [ ] Storage usage acceptable
- [ ] UI remains responsive
- [ ] Error messages are user-friendly
- [ ] Falls back gracefully when enhancements fail
- [ ] Sync conflicts resolve correctly

## Common Pitfalls

### Don't:
1. ❌ Assume network is available
2. ❌ Block UI on network requests
3. ❌ Show technical error messages to users
4. ❌ Require edge device for core features
5. ❌ Store unencrypted sensitive data
6. ❌ Add dependencies without consideration
7. ❌ Over-engineer simple problems
8. ❌ Skip testing on low-end devices
9. ❌ Ignore battery/storage constraints
10. ❌ Break existing offline functionality

### Do:
1. ✅ Test offline first, then online
2. ✅ Provide immediate feedback (optimistic UI)
3. ✅ Handle all errors gracefully
4. ✅ Fall back to basic when enhanced fails
5. ✅ Encrypt sensitive data
6. ✅ Minimize dependencies
7. ✅ Keep solutions simple
8. ✅ Profile on target devices
9. ✅ Be resource-conscious
10. ✅ Maintain offline-first principle

## Questions to Ask

### Before Implementation:
- What happens if there's no internet?
- What happens if the edge device is unavailable?
- Will this work on a 3-year-old Android phone?
- Is there a simpler way to do this?
- What are the storage/memory/battery impacts?

### During Implementation:
- Am I following existing patterns?
- Have I handled all error cases?
- Is this code easy to understand?
- Did I test offline scenarios?
- Are there any hardcoded values that should be configurable?

### After Implementation:
- Does this work without network?
- Did I test on a low-spec device?
- Is the documentation updated?
- Are there any side effects?
- Could this be simplified?

## Getting Help

### When Stuck:
1. Search existing code for similar patterns
2. Review relevant ADRs and documentation
3. Check if there's an existing solution to reuse
4. Consider if you're over-complicating
5. Ask specific questions with context

### When Uncertain:
1. Default to simpler solution
2. Follow existing patterns
3. Prioritize offline functionality
4. Add comments explaining tradeoffs
5. Flag for human review if architectural

## Code Review Criteria

Your code will be evaluated on:
1. **Offline functionality**: Does it work offline?
2. **Simplicity**: Is it as simple as possible?
3. **Performance**: Does it work on low-end devices?
4. **Resilience**: Does it handle failures?
5. **Testing**: Are there adequate tests?
6. **Documentation**: Is it documented?
7. **Standards**: Does it follow coding principles?

## Success Metrics

You're successful when:
- Feature works 100% offline
- Runs smoothly on 2GB Android device
- Code is simple and maintainable
- Tests pass and cover key scenarios
- Documentation is updated
- Follows project principles
- Edge enhancement is optional, not required

## Related Documents

- [Coding Principles](coding-principles.md)
- [Product Vision](../product/vision.md)
- [Constraints](../product/constraints.md)
- [ADRs](../adr/)
