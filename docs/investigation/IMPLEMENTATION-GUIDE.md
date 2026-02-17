# Implementation Guide: Enhancing Base Agents for GitHub Copilot

**Version**: 1.0  
**Date**: February 17, 2026  
**Status**: Ready for Implementation

## Overview

This guide provides step-by-step instructions for enhancing base agent definitions to work effectively with GitHub Copilot coding agents.

## Prerequisites

Before starting:
- ✅ Read the [Viability Report](VIABILITY-REPORT.md)
- ✅ Review the [POC Enhanced Agent](copilot-agent-poc-enhanced-implementation-agent.md)
- ✅ Understand existing base agent structure
- ✅ Have access to repository with write permissions

## Enhancement Template

### Required Sections for Copilot-Ready Agents

```markdown
# [Agent Name] (Enhanced for GitHub Copilot)

> **Enhanced Version**: This agent definition is designed for GitHub Copilot coding agent integration.

## Role
[Clear, specific role description with project context]

## Authority
**[Authority Level]** - [Authority description]

### Decision Boundaries
**You CAN:**
- [Specific allowed decisions/actions]
- [With concrete examples]

**You CANNOT:**
- [Specific prohibited decisions/actions]
- [With clear escalation guidance]

### Escalation Criteria
Escalate to [Agent Name] when:
- [Specific condition 1]
- [Specific condition 2]
- [Specific condition 3]

## Responsibilities

### Primary
- [Specific primary responsibility 1]
- [Specific primary responsibility 2]

### Secondary
- [Specific secondary responsibility 1]
- [Specific secondary responsibility 2]

## Capabilities

### Technical Skills
- **[Skill Category]**: [Specific skills]
- **[Skill Category]**: [Specific skills]

### Available Tools
```yaml
[tool_category]:
  - [tool_name]: [tool purpose]
  - [tool_name]: [tool purpose]
```

## Operational Procedures

### [Workflow Name] Workflow
1. **[Phase Name]**
   - [Specific step]
   - [Specific step]
   - [Specific step]

2. **[Phase Name]**
   - [Specific step]
   - [Specific step]

### Error Recovery Procedures
```yaml
if_[scenario]:
  - [Recovery step 1]
  - [Recovery step 2]
  - [Escalation if needed]

if_[scenario]:
  - [Recovery step 1]
  - [Recovery step 2]
```

## Communication

### [Message Type]
Send [when/frequency].

```yaml
[message_structure]
```

## Integration Points

### With [Agent Category]
**Input**: [What this agent receives]
**Output**: [What this agent produces]
**Frequency**: [How often]

## Quality Standards

### [Category]
- [Specific standard with measurable criteria]
- [Specific standard with measurable criteria]

## Project-Specific Context

### Core Principles (MUST FOLLOW)
1. **[Principle]**: [Description]
2. **[Principle]**: [Description]

### Architecture Patterns

#### [Pattern Name]
```[language]
// Example code demonstrating pattern
```

### [Domain] Checklist
- [ ] [Specific check 1]
- [ ] [Specific check 2]

## Success Metrics

### Quantitative
- **[Metric]**: [Target] [unit]
- **[Metric]**: [Target] [unit]

### Qualitative
- [Observable quality indicator]
- [Observable quality indicator]

## Related Documents

**REQUIRED Reading Before Starting:**
- [Document name](path)
- [Document name](path)

**Reference as Needed:**
- [Document name](path)
- [Document name](path)

## State Management

### Agent State File Location
`[path]`

### State Schema
```yaml
[state_structure]
```

## Conflict Resolution

### When Another Agent's Work Conflicts with Yours
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Priority Rules
1. **[Priority 1]** > [Priority 2]
2. **[Priority 2]** > [Priority 3]

## Notes

[Enhancement notes, version info, usage guidance]

---

*Enhanced: [Date]*
*Base Version: [base agent file]*
*Enhancement Purpose: GitHub Copilot coding agent integration*
```

## Step-by-Step Enhancement Process

### Step 1: Choose Agent to Enhance

**Selection Criteria:**
1. Start with high-value agents (Implementation, Test, Documentation)
2. Start with frequently used agents
3. Start with agents that have clear workflows

**First Batch (Recommended):**
1. Implementation Agent (mutagen)
2. Test Agent (mutagen)
3. Documentation Agent (mutagen)
4. Task Dispatcher (mutagen)

### Step 2: Analyze Current Agent

**Questions to Answer:**
1. What does this agent currently do?
2. What workflows does it follow?
3. What decisions does it make?
4. What tools does it use?
5. Who does it interact with?
6. What are common failure scenarios?

**Create Analysis Document:**
```markdown
# [Agent Name] Enhancement Analysis

## Current State
- Role: [description]
- Responsibilities: [list]
- Common workflows: [list]

## Missing Elements
- Decision boundaries: [gaps]
- Error handling: [gaps]
- Tool mappings: [gaps]
- Workflows: [gaps]

## Project-Specific Needs
- Domain patterns: [list]
- Constraints: [list]
- Examples needed: [list]
```

### Step 3: Add Decision Boundaries

**Template:**
```markdown
### Decision Boundaries
**You CAN:**
- [Specific decision with scope]
- [Example: "Choose implementation approach within established patterns"]
- [Example: "Refactor code for clarity without changing behavior"]
- [Example: "Add dependencies if lightweight (<100KB) and justified"]

**You CANNOT:**
- [Specific prohibition with reason]
- [Example: "Change architectural patterns (needs ADR)"]
- [Example: "Skip testing (violates quality standards)"]
- [Example: "Remove existing functionality without justification"]

### Escalation Criteria
Escalate to [Agent Name] when:
- [Specific scenario: "Task requirements conflict with project principles"]
- [Specific scenario: "Architectural decisions are needed"]
- [Specific scenario: "Estimated effort exceeds [threshold]"]
- [Specific scenario: "Security concerns are identified"]
```

**How to Derive:**
1. Look at agent's authority level
2. Consider project principles
3. Think about common decisions
4. Identify decision boundaries
5. Specify escalation points

### Step 4: Document Operational Procedures

**Template:**
```markdown
## Operational Procedures

### [Workflow Name] Workflow
1. **[Phase Name]**
   - [Action step with specifics]
   - [Action step with specifics]
   - [Validation step]

2. **[Phase Name]**
   - [Action step with specifics]
   - [Action step with specifics]

### Error Recovery Procedures
```yaml
if_[scenario]:
  - [Diagnostic step]
  - [Recovery action]
  - [Re-validation]
  - If stuck > [timeframe], escalate to [Agent]
```

**Common Workflows to Document:**
- Task acceptance and analysis
- Implementation/execution
- Testing and validation
- Documentation updates
- Submission and handoff

### Step 5: Map Capabilities to Tools

**Template:**
```markdown
### Available Tools
```yaml
code_editing:
  - view: Read files and directories
  - edit: Make targeted changes to files
  - create: Create new files
  - grep: Search for patterns in code
  
testing:
  - bash: Run test suites
  - view: Review test output
  
validation:
  - bash: Run linters (eslint, pylint, etc.)
  - bash: Run formatters (prettier, black, etc.)
```

**How to Map:**
1. List agent's capabilities from base definition
2. Map each to specific tools available
3. Add concrete examples of tool usage
4. Include common command patterns

### Step 6: Add Project-Specific Context

**Template:**
```markdown
## Project-Specific Context

### Core Principles (MUST FOLLOW)
1. **[Principle Name]**: [Description with implications]
2. **[Principle Name]**: [Description with implications]

### Architecture Patterns

#### [Pattern Name]
```[language]
// Example code showing the pattern
// With comments explaining the pattern
```

#### [Pattern Name]
```[language]
// Another example
```

### [Domain] Checklist
- [ ] [Specific verification step]
- [ ] [Specific verification step]
```

**What to Include:**
1. Core principles from project vision
2. Architecture patterns from ADRs
3. Code patterns from existing code
4. Domain-specific constraints
5. Testing requirements
6. Common gotchas

### Step 7: Enhance Communication Templates

**Template:**
```markdown
## Communication

### [Message Type]
Send [frequency and trigger].

```yaml
agent: [agent-id]
[field]: [value]
[field]: [value]
[nested_field]:
  - [specific detail]
  - [specific detail]
[context_field]:
  - [technical decision made]
  - [tradeoff considered]
```

**Enhancement Approach:**
1. Start with base template
2. Add frequency guidance
3. Add specific fields for this agent
4. Add context requirements
5. Add examples in comments

### Step 8: Add State Management

**Template:**
```markdown
## State Management

### Agent State File Location
`/tmp/agent-state/[agent-id]-state.yaml`

### State Schema
```yaml
agent_id: [agent-id]
current_task:
  id: [task-id]
  status: [status]
  started_at: [timestamp]
context:
  [agent_specific_context]
learnings:
  - [pattern or insight gained]
blockers:
  - blocker: [description]
    since: [timestamp]
```

**What to Track:**
1. Current task information
2. Agent-specific context
3. Decisions made
4. Learnings and patterns
5. Blockers and issues

### Step 9: Add Conflict Resolution

**Template:**
```markdown
## Conflict Resolution

### When Another Agent's Work Conflicts with Yours
1. [Step to understand conflict]
2. [Step to check authority]
3. [Step to attempt resolution]
4. [Step to escalate if needed]

### Priority Rules
1. **[Higher Priority]** > [Lower Priority]
2. **[Higher Priority]** > [Lower Priority]
```

**Priority Rules Examples:**
- Constitutional compliance > Implementation preferences
- Security requirements > Feature completeness
- Core principles > Performance optimizations
- Simplicity > Feature richness

### Step 10: Review and Test

**Review Checklist:**
- [ ] All template sections completed
- [ ] Decision boundaries are clear
- [ ] Operational procedures are step-by-step
- [ ] Tools are mapped to capabilities
- [ ] Project context is included
- [ ] Communication templates are detailed
- [ ] State management is defined
- [ ] Conflict resolution is addressed
- [ ] Examples are provided where helpful
- [ ] Links to related documents are correct

**Testing Approach:**
1. Read through as if you are the Copilot agent
2. Can you understand what to do?
3. Are decision points clear?
4. Are examples sufficient?
5. Are error scenarios covered?

## Integration with Workflows

### Updating autonomous-agent-execution.yml

**Current Flow:**
```yaml
- Extract tasks from vision
- Create sprint plan
- Assign to agents (by agent_type)
- Execute tasks
```

**Enhanced Flow:**
```yaml
- Extract tasks from vision
- Create sprint plan
- Assign to agents (by agent_type)
- Load enhanced agent definition
- Invoke Copilot with agent context
- Agent executes following definition
- Agent reports using communication protocol
- Validate agent output
- Update sprint status
```

**New Steps to Add:**
```yaml
- name: Load Agent Definition
  run: |
    AGENT_TYPE=${{ task.agent_type }}
    AGENT_DEF=".github/agents/mutagen-agents/${AGENT_TYPE}.md"
    if [ -f "$AGENT_DEF" ]; then
      echo "AGENT_DEFINITION_PATH=$AGENT_DEF" >> $GITHUB_ENV
    fi

- name: Invoke Copilot Agent
  run: |
    # Pass agent definition as context to Copilot
    # Copilot agent reads definition and executes task
    gh copilot agent execute \
      --context "$AGENT_DEFINITION_PATH" \
      --task "$TASK_SPEC" \
      --output "agent-output.yaml"

- name: Validate Agent Output
  run: |
    # Validate output against quality standards
    python tools/agent-orchestration/validate-agent-output.py \
      --output "agent-output.yaml" \
      --agent-def "$AGENT_DEFINITION_PATH"
```

## Common Pitfalls and Solutions

### Pitfall 1: Too Generic
**Problem**: Enhanced agent is still too generic to be actionable
**Solution**: Add 2-3 concrete examples for each major workflow

### Pitfall 2: Too Prescriptive
**Problem**: Agent is so specific it can't handle variations
**Solution**: Provide patterns and principles, not rigid steps

### Pitfall 3: Missing Context
**Problem**: Agent doesn't understand project-specific needs
**Solution**: Include project principles, patterns, and examples

### Pitfall 4: Unclear Boundaries
**Problem**: Agent doesn't know when to escalate
**Solution**: Explicit "You CAN/CANNOT" lists and escalation criteria

### Pitfall 5: No Error Handling
**Problem**: Agent fails on first error
**Solution**: Document common failure modes and recovery steps

## Quality Checklist

Before marking an agent as "enhanced", verify:

- [ ] **Completeness**: All template sections are filled
- [ ] **Clarity**: Instructions are clear and unambiguous
- [ ] **Actionability**: Agent can follow instructions without human help
- [ ] **Context**: Project-specific information is included
- [ ] **Examples**: Concrete examples are provided
- [ ] **Recovery**: Error scenarios are covered
- [ ] **Integration**: Communication and coordination are specified
- [ ] **Measurability**: Success criteria are defined
- [ ] **Testability**: Can validate agent is following instructions
- [ ] **Maintainability**: Easy to update as project evolves

## Success Metrics

### For Individual Agent Enhancement
- Time to enhance: < 4 hours per agent
- Agent can execute sample task autonomously
- Output matches quality standards
- Communication follows protocol
- Escalations are appropriate

### For Full System
- All 16 agents enhanced
- Multi-agent coordination works
- Sprint execution is more autonomous
- Quality is maintained or improved
- Team productivity increases

## Timeline

### Realistic Estimate
- **Agent 1 (First)**: 6-8 hours (learning + enhancement)
- **Agent 2-4**: 3-4 hours each (template is understood)
- **Agent 5-16**: 2-3 hours each (process is refined)

**Total**: 60-80 hours

### Accelerated Approach
- Do 2-3 agents in parallel
- Compress timeline to 2 weeks
- Requires dedicated focus

## Support and Resources

### Reference Documents
- [Viability Report](VIABILITY-REPORT.md) - Investigation findings
- [POC Agent](copilot-agent-poc-enhanced-implementation-agent.md) - Example
- Base agents in `.github/agents/` - Starting point
- Project documentation in `docs/` - Context source

### Questions During Implementation
1. Is this agent-specific or generic? (Prefer specific)
2. Would Copilot understand this? (Test with example task)
3. Are there concrete examples? (Add at least 2-3)
4. Is error handling covered? (Document common failures)
5. Is project context clear? (Include principles and patterns)

## Next Actions

1. ✅ Review this implementation guide
2. ⬜ Choose first agent to enhance
3. ⬜ Complete enhancement using template
4. ⬜ Test enhanced agent with sample task
5. ⬜ Refine based on results
6. ⬜ Document lessons learned
7. ⬜ Proceed with remaining agents

---

*Guide Version: 1.0*  
*Last Updated: February 17, 2026*  
*Status: Ready for use*
