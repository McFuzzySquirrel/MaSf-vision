# Coding Principles

## Overview

This document outlines the core coding principles and practices for the MaS project. All code should adhere to these principles.

## Core Principles

### 1. Offline-First
**Every feature must work offline.**
- Test all features with network disabled
- Never block UI on network requests
- Queue operations when offline
- Sync opportunistically

```javascript
// ❌ Bad: Blocks on network
async function loadContent(id) {
  return await api.fetchContent(id);
}

// ✅ Good: Local-first with sync
async function loadContent(id) {
  const local = await db.getContent(id);
  if (local) return local;
  
  // Queue for background sync if not local
  syncQueue.add({ type: 'content', id });
  throw new Error('Content not available locally');
}
```

### 2. Mobile-First
**Optimize for mobile devices, not desktop.**
- Target low-end Android devices (2GB RAM)
- Minimize memory usage
- Efficient battery consumption
- Touch-friendly UI (44px min touch targets)
- Responsive layouts

### 3. Progressive Enhancement
**Core features work on minimum specs, enhanced features on better devices.**
- Detect device capabilities
- Graceful degradation
- Don't require cutting-edge features
- Test on old devices

### 4. Keep It Simple
**Simplicity is a feature, not a constraint.**
- Prefer simple solutions
- Avoid over-engineering
- Clear, readable code
- Minimal dependencies
- Easy to understand and maintain

### 5. Resilience
**Handle failures gracefully.**
- Expect failures in all external systems
- Never lose user data
- Auto-recovery where possible
- Clear error messages
- Comprehensive logging

## Code Quality Standards

### Readability
- Self-documenting code
- Meaningful names
- Short functions (< 50 lines)
- Clear structure
- Consistent formatting

### Testing
- Unit tests for business logic
- Integration tests for workflows
- Offline scenario testing
- Device simulation tests
- Minimum 80% coverage

### Performance
- Fast app launch (< 2 sec)
- Responsive UI (< 100ms)
- Efficient storage
- Minimal battery impact
- Progressive loading

## Architecture Patterns

### Local-First Data
```
User Action
    ↓
Update Local State (Immediate)
    ↓
Queue for Sync (Background)
    ↓
Sync When Possible (Eventual)
```

### Feature Detection
```javascript
if (edgeDevice.available()) {
  // Enhanced path
  return await edgeDevice.inferModel(data);
} else {
  // Fallback path
  return await mobileModel.infer(data);
}
```

### Optimistic UI
```javascript
// Show result immediately
ui.showResult(optimisticResult);

// Sync in background
syncQueue.add(operation).catch(err => {
  // Rollback if sync fails
  ui.revertResult();
  ui.showError(err);
});
```

## Security Principles

### Data Protection
- Encrypt sensitive data at rest
- Secure communication (HTTPS only)
- Minimize data collection
- User consent for data usage
- Regular security audits

### Privacy
- Local-first data storage
- Minimal server communication
- Anonymized analytics
- COPPA/GDPR compliance
- Clear privacy policy

## Error Handling

### User-Facing Errors
```javascript
try {
  await performAction();
} catch (error) {
  // User-friendly message
  showError('Could not complete action. Please try again.');
  
  // Technical details in logs
  logger.error('Action failed', { error, context });
}
```

### Graceful Degradation
```javascript
try {
  return await enhancedFeature();
} catch (error) {
  logger.warn('Enhanced feature failed, using fallback', error);
  return basicFeature();
}
```

## Code Organization

### Project Structure
```
src/
  ├── features/          # Feature modules
  │   ├── content/
  │   ├── assessment/
  │   └── progress/
  ├── shared/           # Shared utilities
  │   ├── db/
  │   ├── sync/
  │   └── ui/
  ├── services/         # External services
  └── config/           # Configuration
```

### Module Boundaries
- Clear interfaces between modules
- Minimize coupling
- Dependency injection
- No circular dependencies

## Version Control

### Commit Messages
```
type(scope): Short description

Longer explanation if needed

Fixes #123
```

Types: feat, fix, docs, style, refactor, test, chore

### Pull Requests
- Small, focused changes
- Self-reviewing before submission
- Tests included
- Documentation updated
- CI passes

## Dependencies

### Adding Dependencies
1. Evaluate necessity
2. Check license compatibility
3. Check bundle size impact
4. Check offline compatibility
5. Document reason

### Criteria for Acceptance
- Actively maintained
- Good security record
- Reasonable size
- Compatible with offline-first
- Clear license (prefer MIT/Apache)

## Documentation

### Code Documentation
- Public APIs documented
- Complex logic explained
- Examples for common usage
- Architecture decisions recorded (ADRs)

### README Files
- Setup instructions
- Running tests
- Common tasks
- Architecture overview

## Mobile-Specific Guidelines

### Android
- Support API 26+ (Android 8.0+)
- Test on low-end devices
- Handle configuration changes
- Proper lifecycle management
- Background service limits

### iOS
- Support iOS 13+
- Respect memory constraints
- Handle app state transitions
- Background task limits
- App Store guidelines

## Performance Guidelines

### App Size
- Target APK < 50MB
- Minimize dependencies
- Code splitting where possible
- Asset optimization

### Memory
- Profile memory usage
- Avoid memory leaks
- Release resources promptly
- Cache management strategy

### Storage
- Efficient data structures
- Compress where appropriate
- Cleanup old data
- User control over storage

## Accessibility

### Requirements
- Screen reader support
- Sufficient color contrast (WCAG AA)
- Keyboard navigation
- Adjustable text size
- Alternative text for images

## Internationalization

### Guidelines
- Externalize all strings
- Support RTL languages
- Cultural sensitivity
- Date/time localization
- Number formatting

## Review Checklist

Before submitting code:
- [ ] Works offline
- [ ] Tested on low-end device
- [ ] No hardcoded strings
- [ ] Error handling in place
- [ ] Tests written and passing
- [ ] Documentation updated
- [ ] Accessibility considered
- [ ] Security reviewed
- [ ] Performance acceptable
- [ ] No new warnings

## Related Documents

- [AI Agent Instructions](ai-agent-instructions.md)
- [ADR-001: Phone-First Architecture](../adr/ADR-001-phone-first-architecture.md)
- [ADR-002: Offline-First Design](../adr/ADR-002-offline-first-design.md)
