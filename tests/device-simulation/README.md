# Device Simulation Tests

## Overview

Tests that simulate real device conditions to validate app behavior on target hardware with realistic constraints.

## Purpose

Verify that the app works correctly on:
- Low-end devices (2GB RAM, Android 8+)
- Various network conditions
- Limited storage scenarios
- Battery constraints
- Different screen sizes

## Test Categories

### 1. Device Compatibility Tests
### 2. Network Condition Tests
### 3. Storage Constraint Tests
### 4. Performance Tests
### 5. Battery Impact Tests

## Test Environment

### Device Simulators
```
Low-End Android:
- Android 8.0 (API 26)
- 2GB RAM
- Quad-core 1.5GHz CPU
- 32GB storage (20GB free)
- 5" 720p screen

Mid-Range Android:
- Android 11 (API 30)
- 4GB RAM
- Octa-core 2.0GHz CPU
- 64GB storage
- 6" 1080p screen

iOS Baseline:
- iOS 13
- iPhone 8
- 2GB RAM
- 5.5" screen
```

## Test Structure

```
tests/device-simulation/
├── device-profiles/        # Device configuration profiles
├── network-profiles/       # Network condition profiles
├── test-scenarios/         # Test scenarios
│   ├── low-end-device/
│   ├── network-conditions/
│   ├── storage-constraints/
│   └── battery-impact/
└── tools/
    ├── emulator-config/
    └── performance-monitor/
```

## Device Compatibility Tests

### Test: Low-End Device Performance
```javascript
describe('Low-End Device', () => {
  beforeAll(async () => {
    await emulator.start({
      device: 'low-end-android',
      ram: '2GB',
      cpu: 'quad-core-1.5ghz',
      android: '8.0'
    });
  });

  it('should launch within 2 seconds', async () => {
    const startTime = Date.now();
    await app.launch();
    const launchTime = Date.now() - startTime;
    
    expect(launchTime).toBeLessThan(2000);
  });

  it('should load content within 1 second', async () => {
    await app.launch();
    
    const startTime = Date.now();
    await app.loadContent('lesson-1');
    const loadTime = Date.now() - startTime;
    
    expect(loadTime).toBeLessThan(1000);
  });

  it('should maintain < 150MB memory usage', async () => {
    await app.launch();
    await app.loadContent('lesson-1');
    await app.loadContent('lesson-2');
    
    const memoryUsage = await device.getMemoryUsage();
    expect(memoryUsage.peak).toBeLessThan(150 * 1024 * 1024);
  });

  it('should not crash under memory pressure', async () => {
    await app.launch();
    
    // Simulate memory pressure
    await device.simulateMemoryPressure('high');
    
    // App should still function
    await app.loadContent('lesson-1');
    const isRunning = await app.isRunning();
    
    expect(isRunning).toBe(true);
  });
});
```

## Network Condition Tests

### Test: Various Network Scenarios
```javascript
describe('Network Conditions', () => {
  const networkProfiles = [
    { name: 'Offline', speed: 0, latency: 0 },
    { name: '2G', speed: 50, latency: 500 },
    { name: '3G', speed: 750, latency: 100 },
    { name: '4G', speed: 5000, latency: 50 },
    { name: 'WiFi', speed: 20000, latency: 10 }
  ];

  networkProfiles.forEach(profile => {
    describe(profile.name, () => {
      beforeEach(async () => {
        await network.setProfile(profile);
      });

      it('should function without errors', async () => {
        await app.launch();
        await app.loadContent('lesson-1');
        
        const hasErrors = await app.getErrors();
        expect(hasErrors).toHaveLength(0);
      });

      if (profile.speed === 0) {
        it('should work completely offline', async () => {
          await app.launch();
          await app.loadContent('lesson-1');
          await app.takeQuiz('quiz-1');
          await app.viewProgress();
          
          // All operations should succeed
          const progress = await app.getProgress();
          expect(progress).toBeDefined();
        });
      }
    });
  });

  it('should handle network disconnection mid-operation', async () => {
    await network.setProfile({ name: 'WiFi' });
    await app.launch();
    
    // Start sync
    const syncPromise = app.sync();
    
    // Disconnect after 100ms
    setTimeout(() => network.setProfile({ name: 'Offline' }), 100);
    
    // Should handle gracefully
    await syncPromise;
    
    const hasErrors = await app.getErrors();
    expect(hasErrors).toHaveLength(0);
  });
});
```

## Storage Constraint Tests

### Test: Limited Storage Scenarios
```javascript
describe('Storage Constraints', () => {
  it('should handle low storage gracefully', async () => {
    await device.setAvailableStorage('100MB');
    await app.launch();
    
    // Try to download large content
    const result = await app.downloadContent('large-package');
    
    // Should fail gracefully
    expect(result.success).toBe(false);
    expect(result.reason).toBe('insufficient_storage');
    
    // Should show user-friendly message
    const message = await app.getLastMessage();
    expect(message).toContain('storage');
    expect(message).not.toContain('error');
  });

  it('should clean up when storage full', async () => {
    await device.setAvailableStorage('50MB');
    await app.launch();
    
    // Trigger cleanup
    await app.cleanupStorage();
    
    // Should free space
    const storageBefore = await device.getAvailableStorage();
    await app.cleanupStorage();
    const storageAfter = await device.getAvailableStorage();
    
    expect(storageAfter).toBeGreaterThan(storageBefore);
  });
});
```

## Performance Tests

### Test: Performance Under Load
```javascript
describe('Performance Under Load', () => {
  it('should maintain UI responsiveness', async () => {
    await device.setProfile('low-end-android');
    await app.launch();
    
    // Simulate heavy background work
    await app.startBackgroundSync();
    await app.startContentIndexing();
    
    // UI should still be responsive
    const startTime = Date.now();
    await app.navigateTo('lessons');
    const responseTime = Date.now() - startTime;
    
    expect(responseTime).toBeLessThan(100);
  });

  it('should handle rapid interactions', async () => {
    await app.launch();
    
    // Rapidly tap buttons
    for (let i = 0; i < 50; i++) {
      await app.tap('next-button');
    }
    
    // Should not crash or freeze
    const isResponsive = await app.isResponsive();
    expect(isResponsive).toBe(true);
  });
});
```

## Battery Impact Tests

### Test: Battery Consumption
```javascript
describe('Battery Impact', () => {
  it('should use < 10% battery per hour of active use', async () => {
    await device.setProfile('low-end-android');
    await device.startBatteryMonitoring();
    
    await app.launch();
    
    // Simulate 1 hour of use
    for (let i = 0; i < 60; i++) {
      await app.loadContent(`lesson-${i % 10}`);
      await sleep(60000); // Wait 1 minute
    }
    
    const batteryUsage = await device.getBatteryUsage();
    expect(batteryUsage.percentPerHour).toBeLessThan(10);
  });

  it('should minimize background battery drain', async () => {
    await device.startBatteryMonitoring();
    
    // App in background for 8 hours
    await app.launch();
    await app.background();
    await sleep(8 * 60 * 60 * 1000);
    
    const batteryUsage = await device.getBatteryUsage();
    expect(batteryUsage.backgroundDrain).toBeLessThan(5); // < 5% overnight
  });
});
```

## Running Tests

```bash
# Run all device simulation tests
npm run test:device

# Run on specific device profile
npm run test:device -- --device low-end-android

# Run with real device
npm run test:device -- --device real --serial ABC123

# Run network tests only
npm run test:device -- --suite network

# Generate performance report
npm run test:device -- --report performance.html
```

## Test Reports

### Performance Report
```
Device Simulation Test Report
=============================

Device: Low-End Android (2GB RAM, Android 8.0)

Performance Metrics:
- App Launch: 1.8s ✅ (target: < 2s)
- Content Load: 0.9s ✅ (target: < 1s)
- Memory Peak: 142MB ✅ (target: < 150MB)
- Battery Usage: 8.5%/hr ✅ (target: < 10%)

Network Conditions:
- Offline: ✅ All features work
- 2G: ✅ Graceful degradation
- 3G: ✅ Good performance
- 4G: ✅ Optimal performance

Storage:
- Low Storage: ✅ Handled gracefully
- Cleanup: ✅ Frees space effectively

Overall: PASS ✅
```

## Best Practices

### DO
- ✅ Test on real devices when possible
- ✅ Use realistic device profiles
- ✅ Test worst-case scenarios
- ✅ Monitor performance metrics
- ✅ Test over extended periods
- ✅ Simulate real user behavior

### DON'T
- ❌ Test only on powerful devices
- ❌ Ignore low-end devices
- ❌ Skip network condition testing
- ❌ Assume emulator == real device
- ❌ Ignore battery impact
- ❌ Skip long-running tests

## Related Documents

- [Constraints](../../docs/product/constraints.md)
- [Phone Architecture](../../docs/architecture/phone-architecture.md)
- [Reality Enforcement Agent](../../.github/agents/enforcement-agents/reality-enforcement-agent.md)
