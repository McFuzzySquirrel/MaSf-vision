# Quick Start Guide - MaS Framework

## What is MaS?

**MaS (Multi-Agent System) Framework** enables you to transform ANY project vision into a fully autonomous multi-agent system that can self-organize and execute to realize that vision.

## 30-Second Overview

```
Your Vision Document → Master Agent → Constitution + Agents + Protocols → Autonomous Execution
```

The Master Agent reads your vision, generates everything needed, and enables autonomous agent teams to build your project.

## Quick Start (5 minutes)

### 1. Write Your Vision (2 minutes)

Create `docs/product/vision.md`:

```markdown
# My Project Vision

## Mission
[Why does this exist? What problem does it solve?]

## Core Principles
1. Principle one (e.g., "User-first: Every decision prioritizes users")
2. Principle two (e.g., "Simple: Easy to use without training")
3. Principle three (e.g., "Reliable: Works 99%+ of time")

## Goals
### Short Term (6 months)
- Goal 1
- Goal 2

### Long Term (2 years)
- Goal 1
- Goal 2

## Success Criteria
- How will you measure success?
- What are the key metrics?
```

### 2. Run Master Agent (1 minute)

```bash
python tools/agent-orchestration/master-agent.py --action bootstrap
```

**Master Agent will:**
- ✅ Read and understand your vision
- ✅ Generate a project constitution (laws, rules, quality gates)
- ✅ Identify required specialized agents
- ✅ Create communication protocols
- ✅ Bootstrap the entire multi-agent system

**Output:** `.mas-system/` directory with all artifacts

### 3. Generate Agent Definitions (1 minute)

```bash
python tools/agent-orchestration/agent-definition-generator.py
```

**Generator will:**
- ✅ Read agent specifications
- ✅ Create formatted markdown files
- ✅ Place in `.github/agents/` directory

**Output:** Agent definition files for all identified agents

### 4. Start Autonomous Execution (1 minute)

```bash
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous
```

**System will:**
- ✅ Generate sprint plan from vision
- ✅ Extract and assign tasks
- ✅ Coordinate agent execution
- ✅ Track progress automatically

## What You Get

After running these commands, you have:

### ✅ Constitution (`.mas-system/constitution.yaml`)
- Core laws derived from your principles
- Decision-making framework
- Quality gates
- Enforcement rules
- Escalation paths

### ✅ Agent Team (`.github/agents/`)
- Coordination agents (planning, task dispatch)
- Development agents (implementation, testing, docs)
- Enforcement agents (quality, security, compliance)
- Domain-specific agents (based on your vision)

### ✅ Communication Protocol (`.mas-system/communication-protocol.yaml`)
- Message formats
- Coordination patterns
- Workflows
- State management
- Conflict resolution

### ✅ Execution Plan (`.mas-system/bootstrap-summary.md`)
- System overview
- Agent list with roles
- Next steps

## Real Example

### Input: Education Platform Vision

```markdown
# Education Platform Vision

## Mission
Democratize quality education through offline-capable learning

## Core Principles
1. Offline-First: Works without internet
2. Phone-First: Mobile is primary platform
3. Simple: Easy to use without training
```

### Output: Generated System

**Constitution:**
- 3 core principles (Offline-First, Phone-First, Simple)
- 4 quality gates (Code Quality, Accessibility, Security, Vision Alignment)
- Clear decision framework

**9 Agents Created:**
- Master Coordination Agent
- Task Dispatcher Agent
- Implementation Agent
- Mobile Development Agent
- Quality Assurance Agent
- Documentation Agent
- Constitutional Judge Agent
- Security Enforcement Agent
- Quality Enforcement Agent

**All in 3 commands, < 5 minutes**

## Use Cases

The framework works for ANY project:

### Software Development
- Web applications
- Mobile apps
- APIs and microservices
- Infrastructure/DevOps

### Research
- Data analysis projects
- ML experiments
- Scientific research

### Content Creation
- Documentation projects
- Training materials
- Publishing workflows

### Business
- Process automation
- Workflow optimization
- Operations management

## Next Steps

### Review Generated Artifacts
```bash
# Check constitution
cat .mas-system/constitution.yaml

# View agents
ls .github/agents/mutagen-agents/
ls .github/agents/enforcement-agents/

# Read summary
cat .mas-system/bootstrap-summary.md
```

### Customize (Optional)
```bash
# Edit constitution
nano .mas-system/constitution.yaml

# Modify agents
nano .github/agents/mutagen-agents/master-coordinator.md

# Adjust workflows
nano .github/workflows/autonomous-agent-execution.yml
```

### Monitor Execution
```bash
# Check sprint plan
cat tools/agent-orchestration/current-sprint.yaml

# View agent activity
gh issue list --label "autonomous-agent"

# Check workflow status
gh run list --workflow=autonomous-agent-execution.yml
```

## Key Commands Reference

| Command | Purpose | Output |
|---------|---------|--------|
| `master-agent.py --action bootstrap` | Create entire system | `.mas-system/` artifacts |
| `master-agent.py --action interpret` | Just analyze vision | Vision analysis |
| `master-agent.py --action constitution` | Generate constitution only | Constitution YAML |
| `master-agent.py --action agents` | Identify agents only | Agent specs |
| `agent-definition-generator.py` | Create agent files | `.md` files in `.github/agents/` |
| `vision-task-extractor.py` | Generate sprint plan | `current-sprint.yaml` |
| `agent-creator.py --action suggest` | Propose new agents | Agent suggestions |

## Help & Documentation

- **Framework Guide**: [FRAMEWORK-GUIDE.md](FRAMEWORK-GUIDE.md) - Comprehensive guide
- **Implementation Details**: [IMPLEMENTATION-SUMMARY.md](IMPLEMENTATION-SUMMARY.md) - Technical summary
- **Tool Documentation**: [tools/agent-orchestration/README.md](tools/agent-orchestration/README.md) - Tool details
- **Agent Protocol**: [.github/agents/communication-protocol.md](.github/agents/communication-protocol.md) - Communication

## Troubleshooting

### Vision not parsed correctly?
→ Make vision more structured with clear headings

### Wrong agents generated?
→ Add more specific details in vision about technologies/approaches

### Constitution too strict/loose?
→ Edit `.mas-system/constitution.yaml` manually and re-run

### Need help?
→ Check [FRAMEWORK-GUIDE.md](FRAMEWORK-GUIDE.md) for detailed guidance

## That's It!

You now have a complete multi-agent system customized to your project vision.

The agents will:
- ✅ Self-organize into teams
- ✅ Plan sprints from your vision
- ✅ Extract and execute tasks
- ✅ Coordinate autonomously
- ✅ Generate ADRs for decisions
- ✅ Track and report progress

**Just provide the vision, Master Agent handles the rest!**

---

**Framework Status:** ✅ Production Ready
**Time to Bootstrap:** < 5 minutes
**Lines of Vision:** As few as you need
**Complexity:** Automatic
