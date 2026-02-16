# Setup Guide: Autonomous Agent Execution

This guide explains how to set up the autonomous agent execution system in your own repository, and what files you need to copy from the MaSf-vision framework.

## Problem Statement

When users try to run `autonomous-agent-execution.yml` workflow in their own repository, they may encounter errors like:
```
Error: Not found https://api.github.com/repos/...
```

This happens because the workflow and supporting files haven't been copied to your repository yet.

## Quick Setup Checklist

Use this checklist to verify your setup is complete:

- [ ] **Workflows copied** to `.github/workflows/`:
  - [ ] `autonomous-agent-execution.yml`
  - [ ] `adr-generation.yml` (optional)
  - [ ] `pr-evaluation.yml` (optional)
- [ ] **Tools copied** to `tools/agent-orchestration/`:
  - [ ] `vision-task-extractor.py`
  - [ ] `master-agent.py`
  - [ ] `agent-creator.py`
  - [ ] `agent-definition-generator.py`
  - [ ] `pr-constitution-generator.py`
- [ ] **Agent protocol copied** to `.github/agents/`:
  - [ ] `communication-protocol.md`
- [ ] **Vision document created** at `docs/product/vision.md`
- [ ] **Backlog created** at `docs/development/backlog-v1.md` (recommended for task extraction)
- [ ] **GitHub permissions configured** (contents: write, pull-requests: write, issues: write)
- [ ] **Python dependencies installed** (`pyyaml`)
- [ ] **First workflow run successful**

> **Tip**: Use the bootstrap tool to automatically complete all these steps: `python /path/to/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo .`

## Required Files

To use the autonomous agent execution system, you need to copy the following files from the MaSf-vision repository to your own repository:

### 1. Core Workflows (Required)

Copy these workflow files to `.github/workflows/` in your repository:

```bash
.github/workflows/autonomous-agent-execution.yml  # Main autonomous execution workflow
.github/workflows/adr-generation.yml              # Automatic ADR generation (optional but recommended)
.github/workflows/pr-evaluation.yml               # PR validation workflow (optional but recommended)
```

### 2. Agent Orchestration Tools (Required)

Copy these Python tools to `tools/agent-orchestration/` in your repository:

```bash
tools/agent-orchestration/vision-task-extractor.py      # Extracts tasks from vision
tools/agent-orchestration/master-agent.py               # Master agent for system bootstrap
tools/agent-orchestration/agent-creator.py              # Creates specialized agents
tools/agent-orchestration/agent-definition-generator.py # Generates agent definitions
tools/agent-orchestration/pr-constitution-generator.py  # Generates PR constitution
```

### 3. Agent Communication Protocol (Required)

Copy this file to `.github/agents/`:

```bash
.github/agents/communication-protocol.md  # Defines how agents communicate
```

### 4. Documentation Templates (Optional)

If you want to start with example templates:

```bash
tools/agent-orchestration/README.md                # Tool documentation
tools/agent-orchestration/README-pr-constitution.md  # PR constitution guide
```

## Quick Setup Methods

### Method 1: Using the Bootstrap Tool (Recommended)

The easiest way to set up everything is to use the bootstrap tool:

```bash
# Navigate to your repository
cd /path/to/your/repo

# Run the bootstrap tool from the MaSf-vision framework
python /path/to/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo .

# Follow the prompts
```

**What the bootstrap tool does:**
1. ✅ Creates necessary directory structure
2. ✅ Copies all required tools and workflows
3. ✅ Generates PR constitution from your vision
4. ✅ Sets up agent communication protocols
5. ✅ Creates sample documentation if needed

### Method 2: Manual Setup

If you prefer to copy files manually:

```bash
# In your repository, create directories
mkdir -p .github/workflows .github/agents tools/agent-orchestration

# Copy workflows
cp /path/to/MaSf-vision/.github/workflows/autonomous-agent-execution.yml .github/workflows/
cp /path/to/MaSf-vision/.github/workflows/adr-generation.yml .github/workflows/
cp /path/to/MaSf-vision/.github/workflows/pr-evaluation.yml .github/workflows/

# Copy agent orchestration tools
cp /path/to/MaSf-vision/tools/agent-orchestration/vision-task-extractor.py tools/agent-orchestration/
cp /path/to/MaSf-vision/tools/agent-orchestration/master-agent.py tools/agent-orchestration/
cp /path/to/MaSf-vision/tools/agent-orchestration/agent-creator.py tools/agent-orchestration/
cp /path/to/MaSf-vision/tools/agent-orchestration/agent-definition-generator.py tools/agent-orchestration/
cp /path/to/MaSf-vision/tools/agent-orchestration/pr-constitution-generator.py tools/agent-orchestration/

# Copy agent communication protocol
cp /path/to/MaSf-vision/.github/agents/communication-protocol.md .github/agents/

# Optional: Copy documentation
cp /path/to/MaSf-vision/tools/agent-orchestration/README*.md tools/agent-orchestration/
```

### Method 3: Using Git Sparse Checkout

For a cleaner approach using git:

```bash
# In your repository
git remote add masf-framework https://github.com/McFuzzySquirrel/MaSf-vision.git
git fetch masf-framework

# Cherry-pick specific files
git checkout masf-framework/main -- .github/workflows/autonomous-agent-execution.yml
git checkout masf-framework/main -- .github/workflows/adr-generation.yml
git checkout masf-framework/main -- .github/workflows/pr-evaluation.yml
git checkout masf-framework/main -- tools/agent-orchestration/
git checkout masf-framework/main -- .github/agents/communication-protocol.md

# Commit the files
git commit -m "Add MaSf-vision autonomous agent framework files"
```

## Prerequisites

Before running the autonomous agent execution workflow, ensure you have:

### 1. Vision Document

Create your project vision in one of these locations:
- `docs/product/vision.md` (recommended)
- `docs/vision.md`
- `VISION.md`

See [Vision Document Requirements](#vision-document-requirements) below.

### 2. Backlog Document (Optional but Recommended)

For the autonomous agent execution to generate meaningful sprint plans, create a backlog at:
- `docs/development/backlog-v1.md`

The backlog should contain epics and tasks. If no backlog exists, the system will work from vision only but may have limited task extraction.

**Example backlog structure:**
```markdown
## Epic 1: User Authentication
- Implement login system
- Add password reset
- Setup OAuth integration

## Epic 2: Dashboard
- Create main dashboard layout
- Add analytics widgets
- Implement data refresh
```

### 3. GitHub Permissions

The workflows need specific permissions. Add to your workflow file or ensure repository settings allow:

```yaml
permissions:
  contents: write      # To commit changes
  pull-requests: write # To create/update PRs
  issues: write        # To create issues
```

### 4. Python Dependencies

The tools require Python 3.8+ and the following packages:
- `pyyaml` (for YAML parsing)

Install with:
```bash
pip install pyyaml
```

## Vision Document Requirements

Your vision document should include these sections for the system to work properly:

```markdown
# Project Vision

## Mission Statement
[What your project aims to achieve]

## Guiding Principles
1. **Principle 1**: Description
2. **Principle 2**: Description
3. **Principle 3**: Description

## Goals
### Short Term (6-12 months)
- Goal 1
- Goal 2

### Long Term (2-5 years)
- Goal 1
- Goal 2

## Success Criteria
- How you'll measure success
- Key metrics

## Constraints (Optional)
- Technical constraints
- Resource constraints
```

## Running the Autonomous Agent System

Once setup is complete, you can trigger autonomous execution:

### Manual Trigger

```bash
# Full autonomous mode (recommended for first run)
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous

# Individual modes
gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning
gh workflow run autonomous-agent-execution.yml -f mode=execute-tasks
gh workflow run autonomous-agent-execution.yml -f mode=create-adr
```

### Scheduled Execution

The workflow is configured to run automatically:
- **Weekly**: Every Monday at 9 AM UTC
- Checks for new work and creates sprint plans

You can modify the schedule in `.github/workflows/autonomous-agent-execution.yml`:

```yaml
schedule:
  - cron: '0 9 * * 1'  # Modify this line
```

## What Happens When You Run It

### 1. Sprint Planning Mode

The workflow will:
1. ✅ Read your vision document
2. ✅ Extract actionable tasks and epics
3. ✅ Generate a sprint plan (`tools/agent-orchestration/current-sprint.yaml`)
4. ✅ Create a GitHub issue with the sprint plan
5. ✅ Set up task assignments

### 2. Execute Tasks Mode

The workflow will:
1. ✅ Download the sprint plan
2. ✅ Coordinate agent execution
3. ✅ Create tracking issues
4. ✅ Monitor progress

### 3. Create ADR Mode

The workflow will:
1. ✅ Detect architectural decisions in recent commits
2. ✅ Suggest ADRs that should be created
3. ✅ Create issues for tracking

### 4. Full Autonomous Mode

Runs all three modes in sequence for complete autonomous operation.

## Troubleshooting

### Error: "Not found https://api.github.com/repos/..."

**Cause**: The workflow is trying to access your repository via GitHub API, but the workflow file references don't exist yet.

**Solution**:
1. Make sure you've copied all required files (see [Required Files](#required-files))
2. Commit and push the files to your repository
3. Verify the workflow file exists in `.github/workflows/`
4. Check GitHub Actions tab to see if the workflow is recognized

### Error: "Vision document not found"

**Cause**: The vision-task-extractor.py can't find your vision document.

**Solution**:
1. Create vision document at `docs/product/vision.md`
2. Or update the workflow to point to your vision location
3. Ensure the vision has the required structure

### Error: "Permission denied"

**Cause**: GitHub Actions doesn't have required permissions.

**Solution**:
1. Go to repository Settings → Actions → General
2. Set "Workflow permissions" to "Read and write permissions"
3. Enable "Allow GitHub Actions to create and approve pull requests"

### Error: "Module 'yaml' not found"

**Cause**: PyYAML is not installed in the workflow runner.

**Solution**: The workflow already includes:
```yaml
- name: Install dependencies
  run: pip install pyyaml
```

If this fails, check your workflow file has this step.

### Workflow doesn't appear in Actions tab

**Cause**: Workflow file has syntax errors or isn't in the correct location.

**Solution**:
1. Verify file is at `.github/workflows/autonomous-agent-execution.yml`
2. Validate YAML syntax: `yamllint .github/workflows/autonomous-agent-execution.yml`
3. Check for typos in workflow name and structure
4. Push the file to the main/master branch

### No sprint plan generated

**Cause**: Vision document doesn't have recognizable structure, or backlog is missing.

**Solution**:
1. Ensure vision has clear headings: "Goals", "Principles", etc.
2. Create a backlog file at `docs/development/backlog-v1.md` with epics and tasks
3. Add specific tasks/epics in your backlog for the system to extract
4. Run vision-task-extractor.py locally to debug:
   ```bash
   python tools/agent-orchestration/vision-task-extractor.py --repo-root . --output /tmp/test-sprint.yaml
   ```

### Error: "Backlog file not found"

**Cause**: The vision-task-extractor requires a backlog file to generate sprint plans.

**Solution**:
1. Create `docs/development/backlog-v1.md`
2. Add epics and tasks in markdown format
3. The backlog should list concrete work items the system can extract

## Verifying Your Setup

### 1. Check Files Are Present

```bash
# Verify workflows exist
ls -la .github/workflows/autonomous-agent-execution.yml
ls -la .github/workflows/adr-generation.yml
ls -la .github/workflows/pr-evaluation.yml

# Verify tools exist
ls -la tools/agent-orchestration/*.py

# Verify agent protocol exists
ls -la .github/agents/communication-protocol.md
```

### 2. Test the Tools Locally

```bash
# Test vision task extractor
python tools/agent-orchestration/vision-task-extractor.py \
    --repo-root . \
    --output /tmp/test-sprint.yaml

# Check the output
cat /tmp/test-sprint.yaml
```

### 3. Trigger a Test Workflow

```bash
# Trigger sprint planning only (safest test)
gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning

# Check the workflow status
gh run list --workflow=autonomous-agent-execution.yml

# View workflow details
gh run view $(gh run list --workflow=autonomous-agent-execution.yml --json databaseId -q '.[0].databaseId')
```

## Customizing for Your Project

### Modify Sprint Duration

Edit the workflow to change default sprint duration:

```yaml
inputs:
  sprint_duration:
    description: 'Sprint duration in days'
    required: false
    default: '14'  # Change this value
```

### Adjust Scheduling

Change when the workflow runs automatically:

```yaml
schedule:
  - cron: '0 9 * * 1'  # Every Monday at 9 AM UTC
  # Change to: '0 9 * * 5' for Friday
  # Or: '0 0 1 * *' for first day of month
```

### Add Custom Agent Types

Modify `tools/agent-orchestration/vision-task-extractor.py` to recognize your custom agent types:

```python
def _suggest_agent_type(self, task_description: str) -> str:
    """Suggest agent type based on task."""
    desc_lower = task_description.lower()
    
    # Add your custom agent types here
    if 'your-custom-keyword' in desc_lower:
        return 'your-custom-agent'
    
    # ... existing logic
```

## Next Steps After Setup

1. ✅ **Commit all files to your repository**
   ```bash
   git add .github/ tools/
   git commit -m "Add MaSf-vision autonomous agent framework"
   git push
   ```

2. ✅ **Create or verify your vision document** at `docs/product/vision.md`

3. ✅ **Run the bootstrap** (if you haven't already)
   ```bash
   python tools/agent-orchestration/master-agent.py --action bootstrap
   ```

4. ✅ **Trigger your first autonomous execution**
   ```bash
   gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous
   ```

5. ✅ **Monitor the execution** in GitHub Actions tab

6. ✅ **Review generated issues** for sprint plans and tasks

7. ✅ **Iterate on your vision** as the system learns your project

## Common Pitfalls and Solutions

### 1. Forgetting to Copy All Required Files

**Problem**: Workflow runs but fails with "file not found" errors.

**Solution**: Use the checklist at the top of this guide to ensure all files are copied. The bootstrap tool automatically handles this.

### 2. Not Configuring GitHub Permissions

**Problem**: Workflow fails with "permission denied" errors.

**Solution**: 
- Go to repository Settings → Actions → General
- Set "Workflow permissions" to "Read and write permissions"
- Enable "Allow GitHub Actions to create and approve pull requests"

### 3. Running Workflow Before Committing Files

**Problem**: Workflow doesn't find the required files.

**Solution**: Always commit and push all copied files to your repository before triggering the workflow.

### 4. Missing or Improperly Formatted Vision

**Problem**: Sprint plan is empty or doesn't extract tasks properly.

**Solution**: Ensure your vision document has:
- Clear section headings (use `##` for main sections)
- "Guiding Principles" or "Principles" section with numbered list
- "Goals" section with short-term and long-term goals
- Proper markdown formatting

### 5. Trying to Run in a Forked Repository

**Problem**: Workflow might not have proper permissions in forks.

**Solution**: The autonomous-agent-execution workflow is designed for the main repository. For forks, you may need to adjust permissions or workflow triggers.

### 6. Using Relative Paths in Custom Scripts

**Problem**: Custom scripts fail to find files.

**Solution**: Always use absolute paths or paths relative to repository root when modifying tools.

### 7. Not Installing Python Dependencies

**Problem**: Workflow fails with "module not found" errors.

**Solution**: The workflow includes dependency installation. If running tools locally, ensure `pyyaml` is installed: `pip install pyyaml`

### 8. Modifying Workflows Without Testing

**Problem**: Workflow syntax errors prevent execution.

**Solution**: 
- Validate YAML syntax before committing
- Test workflows with manual triggers before relying on scheduled runs
- Start with `mode=sprint-planning` for safest testing

## Getting Help

- **Framework Documentation**: [README.md](README.md)
- **Quick Start Guide**: [QUICK-START.md](QUICK-START.md)
- **Tool Documentation**: [tools/agent-orchestration/README.md](tools/agent-orchestration/README.md)
- **PR Validation Setup**: [QUICK-START-PR-VALIDATION.md](QUICK-START-PR-VALIDATION.md)

## Summary

The autonomous agent execution system requires:

1. **Workflows** copied to `.github/workflows/`
2. **Tools** copied to `tools/agent-orchestration/`
3. **Agent protocols** copied to `.github/agents/`
4. **Vision document** created at `docs/product/vision.md`
5. **GitHub permissions** configured properly

Use the bootstrap tool for easiest setup, or follow manual steps for more control.

Once setup is complete, the system will autonomously plan sprints, extract tasks, coordinate agents, and execute your project vision.
