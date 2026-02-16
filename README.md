## About These Projects

All of my projects exist for one main reason: **learning through experimentation**.  
Each repository is a result of me asking questions like:  
> “Is this possible?”  
> “I wonder if…?”  

Sometimes they’re attempts to solve real problems I’ve come across, other times they’re just me following curiosity down a rabbit hole.  
This is my **learning playground**, a space where I test ideas, try new things, and learn by doing.  

I share them here in case they help or inspire someone else.  
So expect some projects to be **messy**, others **well-structured**, all of them are honest reflections of learning in progress.  

Feel free to **use**, **modify**, or **build on** anything here. 

So here we go:

# MaSf-vision (Multi-Agent System Framework Based on Vision)

## Project Overview

**MaSf-vision** (Multi-Agent System Framework based on vision) is a **general-purpose multi-agent system framework** that enables autonomous AI agents to understand any vision, self-organize, and execute collaboratively to realize that vision.

## 🚨 Common Issues & Quick Fixes

### Getting "Workflow Not Found" Error?

If you're trying to use MaSf-vision in your repository (like eZansiEdgeAI) and getting:
```
HTTP 404: Not Found (https://api.github.com/repos/.../workflows/autonomous-agent-execution.yml)
```

**→ See [SOLUTION.md](SOLUTION.md) for the complete solution!**

**TL;DR**: You need to bootstrap the framework into your repository first, and push to the **main branch**:
```bash
python /path/to/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo /path/to/your/repo
git checkout main && git push origin main
```

### Getting "Deprecated artifact v3" Error?

If your workflow fails with:
```
This request has been automatically failed because it uses a deprecated version of `actions/upload-artifact: v3`
```

**→ See [ARTIFACT-V3-FIX.md](ARTIFACT-V3-FIX.md) for the fix!**

**Quick fix**: Update your workflow file to use `@v4` instead of `@v3` for upload-artifact and download-artifact actions.

### Core Capability

The **Master Agent** can:
1. **Read and interpret any project vision** - Understanding mission, principles, and goals
2. **Generate a project constitution** - Deriving core laws and decision frameworks
3. **Create specialized agents** - Identifying and instantiating needed agent types
4. **Establish communication protocols** - Defining how agents coordinate
5. **Bootstrap autonomous execution** - Enabling agents to self-organize and execute

### Example Use Case: Education Platform

The current example demonstrates the framework applied to a phone-first, offline-capable learning platform designed to work in resource-constrained environments. The system prioritizes mobile devices as the primary computing platform, with optional edge devices serving as accelerators.

**This is just one example** - the framework can adapt to any domain or vision.

## Framework Architecture

### Multi-Agent System Components

```
Vision Document → Master Agent → Constitution + Agents + Protocols → Autonomous Execution
```

1. **Master Agent** (`tools/agent-orchestration/master-agent.py`)
   - Interprets project vision
   - Generates constitution from principles
   - Identifies required agent specializations
   - Creates communication protocols

2. **Agent System** (`.mas-system/`)
   - Constitution: Core laws and decision framework
   - Agent Specifications: Required agent types and roles
   - Communication Protocol: Coordination patterns and workflows
   - State Management: Shared context and progress tracking

3. **Autonomous Execution** (`.github/workflows/`)
   - Sprint planning from vision
   - Task extraction and assignment
   - ADR auto-generation
   - Progress tracking and coordination

### Example: Education Platform Architecture

When applied to the education use case, the system follows a **phone-first architecture** where:
- The mobile app is the primary interface and computing platform
- All core functionality works offline
- Edge devices are optional accelerators, not dependencies
- Data synchronization happens opportunistically

## Repository Structure

```
├── .mas-system/             # Generated multi-agent system artifacts
│   ├── constitution.yaml    # Project constitution and laws
│   ├── agent-specifications.yaml  # Required agent definitions
│   ├── communication-protocol.yaml  # Coordination protocols
│   └── vision-analysis.yaml # Parsed vision understanding
│
├── tools/                   # Multi-agent system tools
│   └── agent-orchestration/ # Agent coordination and bootstrap
│       ├── master-agent.py  # Master agent (vision interpreter)
│       ├── vision-task-extractor.py  # Task extraction
│       ├── agent-creator.py # Dynamic agent creation
│       └── README.md        # Orchestration guide
│
├── .github/                 # GitHub-specific configuration
│   ├── agents/              # Agent definitions and protocols
│   │   ├── mutagen-agents/  # Development/coordination agents
│   │   ├── enforcement-agents/  # Quality/security agents
│   │   └── communication-protocol.md
│   └── workflows/           # Autonomous execution workflows
│       ├── autonomous-agent-execution.yml
│       ├── adr-generation.yml
│       └── pr-evaluation.yml
│
├── docs/                    # Project documentation
│   ├── product/             # Vision and requirements (example)
│   ├── adr/                 # Architecture Decision Records
│   ├── architecture/        # System architecture
│   └── development/         # Development guidelines
│
├── apps/                    # Application code (example use case)
│   ├── learner-mobile/      # Mobile application
│   └── school-edge-node/    # Edge device application with API Gateway
│       ├── api_server.py    # REST API for mobile-edge communication
│       ├── API.md           # API documentation
│       └── requirements.txt # Python dependencies
│
├── models/                  # ML models (example use case)
├── tests/                   # Test suites
└── README.md               # This file
```

## Getting Started

### For New Users: Adopting MaSf-vision in Your Repository

If you want to use the MaSf-vision framework in your own repository:

1. **See the [Setup Guide for Autonomous Agents](SETUP-AUTONOMOUS-AGENTS.md)** - Complete instructions on which files to copy and how to set up the system
2. **Or use the bootstrap tool**:
   ```bash
   python /path/to/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo /path/to/your/repo
   ```

### Bootstrap a New Multi-Agent System

1. **Create your vision document** in `docs/product/vision.md`
2. **Run the master agent** to interpret vision and generate system:
   ```bash
   python tools/agent-orchestration/master-agent.py --action bootstrap
   ```
3. **Review generated artifacts** in `.mas-system/`:
   - Constitution and core laws
   - Required agent specifications
   - Communication protocols
4. **Initialize autonomous execution**:
   ```bash
   gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous
   ```

### Apply to Education Platform Example

See [Development Guide](docs/development/coding-principles.md) for the education platform setup.

### Run the Edge Node API (Optional)

If you want to test the school edge node API Gateway:

```bash
# Navigate to the edge node directory
cd apps/school-edge-node

# Install dependencies
pip install -r requirements.txt

# Start the API server
python api_server.py
```

The API will be available at http://localhost:8000 with:
- Interactive docs: http://localhost:8000/docs
- Discovery endpoint: http://localhost:8000/api/v1/discover
- Health check: http://localhost:8000/health

See [Edge Node API Documentation](apps/school-edge-node/API.md) for details.

## Documentation

### Framework Documentation
- [Setup Guide for Autonomous Agents](SETUP-AUTONOMOUS-AGENTS.md) - Complete setup instructions
- [Master Agent Guide](tools/agent-orchestration/README.md)
- [Agent Communication Protocol](.github/agents/communication-protocol.md)
- [Autonomous Sprint Driver](.github/agents/mutagen-agents/autonomous-sprint-driver.md)

### Example Use Case: Education Platform
- [System Overview](docs/architecture/system-overview.md)
- [Product Vision](docs/product/vision.md)
- [Architecture Decision Records](docs/adr/)

## Framework Features

### 1. Vision Interpretation
The Master Agent analyzes any vision document to extract:
- Mission and purpose
- Core principles and values
- Short and long-term goals
- Constraints and requirements
- Success criteria
- Domain/industry context

### 2. Constitution Generation
Automatically generates a project constitution including:
- Core laws (inviolable principles)
- Decision-making framework
- Quality gates and review criteria
- Enforcement rules
- Escalation paths

### 3. Dynamic Agent Creation
Identifies and creates specialized agents based on needs:
- **Coordination Agents**: Sprint planning, task dispatch
- **Development Agents**: Implementation, testing, documentation
- **Enforcement Agents**: Quality, security, constitutional compliance
- **Domain-Specific Agents**: Tailored to project domain

### 4. Communication Protocols
Generates coordination protocols including:
- Standard message formats
- Coordination patterns (parallel, sequential, etc.)
- Workflow definitions
- State management strategies
- Conflict resolution procedures

### 5. Autonomous Execution
Enables agents to:
- Self-organize into teams
- Extract and assign tasks from vision
- Execute sprints autonomously
- Generate ADRs for decisions
- Track and report progress

## Use Cases

The framework can be applied to any domain:

- **Software Development**: Web apps, mobile apps, APIs
- **Research Projects**: Data analysis, ML experiments
- **Infrastructure**: DevOps, cloud architecture
- **Content Creation**: Documentation, training materials
- **Business Operations**: Process automation, workflows

**Current Example**: Education platform (offline-capable mobile learning)

## CLI Bootstrap Tool

The MaSf-vision framework now includes a CLI bootstrap tool that makes it easy to adopt the framework for your own projects.

### Quick Start

```bash
# Bootstrap the framework into your repository
python tools/agent-orchestration/bootstrap.py

# Or bootstrap into a specific directory
python tools/agent-orchestration/bootstrap.py --target-repo /path/to/your/repo
```

The bootstrap tool will:
1. Set up the necessary directory structure
2. Copy framework tools and workflows
3. Generate a PR constitution from your vision
4. Create sample documentation if needed

### What You Get

- **Vision-aware PR validation**: Automatically validates PRs against YOUR project's principles
- **Dynamic constitution generation**: PR rules derived from your vision, not hardcoded
- **Automated workflows**: GitHub Actions that enforce your constitution
- **Customizable**: Easy to adjust and extend for your specific needs

See [Bootstrap Tool Documentation](tools/agent-orchestration/bootstrap.py) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                      Vision Document                         │
│  (Describes what needs to be built and why)                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                      Master Agent                            │
│  - Interprets vision                                         │
│  - Generates constitution                                    │
│  - Creates specialized agents                                │
│  - Establishes protocols                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   Multi-Agent System                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Coordination │  │ Development  │  │ Enforcement  │      │
│  │   Agents     │  │   Agents     │  │   Agents     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Autonomous Execution                            │
│  - Sprint planning                                           │
│  - Task assignment and execution                             │
│  - ADR generation                                            │
│  - Progress tracking                                         │
│  - Self-organization                                         │
└─────────────────────────────────────────────────────────────┘
```

## Agent Communication Protocol (ACP)

This project uses the Agent Communication Protocol for AI-assisted development. See [.github/agents/communication-protocol.md](.github/agents/communication-protocol.md) for details.

## PR Merge Constitution (PMC)

All pull requests are evaluated against the PR Merge Constitution. See [.github/agents/pr-merge-constitution.yaml](.github/agents/pr-merge-constitution.yaml) for the criteria.
