# Constraints

## Overview

This document outlines the key constraints that shape the MaS product design and implementation decisions.

## Technical Constraints

### Device Limitations
- **Minimum Specification**: Android 8.0+ with 2GB RAM
- **Storage**: Limited to 32-64GB total device storage
- **Processing Power**: Low-end mobile processors
- **Screen Size**: 4.5" to 6.5" displays
- **Battery**: Must be power efficient, long battery life

### Network Constraints
- **Connectivity**: Assume no reliable internet access
- **Bandwidth**: When available, may be 2G speeds (< 100 kbps)
- **Latency**: High latency (> 500ms) when connected
- **Cost**: Data costs may be prohibitive
- **Availability**: Internet may be available only periodically

### Infrastructure Constraints
- **No Servers**: Cannot assume local server infrastructure
- **No IT Support**: Teachers must self-support
- **Power**: Unreliable electricity
- **Environment**: Extreme temperatures, dust, humidity

## Resource Constraints

### Financial
- **Low Budget**: Target cost per learner < $50/year
- **Free-Tier**: Core functionality must be free
- **Minimal Hardware**: No special equipment required
- **Open Source**: Prefer open source to reduce licensing costs

### Human Resources
- **Teacher Training**: Minimal training time available
- **Technical Skills**: Cannot assume technical expertise
- **Support**: Limited or no technical support available
- **Content Creation**: Limited professional content development

### Content
- **Bandwidth**: Content must be distributable offline
- **Size**: Total content packages should be < 2GB per subject
- **Format**: Must work on mobile screens
- **Localization**: Need multi-language support
- **Quality**: Balance quality with file size

## Operational Constraints

### Deployment
- **Remote Installation**: Cannot physically access devices
- **Scale**: Must support 1 to 10,000+ devices
- **Updates**: Over-the-air updates may not be available
- **Security**: Limited ability to enforce security policies

### Maintenance
- **Self-Service**: Teachers must handle basic issues
- **Diagnostics**: Limited ability to diagnose problems remotely
- **Recovery**: Must survive and recover from crashes/failures
- **Backup**: Data backup may not be possible

## Regulatory Constraints

### Privacy
- **Student Data**: Must comply with child privacy regulations
- **Data Storage**: Minimize personal data collection
- **Consent**: Obtain appropriate consent
- **Transparency**: Clear data usage policies

### Accessibility
- **Inclusive Design**: Must be accessible to learners with disabilities
- **Language**: Support multiple languages and scripts
- **Cultural Sensitivity**: Content must be culturally appropriate

### Education Standards
- **Curriculum Alignment**: Must align with local curricula
- **Assessment**: Valid and reliable assessment methods
- **Certification**: May need official recognition

## Design Implications

### Must Haves
1. **Offline-First**: All core features work offline
2. **Mobile-First**: Optimized for mobile screens and touch
3. **Lightweight**: Small app size and content packages
4. **Resilient**: Handles failures gracefully
5. **Simple**: Minimal learning curve

### Must Not Haves
1. **No Required Connectivity**: Cannot depend on internet
2. **No Required Infrastructure**: Cannot need servers/edge devices
3. **No Complex Setup**: Cannot require IT expertise
4. **No Large Downloads**: Cannot assume high bandwidth
5. **No Expensive Devices**: Cannot require flagship phones

## Trade-offs

### Quality vs. Size
- Accept some quality reduction to minimize file sizes
- Use efficient codecs and compression
- Prioritize essential content

### Features vs. Simplicity
- Limit features to essential functionality
- Avoid feature creep
- Progressive disclosure of advanced features

### Performance vs. Compatibility
- Support older devices even if slower
- Graceful degradation on low-end devices
- Optimize for common case (low-spec devices)

## Future Relaxation

As infrastructure improves in target regions:
- Connectivity constraints may ease
- Device specifications will improve
- Bandwidth availability will increase

The system should take advantage of improvements while maintaining baseline functionality.

## Related Documents

- [Vision](vision.md)
- [Success Metrics](success-metrics.md)
- [System Overview](../architecture/system-overview.md)
