# Integration Tests

## Overview

Integration tests verify that different components work together correctly.

## Testing Scope

### Component Integration
- UI + Business Logic
- Business Logic + Data Layer
- Service + Service communication

### System Integration
- Mobile App + Local Database
- Mobile App + Edge Device
- Edge Device + Cloud Services

### End-to-End Workflows
- Complete user journeys
- Multi-step processes
- Cross-component flows

## Test Structure

```
tests/integration/
├── mobile/
│   ├── content-workflow.test.js
│   ├── assessment-workflow.test.js
│   └── sync-workflow.test.js
├── edge/
│   ├── content-distribution.test.js
│   ├── model-inference.test.js
│   └── sync-coordination.test.js
└── end-to-end/
    ├── offline-learning.test.js
    ├── online-sync.test.js
    └── edge-acceleration.test.js
```

## Test Scenarios

### Scenario 1: Offline Content Viewing
```javascript
describe('Offline Content Viewing', () => {
  it('should complete full content viewing workflow offline', async () => {
    // Setup: Load content package
    await setupContentPackage('math-grade5');
    
    // Enable offline mode
    network.goOffline();
    
    // User opens app
    await app.launch();
    
    // Navigate to lesson
    await app.navigateTo('lessons');
    await app.selectLesson('fractions');
    
    // View lesson content
    const content = await app.getCurrentContent();
    expect(content).toBeDefined();
    expect(content.title).toBe('Introduction to Fractions');
    
    // Complete lesson
    await app.markComplete();
    
    // Verify progress saved locally
    const progress = await db.getProgress('fractions');
    expect(progress.completed).toBe(true);
    
    // Verify sync queued
    const syncQueue = await db.getSyncQueue();
    expect(syncQueue).toContainEqual({
      type: 'progress',
      lessonId: 'fractions'
    });
  });
});
```

### Scenario 2: Assessment Taking
```javascript
describe('Assessment Workflow', () => {
  it('should complete assessment offline with local scoring', async () => {
    network.goOffline();
    
    // Start quiz
    await app.navigateTo('assessments');
    await app.startQuiz('fractions-quiz');
    
    // Answer questions
    await app.answerQuestion(0, 1);
    await app.answerQuestion(1, 2);
    await app.nextQuestion();
    
    // Submit quiz
    await app.submitQuiz();
    
    // Verify immediate results
    const results = await app.getQuizResults();
    expect(results.score).toBeDefined();
    expect(results.feedback).toBeDefined();
    
    // Verify data saved
    const savedResults = await db.getQuizResults('fractions-quiz');
    expect(savedResults).toEqual(results);
  });
});
```

### Scenario 3: Edge Device Integration
```javascript
describe('Edge Device Integration', () => {
  it('should use edge device when available, fallback when not', async () => {
    // With edge device
    edgeDevice.start();
    
    const result1 = await mlService.infer(data);
    expect(result1.source).toBe('edge');
    expect(result1.accuracy).toBeGreaterThan(0.9);
    
    // Edge device goes offline
    edgeDevice.stop();
    
    const result2 = await mlService.infer(data);
    expect(result2.source).toBe('mobile');
    expect(result2.accuracy).toBeGreaterThan(0.7);
    
    // User experience unaffected
    expect(result1.format).toEqual(result2.format);
  });
});
```

### Scenario 4: Sync Workflow
```javascript
describe('Sync Workflow', () => {
  it('should sync progress when connectivity restored', async () => {
    // Work offline
    network.goOffline();
    
    await app.completeLesson('lesson-1');
    await app.completeLesson('lesson-2');
    await app.takeQuiz('quiz-1');
    
    // Verify queued for sync
    let queue = await syncQueue.getAll();
    expect(queue).toHaveLength(3);
    
    // Go online
    network.goOnline();
    
    // Trigger sync
    await syncService.sync();
    
    // Wait for completion
    await waitFor(() => syncQueue.getAll()).toHaveLength(0);
    
    // Verify server has data
    const serverProgress = await server.getProgress(userId);
    expect(serverProgress.completedLessons).toContain('lesson-1');
    expect(serverProgress.completedLessons).toContain('lesson-2');
  });
});
```

## Test Environment

### Setup
```javascript
beforeEach(async () => {
  // Clean database
  await db.clear();
  
  // Reset network state
  network.reset();
  
  // Load test data
  await loadTestData();
  
  // Initialize app
  await app.initialize();
});

afterEach(async () => {
  // Cleanup
  await app.shutdown();
  await db.close();
  await network.restore();
});
```

### Test Data
```javascript
const testData = {
  contentPackages: [
    {
      id: 'math-grade5',
      lessons: [...],
      assessments: [...]
    }
  ],
  users: [
    {
      id: 'test-user-1',
      profile: {...}
    }
  ]
};
```

## Running Tests

```bash
# Run all integration tests
npm run test:integration

# Run specific test suite
npm run test:integration -- content-workflow

# Run with real database
npm run test:integration -- --use-real-db

# Run with edge device simulator
npm run test:integration -- --with-edge
```

## Performance Testing

```javascript
describe('Performance', () => {
  it('should load content within 1 second', async () => {
    const startTime = Date.now();
    
    await app.loadContent('lesson-1');
    
    const duration = Date.now() - startTime;
    expect(duration).toBeLessThan(1000);
  });

  it('should handle 100 concurrent users', async () => {
    const users = Array(100).fill(null).map((_, i) => 
      createUser(`user-${i}`)
    );
    
    const results = await Promise.all(
      users.map(user => user.loadContent('lesson-1'))
    );
    
    expect(results.every(r => r.success)).toBe(true);
  });
});
```

## Best Practices

### DO
- ✅ Test realistic workflows
- ✅ Test offline scenarios
- ✅ Test error conditions
- ✅ Test integration points
- ✅ Use realistic test data
- ✅ Clean up between tests

### DON'T
- ❌ Test internal implementation
- ❌ Mock everything
- ❌ Make tests too brittle
- ❌ Ignore timing issues
- ❌ Skip error scenarios
- ❌ Leave test data behind

## Related Documents

- [Coding Principles](../../docs/development/coding-principles.md)
- [Testing Strategy](../../docs/testing/strategy.md) (to be created)
- [System Overview](../../docs/architecture/system-overview.md)
