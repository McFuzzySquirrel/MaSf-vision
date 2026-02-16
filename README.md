# MaS - Mobile Adaptive System

## Project Overview

MaS is a phone-first, offline-capable learning platform designed to work in resource-constrained environments. The system prioritizes mobile devices as the primary computing platform, with optional edge devices serving as accelerators.

## Architecture

This project follows a **phone-first architecture** where:
- The mobile app is the primary interface and computing platform
- All core functionality works offline
- Edge devices are optional accelerators, not dependencies
- Data synchronization happens opportunistically

## Repository Structure

```
├── docs/                    # Documentation
│   ├── architecture/        # System architecture documentation
│   ├── product/            # Product vision and requirements
│   ├── adr/                # Architecture Decision Records
│   └── development/        # Development guidelines
│
├── .github/                # GitHub-specific configuration
│   ├── agents/             # AI agent instructions and configurations
│   └── workflows/          # CI/CD workflows
│
├── apps/                   # Application code
│   ├── learner-mobile/     # Mobile application for learners
│   └── school-edge-node/   # Edge device application
│
├── models/                 # ML models
│   ├── phone-models/       # Models optimized for mobile devices
│   └── edge-models/        # Models for edge acceleration
│
├── tools/                  # Development and content tools
│   ├── content-pack-builder/  # Tools for creating content packages
│   └── dataset-tools/         # Dataset preparation and management
│
└── tests/                  # Test suites
    ├── unit/              # Unit tests
    ├── integration/       # Integration tests
    └── device-simulation/ # Device simulation tests
```

## Getting Started

See [Development Guide](docs/development/coding-principles.md) for setup instructions.

## Documentation

- [System Overview](docs/architecture/system-overview.md)
- [Product Vision](docs/product/vision.md)
- [Architecture Decision Records](docs/adr/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Agent Communication Protocol (ACP)

This project uses the Agent Communication Protocol for AI-assisted development. See [.github/agents/communication-protocol.md](.github/agents/communication-protocol.md) for details.

## PR Merge Constitution (PMC)

All pull requests are evaluated against the PR Merge Constitution. See [.github/agents/pr-merge-constitution.yaml](.github/agents/pr-merge-constitution.yaml) for the criteria.
