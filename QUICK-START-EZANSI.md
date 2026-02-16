# Quick Start: Setting Up MaSf-vision in eZansiEdgeAI Repository

## The Problem

You're getting this error when trying to run the autonomous agent workflow:
```bash
HTTP 404: Not Found (https://api.github.com/repos/eZansiEdgeAI/ezansieedgeai/actions/workflows/autonomous-agent-execution.yml)
```

**Why?** The eZansiEdgeAI repository doesn't have the MaSf-vision framework files yet. You need to bootstrap the framework into your repository first.

## Solution: Two Quick Methods

### Method 1: Using the Bootstrap Tool (Easiest)

1. **Clone MaSf-vision** (if you haven't already):
   ```bash
   cd ~/Projects
   git clone https://github.com/McFuzzySquirrel/MaSf-vision.git
   ```

2. **Navigate to your eZansiEdgeAI repository**:
   ```bash
   cd ~/Projects/ezansieedgeai
   ```

3. **Run the bootstrap tool**:
   ```bash
   python ~/Projects/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo .
   ```

4. **Review and commit the changes TO MAIN BRANCH**:
   ```bash
   git status
   git add .
   git commit -m "Bootstrap MaSf-vision framework"
   
   # ⚠️ IMPORTANT: Push to main/default branch!
   # Workflows must be on main branch to be available for workflow_dispatch
   git checkout main  # Switch to main if you're on a feature branch
   git push origin main
   ```

5. **Now you can run the workflow**:
   ```bash
   gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous
   ```

> **💡 Pro Tip**: If you get "HTTP 404" error when running the workflow, it's because GitHub Actions requires workflows to be on the main/default branch. Make sure you pushed to `main` not a feature branch!

### Method 2: Manual Copy (For Custom Setup)

If you want more control over what gets copied:

1. **Create necessary directories**:
   ```bash
   cd ~/Projects/ezansieedgeai
   mkdir -p .github/workflows
   mkdir -p .github/agents
   mkdir -p tools/agent-orchestration
   ```

2. **Copy the workflow files**:
   ```bash
   cp ~/Projects/MaSf-vision/.github/workflows/autonomous-agent-execution.yml .github/workflows/
   cp ~/Projects/MaSf-vision/.github/workflows/pr-evaluation.yml .github/workflows/
   cp ~/Projects/MaSf-vision/.github/workflows/adr-generation.yml .github/workflows/
   ```

3. **Copy the agent orchestration tools**:
   ```bash
   cp ~/Projects/MaSf-vision/tools/agent-orchestration/*.py tools/agent-orchestration/
   ```

4. **Copy the agent communication protocol**:
   ```bash
   cp ~/Projects/MaSf-vision/.github/agents/communication-protocol.md .github/agents/
   ```

5. **Commit and push TO MAIN BRANCH**:
   ```bash
   git add .
   git commit -m "Add MaSf-vision framework files"
   
   # ⚠️ CRITICAL: Push to main branch!
   git checkout main  # Make sure you're on main
   git push origin main
   ```

6. **Run the workflow**:
   ```bash
   gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous
   ```

## What Gets Set Up

After bootstrapping, your eZansiEdgeAI repository will have:

### Workflows (`.github/workflows/`)
- ✅ `autonomous-agent-execution.yml` - Main autonomous agent workflow
- ✅ `pr-evaluation.yml` - PR validation against your vision
- ✅ `adr-generation.yml` - Automatic architecture decision records

### Tools (`tools/agent-orchestration/`)
- ✅ `vision-task-extractor.py` - Extracts tasks from your vision
- ✅ `master-agent.py` - Master orchestration agent
- ✅ `agent-creator.py` - Creates specialized agents
- ✅ `pr-constitution-generator.py` - Generates PR rules from vision

### Agent Protocols (`.github/agents/`)
- ✅ `communication-protocol.md` - Agent communication standards
- ✅ `pr-merge-constitution.yaml` - Auto-generated PR rules (after first run)

## Verify Setup

After bootstrapping, verify everything is set up correctly:

```bash
# Check if workflow files exist
ls -la .github/workflows/autonomous-agent-execution.yml

# Check if tools exist
ls -la tools/agent-orchestration/

# Try to run the workflow
gh workflow list

# You should see "Autonomous Agent Execution" in the list
```

## Running the Workflow

Once set up, you can run autonomous execution:

```bash
# Full autonomous mode (planning + execution)
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous

# Just sprint planning
gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning

# Just execute tasks
gh workflow run autonomous-agent-execution.yml -f mode=execute-tasks

# Create ADRs
gh workflow run autonomous-agent-execution.yml -f mode=create-adr
```

## Workflow Modes Explained

### `full-autonomous`
Complete autonomous execution:
1. Reads your vision document
2. Extracts tasks and creates sprint plan
3. Executes tasks autonomously
4. Creates PRs with changes
5. Generates ADRs for decisions

### `sprint-planning`
Only generates sprint plan from vision:
- Analyzes `docs/product/vision.md`
- Creates task breakdown
- Outputs sprint plan

### `execute-tasks`
Execute existing tasks:
- Reads backlog from `docs/development/backlog-v1.md`
- Executes high-priority tasks
- Creates PRs for completed work

### `create-adr`
Generate Architecture Decision Records:
- Analyzes recent code changes
- Creates ADR documents
- Documents key decisions

## Troubleshooting

### Error: "workflow not found"
❌ Problem: Workflow file not in repository
✅ Solution: Run the bootstrap tool or manually copy workflows

### Error: "HTTP 404: Not Found" when running workflow  
❌ Problem: **Workflows must be on the main/default branch**
✅ Solution: 
```bash
# This is a common issue! GitHub Actions requires workflows to be 
# on the default branch (main/master) before workflow_dispatch works.

# If you're on a feature branch, push to main first:
git checkout main
git merge your-feature-branch  # or manually add the files
git push origin main

# Now the workflow will be available:
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous
```

**Root Cause**: GitHub only allows manual workflow execution (`workflow_dispatch`) on workflows that exist on the repository's default branch. Working on a feature branch? The workflow won't show up until it's merged to main!

### Error: "Python module not found"
❌ Problem: Missing dependencies in workflow
✅ Solution: The workflow installs `pyyaml` automatically, but check logs

### Error: "Permission denied"
❌ Problem: GitHub Actions doesn't have permissions
✅ Solution: Go to Settings → Actions → General → Workflow permissions → Set to "Read and write permissions"

### Error: "Vision document not found"
❌ Problem: No vision document in `docs/product/vision.md`
✅ Solution: Your README.md in the masf-vision branch already contains the vision. Either:
   - Move it to `docs/product/vision.md`, OR
   - Create a symbolic link, OR
   - The workflow will use README.md as fallback

## Next Steps

After successful setup:

1. **Test the workflow**:
   ```bash
   gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning
   gh run watch
   ```

2. **Review the output**:
   - Check the Actions tab in GitHub
   - Review any generated sprint plans or PRs

3. **Customize for your needs**:
   - Adjust workflow parameters
   - Modify agent instructions
   - Update PR constitution rules

## Vision Document Location

Your eZansiEdgeAI repository has the vision in `README.md`. The framework can use this, but for best results:

**Option 1** - Create standard location:
```bash
mkdir -p docs/product
cp README.md docs/product/vision.md
git add docs/product/vision.md
git commit -m "Add vision document in standard location"
git push
```

**Option 2** - The workflow will automatically use README.md if vision.md doesn't exist.

## Support

For more details, see:
- [Full Setup Guide](https://github.com/McFuzzySquirrel/MaSf-vision/blob/main/SETUP-AUTONOMOUS-AGENTS.md)
- [Framework Guide](https://github.com/McFuzzySquirrel/MaSf-vision/blob/main/FRAMEWORK-GUIDE.md)
- [MaSf-vision README](https://github.com/McFuzzySquirrel/MaSf-vision)

## Quick Command Reference

```bash
# Setup
python ~/Projects/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo .

# List workflows
gh workflow list

# Run workflow
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous

# Watch workflow execution
gh run watch

# View workflow runs
gh run list --workflow=autonomous-agent-execution.yml

# View specific run logs
gh run view <run-id>
```

---

**TL;DR**: Your eZansiEdgeAI repo needs the MaSf-vision framework files. Run the bootstrap tool:
```bash
cd ~/Projects/ezansieedgeai
python ~/Projects/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo .

# ⚠️ CRITICAL: Push to main branch (not a feature branch!)
git checkout main
git add . && git commit -m "Bootstrap MaSf-vision framework" && git push origin main

# Now you can run the workflow
gh workflow run autonomous-agent-execution.yml -f mode=full-autonomous
```

**Common Gotcha**: Workflows must be on the main/default branch to use `workflow_dispatch`. If you push to a feature branch, the workflow won't be available for manual execution!
