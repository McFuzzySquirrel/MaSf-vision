# Generic Agent Enhancement Template

**Purpose**: Universal template for enhancing base agents across any project type  
**Version**: 1.0  
**Date**: February 17, 2026

## Overview

This is a **project-agnostic template** for enhancing base agent definitions. The structure is universal; the content should be customized for your specific project.

## What's Generic vs. Project-Specific

### ✅ Generic Structure (Use As-Is)
- Section headers and organization
- Types of information to include
- Communication templates format
- State management approach
- Conflict resolution framework

### 🔧 Project-Specific Content (Customize)
- Core principles and values
- Technology stack and tools
- Architecture patterns
- Domain-specific workflows
- Quality standards
- Success metrics
- Testing requirements

## Universal Template

```markdown
# [Agent Name] (Enhanced for GitHub Copilot)

> **Enhanced Version**: This agent definition is designed for GitHub Copilot coding agent integration for [PROJECT NAME].

## Role
[Clear description of agent's purpose within YOUR project context]

## Authority
**[Authority Level]** - [Authority description]

### Decision Boundaries
**You CAN:**
- [List allowed decisions specific to this agent's role]
- [Include YOUR project's standards and patterns]
- [Reference YOUR technology choices]

**You CANNOT:**
- [List prohibited actions]
- [Reference YOUR project's architectural constraints]
- [Note what requires escalation in YOUR context]

### Escalation Criteria
Escalate to [YOUR coordinator agent] when:
- [Situation conflicts with YOUR project principles]
- [Estimated effort exceeds YOUR project threshold]
- [Security concerns in YOUR context]
- [YOUR project-specific escalation triggers]

## Responsibilities

### Primary
- [Agent's main duties in YOUR project]
- [Using YOUR tech stack]
- [Following YOUR standards]

### Secondary
- [Supporting duties]
- [Collaboration expectations in YOUR team]

## Capabilities

### Technical Skills
- **[Category relevant to YOUR project]**: [Specific skills]
- **[YOUR tech stack]**: [Tools and frameworks you use]
- **[YOUR development practices]**: [Methodologies]

### Available Tools
```yaml
[category]:
  - [tool_name]: [how it's used in YOUR project]
  - [YOUR specific tools]: [their purposes]
```

## Operational Procedures

### [Workflow Name - YOUR Process]
1. **[Phase Name]**
   - [Steps following YOUR methodology]
   - [Using YOUR tools]
   - [Meeting YOUR standards]

2. **[Next Phase]**
   - [YOUR specific steps]

### Error Recovery Procedures
```yaml
if_[scenario_in_YOUR_context]:
  - [Recovery steps using YOUR tools]
  - [Escalation to YOUR team members]

if_[YOUR_specific_failure_mode]:
  - [YOUR recovery process]
```

## Communication

### [Message Type]
Send [frequency appropriate for YOUR team].

```yaml
agent: [agent-id]
[YOUR required fields]
[YOUR context information]
```

## Integration Points

### With [YOUR Other Agents]
**Input**: [What this agent receives in YOUR workflow]
**Output**: [What this agent produces in YOUR workflow]
**Frequency**: [YOUR cadence]

## Quality Standards

### [YOUR Quality Category]
- [YOUR specific standard with measurable criteria]
- [Using YOUR metrics]

## Project-Specific Context

⚠️ **CUSTOMIZE THIS ENTIRE SECTION FOR YOUR PROJECT**

### Core Principles (YOUR PROJECT VALUES)
1. **[YOUR Principle 1]**: [Description and implications]
2. **[YOUR Principle 2]**: [Description and implications]
3. **[YOUR Principle 3]**: [Description and implications]

### Architecture Patterns (YOUR TECH STACK)

#### [YOUR Pattern Name]
```[YOUR language]
// Example code showing YOUR pattern
// Using YOUR frameworks and libraries
// Following YOUR conventions
```

#### [YOUR Another Pattern]
```[YOUR language]
// Another pattern example
// Specific to YOUR architecture
```

### [YOUR Domain] Checklist
- [ ] [YOUR verification step 1]
- [ ] [YOUR verification step 2]
- [ ] [YOUR specific requirements]

### Anti-Patterns (YOUR CONTEXT)
**Don't:**
- ❌ [Anti-pattern specific to YOUR project]
- ❌ [YOUR common mistakes]

**Do Instead:**
- ✅ [YOUR preferred approach]
- ✅ [YOUR best practice]

## Success Metrics

### Quantitative (YOUR TARGETS)
- **[YOUR Metric]**: [YOUR Target] [YOUR unit]
- **[YOUR KPI]**: [YOUR Goal]

### Qualitative (YOUR STANDARDS)
- [Observable quality in YOUR context]
- [YOUR team's expectations]

## Related Documents

**REQUIRED Reading Before Starting:**
- [YOUR Project Documentation]
- [YOUR Coding Standards]
- [YOUR Architecture Docs]

**Reference as Needed:**
- [YOUR ADRs]
- [YOUR API Docs]

## State Management

### Agent State File Location
`/tmp/agent-state/[agent-id]-state.yaml`

### State Schema
```yaml
agent_id: [agent-id]
current_task:
  id: [task-id]
  status: [status]
[YOUR additional state fields]
context:
  [YOUR agent-specific context]
learnings:
  - [Insights relevant to YOUR project]
```

## Conflict Resolution

### When Another Agent's Work Conflicts with Yours
1. [Step considering YOUR agent hierarchy]
2. [Check authority in YOUR system]
3. [YOUR escalation process]

### Priority Rules (YOUR PROJECT PRIORITIES)
1. **[YOUR Highest Priority]** > [Lower priority]
2. **[YOUR Next Priority]** > [Even lower]
[YOUR specific priority hierarchy]

## Notes

This agent has been enhanced for GitHub Copilot integration following [YOUR PROJECT]'s standards and practices.

---

*Enhanced: [Date]*
*Project: [YOUR PROJECT NAME]*
*Based on: Universal Agent Enhancement Template v1.0*
```

## Example Adaptations for Different Project Types

### Web Application Project
**Core Principles:**
- API-first architecture
- RESTful design
- Microservices patterns
- Cloud-native deployment

**Tech Stack:**
- Node.js, React, PostgreSQL
- Docker, Kubernetes
- AWS services

**Patterns:**
```javascript
// API route pattern
app.get('/api/resource/:id', async (req, res) => {
  const data = await service.get(req.params.id);
  res.json(data);
});
```

### Data Science Project
**Core Principles:**
- Reproducible research
- Data versioning
- Experiment tracking
- Model validation

**Tech Stack:**
- Python, Jupyter, pandas, scikit-learn
- MLflow, DVC
- Cloud compute

**Patterns:**
```python
# Experiment tracking pattern
with mlflow.start_run():
    model = train_model(data)
    mlflow.log_metrics({"accuracy": score})
    mlflow.log_model(model)
```

### DevOps/Infrastructure Project
**Core Principles:**
- Infrastructure as Code
- Immutable infrastructure
- Continuous deployment
- Observability

**Tech Stack:**
- Terraform, Kubernetes, Helm
- Prometheus, Grafana
- GitOps workflows

**Patterns:**
```hcl
# Terraform module pattern
module "service" {
  source = "./modules/service"
  replicas = var.replicas
  image = var.image_tag
}
```

### Mobile Game Project
**Core Principles:**
- Performance optimization
- Battery efficiency
- Offline gameplay
- Cross-platform support

**Tech Stack:**
- Unity/Unreal, C#/C++
- Asset pipelines
- Platform SDKs

**Patterns:**
```csharp
// Object pooling pattern
public class Pool<T> where T : MonoBehaviour {
    private Queue<T> pool = new Queue<T>();
    public T Get() => pool.Count > 0 ? pool.Dequeue() : Instantiate();
}
```

## Customization Checklist

When adapting this template for your project:

- [ ] Replace all "[YOUR ...]" placeholders with your specifics
- [ ] Update **Core Principles** section with your values
- [ ] Add **Architecture Patterns** with your tech stack examples
- [ ] Customize **Quality Standards** to your metrics
- [ ] Set **Success Metrics** to your team's KPIs
- [ ] Update **Tool Mappings** to your available tools
- [ ] Adjust **Escalation Criteria** to your thresholds
- [ ] Modify **Communication** templates for your workflow
- [ ] Define **Priority Rules** for your project hierarchy
- [ ] Add **Anti-Patterns** specific to your domain
- [ ] Update **Related Documents** links
- [ ] Customize **Testing Checklist** for your requirements

## What Stays Consistent

Regardless of project type, these elements remain the same:

1. **Section Structure**: All agents should have the same sections
2. **Communication Format**: YAML templates for status/requests
3. **State Management**: Consistent schema approach
4. **Escalation Framework**: Always define clear criteria
5. **Decision Boundaries**: Always separate CAN/CANNOT
6. **Error Recovery**: Always include failure handling
7. **Conflict Resolution**: Always define priority rules

## Benefits of This Approach

### For Any Project Type:
✅ **Consistency**: All agents follow same structure  
✅ **Completeness**: All necessary sections included  
✅ **Clarity**: Clear boundaries and procedures  
✅ **Actionable**: GitHub Copilot can execute autonomously  
✅ **Maintainable**: Easy to update as project evolves  
✅ **Scalable**: Pattern works for 5 or 50 agents  

### Project-Specific Customization:
✅ **Relevant**: Content matches your actual workflow  
✅ **Accurate**: Patterns reflect your tech stack  
✅ **Aligned**: Standards match your team's practices  
✅ **Practical**: Examples use your real tools  

## Migration Path for Existing Projects

### Step 1: Identify Your Project Type
- Web/API backend
- Mobile application
- Data/ML pipeline
- Desktop application
- DevOps/Infrastructure
- Game development
- Embedded systems
- Other

### Step 2: Gather Your Project Assets
- Architecture documentation
- Coding standards
- Tech stack list
- Common patterns
- Quality metrics
- Team workflows

### Step 3: Customize the Template
- Replace placeholder text
- Add your code examples
- Update tool references
- Adjust metrics/standards

### Step 4: Apply to Your Agents
- Start with 2-3 priority agents
- Validate with real tasks
- Refine based on results
- Scale to remaining agents

## Frequently Asked Questions

**Q: Do I need to customize every single section?**  
A: Yes, especially the "Project-Specific Context" section. Other sections can use the template language but should reference your specific tools/processes.

**Q: Can I remove sections that don't apply?**  
A: It's better to keep all sections but adjust content. For example, if you don't have formal ADRs, just reference your architecture docs instead.

**Q: How do I handle multiple tech stacks in one project?**  
A: Create stack-specific agents (e.g., Frontend Implementation Agent, Backend Implementation Agent) or include multiple pattern sections.

**Q: Should enforcement agents be different?**  
A: Yes! Enforcement agents need different operational procedures focused on validation, not implementation. But the structure remains the same.

## Summary

The **structure** is universal and works for any project:
- Decision Boundaries
- Operational Procedures  
- Tool Mappings
- Error Recovery
- Communication
- State Management
- Conflict Resolution

The **content** must be customized for each project:
- Core principles
- Tech stack
- Patterns
- Standards
- Metrics
- Workflows

**Use this template as a starting point, then customize every "[YOUR ...]" placeholder to match your project's reality.**

---

*Template Version: 1.0*  
*Created: February 17, 2026*  
*Purpose: Enable agent enhancement for any project type*
