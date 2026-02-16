# MaSf-vision Framework - User Guide

## Overview

The **MaSf-vision** (Multi-Agent System Framework based on vision) enables you to transform **any project vision** into a fully autonomous multi-agent system that can self-organize and execute to realize that vision.

## How It Works

### The Big Picture

1. **You provide**: A vision document describing what you want to build
2. **Master Agent interprets**: Understands mission, principles, goals, constraints
3. **System generates**: Constitution, specialized agents, communication protocols
4. **Agents execute**: Self-organize, plan, coordinate, and build autonomously

### Key Insight

Instead of manually:
- Defining agent roles
- Creating communication protocols
- Setting up coordination mechanisms
- Writing constitutions and rules

The **Master Agent does this automatically** by interpreting your vision.

## Quick Start

### 1. Create Your Vision Document

Create `docs/product/vision.md` with these sections:

```markdown
# Project Vision

## Mission Statement
[Why does this project exist? What problem does it solve?]

## Core Principles
[What are the guiding principles?]
1. Principle one
2. Principle two
...

## Goals

### Short Term (6-12 months)
- Goal 1
- Goal 2

### Long Term (3-5 years)
- Goal 1
- Goal 2

## Success Criteria
[How will you know if you've succeeded?]
- Criterion 1
- Criterion 2

## Constraints
[What limitations or requirements exist?]
- Constraint 1
- Constraint 2
```

### 2. Run the Master Agent

```bash
# Bootstrap the entire system
python tools/agent-orchestration/master-agent.py --action bootstrap

# Or step by step:
python tools/agent-orchestration/master-agent.py --action interpret  # Just analyze vision
python tools/agent-orchestration/master-agent.py --action constitution  # Generate constitution
python tools/agent-orchestration/master-agent.py --action agents  # Identify agents
python tools/agent-orchestration/master-agent.py --action protocol  # Generate protocol
```

### 3. Review Generated Artifacts

Check `.mas-system/` directory for:

- **`vision-analysis.yaml`**: How the Master Agent interpreted your vision
- **`constitution.yaml`**: Generated laws, principles, and rules
- **`agent-specifications.yaml`**: Required agent types and roles
- **`communication-protocol.yaml`**: How agents will coordinate
- **`bootstrap-summary.md`**: Human-readable summary

### 4. Start Autonomous Execution

```bash
# Trigger the autonomous system
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous

# Or manually:
gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning  # Just planning
gh workflow run autonomous-agent-execution.yml -f mode=execute-tasks    # Execute
gh workflow run autonomous-agent-execution.yml -f mode=create-adr       # ADR generation
```

## Vision Document Best Practices

### Make It Specific

❌ **Vague**: "Build a good product"
✅ **Specific**: "Build a mobile app that helps students learn math offline"

### State Principles Clearly

❌ **Unclear**: "Quality matters"
✅ **Clear**: "Quality First - Never compromise quality for speed"

### Quantify Success

❌ **Unmeasurable**: "Users should like it"
✅ **Measurable**: "90% user satisfaction rate, < 2% crash rate"

### Define Constraints

❌ **Implicit**: (assumes constraints)
✅ **Explicit**: "Must work offline, run on 2GB RAM devices, no server required"

### Example Vision Templates

#### Software Product
```markdown
# [Product Name] Vision

## Mission
To [solve problem] for [target users] by [approach].

## Core Principles
1. User-First: Every decision prioritizes user needs
2. Simple: Easy to use without training
3. Reliable: Works consistently 99%+ of time

## Goals
### Short Term (6 months)
- MVP with core features
- 100 beta users
- User feedback incorporated

### Long Term (2 years)
- 10,000 active users
- Full feature set
- Sustainable business model

## Success Criteria
- Users can complete key task in < 2 minutes
- 90%+ user retention after 30 days
- < 0.1% error rate

## Constraints
- Budget: $X for first year
- Team: 3 developers
- Timeline: 6 months to MVP
- Must be accessible (WCAG AA)
```

#### Research Project
```markdown
# [Research Project] Vision

## Mission
To advance [research area] by [methodology], contributing [expected outcome].

## Core Principles
1. Reproducible: All results must be reproducible
2. Open: Share data, code, and findings openly
3. Rigorous: Follow scientific method strictly

## Goals
### Short Term (6 months)
- Literature review complete
- Methodology validated
- Initial experiments done

### Long Term (2 years)
- Paper published in top venue
- Code/data released
- Community adoption

## Success Criteria
- Results replicated by independent researchers
- Cited by peer research
- Methodology adopted by community

## Constraints
- Must use only open-source tools
- Data must be anonymized
- Results must be statistically significant (p < 0.05)
```

## Understanding Generated Artifacts

### Constitution (`constitution.yaml`)

The constitution defines the "laws" of your project:

```yaml
core_laws:
  - id: LAW-001
    principle: "User privacy must be protected"
    enforcement: automatic
    violation_action: reject

decision_framework:
  agent_authority:
    implement: "Implementation details"
    propose: "Architectural changes"
    escalate: "Vision/principle changes"

quality_gates:
  - name: "Code Quality"
    checks: [linting, tests, coverage]
    required: true
```

**What to review:**
- Are the core laws correct?
- Do quality gates match your needs?
- Is the decision framework appropriate?

### Agent Specifications (`agent-specifications.yaml`)

Lists all agents the system determined you need:

```yaml
agents:
  - agent_id: master-coordinator
    type: coordination
    role: "Orchestrate overall execution"
    authority: coordinate
    
  - agent_id: implementation-agent
    type: development
    role: "Implement features"
    authority: implement
    
  - agent_id: constitutional-judge
    type: enforcement
    role: "Ensure compliance"
    authority: enforce
```

**What to review:**
- Are all necessary specializations included?
- Are any agents unnecessary?
- Do roles make sense for your project?

### Communication Protocol (`communication-protocol.yaml`)

Defines how agents coordinate:

```yaml
message_formats:
  status_update:
    agent: string
    status: [in-progress, completed, blocked]
    
coordination_patterns:
  parallel: "Independent tasks simultaneously"
  sequential: "Tasks with dependencies in order"
  
workflows:
  feature_development:
    - Design
    - Implementation
    - Testing
    - Review
```

**What to review:**
- Do workflows match your development process?
- Are coordination patterns appropriate?
- Do message formats capture needed info?

## Customizing the System

### After Bootstrap

You can manually edit generated files:

```bash
# Edit constitution
nano .mas-system/constitution.yaml

# Edit agent specs
nano .mas-system/agent-specifications.yaml

# Re-run bootstrap to regenerate
python tools/agent-orchestration/master-agent.py --action bootstrap
```

### Adding Custom Agents

Create agent definition files in `.github/agents/`:

```markdown
# Custom Agent Name

## Role
[What this agent does]

## Authority
**Authority Level** - [What decisions it can make]

## Responsibilities
- Task 1
- Task 2

## Integration
- Works with: [Other agents]
- Reports to: [Coordination agent]
```

### Modifying Workflows

Edit `.github/workflows/autonomous-agent-execution.yml` to:
- Change execution frequency
- Add custom steps
- Integrate external tools

## Monitoring and Control

### Check System Status

```bash
# View sprint plan
cat tools/agent-orchestration/current-sprint.yaml

# Check agent activity
gh issue list --label "autonomous-agent"

# View workflow runs
gh run list --workflow=autonomous-agent-execution.yml
```

### Manual Intervention

```bash
# Pause autonomous execution
# (Delete or close coordination issues)

# Trigger specific action
gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning

# Review and approve
gh pr list --label "autonomous-agent"
```

### Debug Issues

```bash
# View master agent output
python tools/agent-orchestration/master-agent.py --action interpret

# Check generated constitution
cat .mas-system/constitution.yaml

# Test agent creation
python tools/agent-orchestration/agent-creator.py --action analyze
```

## Domain-Specific Examples

### Web Application

Vision emphasizes:
- User interface
- API design
- Database architecture
- Deployment

Generated agents:
- UI Development Agent
- API Development Agent
- Database Agent
- DevOps Agent

### Mobile Application

Vision emphasizes:
- Offline capability
- Mobile-first design
- Performance
- Multiple platforms

Generated agents:
- Mobile UI Agent
- Offline Sync Agent
- Performance Agent
- Platform Agent (iOS/Android)

### Data Science Project

Vision emphasizes:
- Data processing
- Model training
- Experiment tracking
- Reproducibility

Generated agents:
- Data Pipeline Agent
- ML Model Agent
- Experiment Agent
- Documentation Agent

### DevOps Infrastructure

Vision emphasizes:
- Automation
- Monitoring
- Security
- Scalability

Generated agents:
- Automation Agent
- Monitoring Agent
- Security Agent
- Infrastructure Agent

## Advanced Features

### Multi-Vision Support

You can have multiple visions in one repo:

```bash
# Bootstrap different systems
python tools/agent-orchestration/master-agent.py \
  --vision docs/product/vision-v2.md \
  --output .mas-system-v2
```

### Custom Domain Detection

The Master Agent infers domain automatically, but you can guide it:

```markdown
# Add to vision.md
## Domain
This is a [healthcare/finance/education/etc.] project
```

### Integration with Existing Tools

Add to workflows:

```yaml
# .github/workflows/autonomous-agent-execution.yml
- name: Custom Integration
  run: |
    # Your custom scripts
    ./custom-tool.sh
```

## Best Practices

### 1. Start Small

Begin with a focused vision for MVP, then expand.

### 2. Iterate on Constitution

Review and refine generated constitution based on execution.

### 3. Trust but Verify

Let agents work autonomously, but review critical decisions.

### 4. Keep Vision Updated

As project evolves, update vision document and re-run bootstrap.

### 5. Monitor Quality Gates

Ensure agents are following constitution and quality standards.

## Troubleshooting

### Vision Not Parsed Correctly

**Problem**: Master Agent misunderstands vision
**Solution**: Make vision more structured with clear headings

### Wrong Agents Generated

**Problem**: Agent types don't match needs
**Solution**: Add more specific architectural hints in vision

### Constitution Too Strict/Loose

**Problem**: Quality gates blocking or not catching issues
**Solution**: Edit `.mas-system/constitution.yaml` manually

### Agents Not Coordinating

**Problem**: Agents working in silos
**Solution**: Check communication protocol, add sync points

## FAQ

**Q: Can I use this for non-software projects?**
A: Yes! Any project with a clear vision and execution steps.

**Q: Do I need GitHub Actions?**
A: No, you can run agents locally or use other CI/CD systems.

**Q: Can agents create other agents?**
A: Yes! Agents can propose new agent types via agent-creator.py.

**Q: How do I stop autonomous execution?**
A: Close/delete coordination issues or disable workflows.

**Q: Can I have human-in-the-loop?**
A: Yes! Constitution defines what requires human approval.

**Q: Is this production-ready?**
A: This is an experimental framework. Review all agent outputs.

## Next Steps

1. **Try the example**: Use the education platform vision
2. **Create your own**: Write a vision for your project
3. **Experiment**: Run bootstrap and see what gets generated
4. **Refine**: Iterate on vision and constitution
5. **Deploy**: Start autonomous execution when ready

## Resources

- [Master Agent Documentation](README.md)
- [Communication Protocol](.github/agents/communication-protocol.md)
- [Example Visions](docs/product/)
- [Agent Definitions](.github/agents/)

---

**Remember**: The framework learns from your vision. The better your vision, the better the multi-agent system!
