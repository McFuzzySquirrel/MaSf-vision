# Unit Tests

## Overview

Unit tests for individual components, functions, and classes in the MaS codebase.

## Testing Principles

### 1. Test Behavior, Not Implementation
Focus on what the code does, not how it does it.

### 2. Offline-First Testing
All tests should pass with network disabled.

### 3. Fast Execution
Unit tests should be fast (< 100ms each).

### 4. Independent
Each test should be independent and isolated.

### 5. Readable
Tests should be clear and self-documenting.

## Test Structure

```
tests/unit/
├── mobile/              # Mobile app tests
│   ├── features/
│   ├── services/
│   └── utils/
├── edge/               # Edge device tests
│   ├── services/
│   └── utils/
├── models/             # ML model tests
│   ├── phone/
│   └── edge/
└── tools/              # Tool tests
    ├── content-pack/
    └── dataset/
```

## Test Organization

### By Feature
```
features/
├── content/
│   ├── content-loader.test.js
│   ├── content-viewer.test.js
│   └── content-storage.test.js
└── assessment/
    ├── quiz-engine.test.js
    └── scoring.test.js
```

### Test Naming
```javascript
// Good test names
describe('ContentLoader', () => {
  describe('loadContent', () => {
    it('should load content from local storage', () => {});
    it('should throw error when content not found', () => {});
    it('should cache loaded content', () => {});
  });
});
```

## Test Patterns

### Arrange-Act-Assert
```javascript
test('should calculate score correctly', () => {
  // Arrange
  const answers = [1, 2, 3];
  const correctAnswers = [1, 2, 4];
  
  // Act
  const score = calculateScore(answers, correctAnswers);
  
  // Assert
  expect(score).toBe(66.67);
});
```

### Test Doubles
```javascript
// Mock external dependencies
const mockStorage = {
  get: jest.fn(),
  set: jest.fn()
};

// Test with mock
test('should save to storage', async () => {
  const service = new ContentService(mockStorage);
  await service.save(content);
  
  expect(mockStorage.set).toHaveBeenCalledWith('content', content);
});
```

## Coverage Requirements

- Overall: 80%+ coverage
- Business logic: 90%+ coverage
- Utilities: 80%+ coverage
- UI components: 70%+ coverage

## Running Tests

```bash
# Run all unit tests
npm test

# Run specific test file
npm test content-loader.test.js

# Run with coverage
npm test --coverage

# Watch mode
npm test --watch
```

## Testing Offline Functionality

```javascript
describe('offline behavior', () => {
  beforeEach(() => {
    // Simulate offline
    mockNetwork.setOnline(false);
  });

  it('should load content from local cache', async () => {
    const content = await contentService.load('lesson-1');
    expect(content).toBeDefined();
    expect(networkService.fetch).not.toHaveBeenCalled();
  });

  it('should queue sync operations', async () => {
    await contentService.save(newContent);
    expect(syncQueue.add).toHaveBeenCalled();
  });
});
```

## Best Practices

### DO
- ✅ Test one thing per test
- ✅ Use descriptive test names
- ✅ Test edge cases
- ✅ Test error conditions
- ✅ Mock external dependencies
- ✅ Clean up after tests

### DON'T
- ❌ Test implementation details
- ❌ Make tests dependent on each other
- ❌ Use real network calls
- ❌ Use real database
- ❌ Share state between tests
- ❌ Write flaky tests

## Tools and Frameworks

### JavaScript/TypeScript
- Jest
- React Testing Library
- Enzyme (if needed)

### Python
- pytest
- unittest
- mock

### Native Mobile
- XCTest (iOS)
- JUnit (Android)

## Related Documents

- [Coding Principles](../../docs/development/coding-principles.md)
- [Testing Strategy](../../docs/testing/strategy.md) (to be created)
