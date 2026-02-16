# Quick Start Guide: Vision-Agnostic PR Validation

This guide shows you how to quickly set up vision-aware PR validation for your project.

## What This Does

The MaSf-vision PR validation system:
- ✅ Reads YOUR project's vision document
- ✅ Extracts your core principles automatically
- ✅ Generates a PR constitution tailored to your project
- ✅ Validates PRs against YOUR principles (not hardcoded ones)

## 5-Minute Setup

### Option 1: Using the Bootstrap Tool (Recommended)

If you're starting fresh or want to set up a new repository:

```bash
# Clone or navigate to your repository
cd your-repo

# Run the bootstrap tool
python /path/to/MaSf-vision/tools/agent-orchestration/bootstrap.py

# Follow the prompts
```

The bootstrap tool will:
1. Set up directory structure
2. Copy necessary tools
3. Create sample vision if needed
4. Generate your constitution
5. Set up workflows

### Option 2: Manual Setup

If you want more control:

```bash
# 1. Copy the necessary files
mkdir -p tools/agent-orchestration .github/workflows .github/agents
cp MaSf-vision/tools/agent-orchestration/pr-constitution-generator.py tools/agent-orchestration/
cp MaSf-vision/tools/agent-orchestration/master-agent.py tools/agent-orchestration/
cp MaSf-vision/.github/workflows/pr-evaluation.yml .github/workflows/

# 2. Create your vision document (if you don't have one)
mkdir -p docs/product
# Edit docs/product/vision.md with your project's vision

# 3. Generate your constitution
python tools/agent-orchestration/pr-constitution-generator.py
```

## Vision Document Structure

Your vision should include:

### Required Sections

```markdown
## Mission Statement
What you're trying to achieve

## Guiding Principles
1. **Principle 1**: Description
2. **Principle 2**: Description
3. **Principle 3**: Description
...

## Success Criteria
- Metric 1
- Metric 2
```

### Optional but Recommended

```markdown
## Constraints
- Technical constraint 1
- Resource constraint 2

## Goals
### Short Term
- Goal 1

### Long Term
- Goal 1
```

## Testing Your Setup

1. **Generate the constitution:**
   ```bash
   python tools/agent-orchestration/pr-constitution-generator.py
   ```

2. **Review the generated constitution:**
   ```bash
   cat .github/agents/pr-merge-constitution.yaml
   ```

3. **Create a test PR:**
   - Make a small change
   - Open a PR
   - Watch the workflow run

4. **Check the PR comments:**
   - You should see comments from the Constitutional Review
   - The principles should match YOUR vision
   - Not hardcoded education-specific principles

## Example: Education vs Healthcare

### Education Project Vision

```markdown
## Guiding Principles
1. **Learner First**: Every decision prioritizes learner experience
2. **Offline-First**: Works without connectivity
3. **Simple**: Easy to use with minimal training
```

**Generated Constitution Includes:**
- ✅ Learner-first checks
- ✅ Offline functionality validation
- ✅ Simplicity enforcement

### Healthcare Project Vision

```markdown
## Guiding Principles
1. **Patient Safety**: Never compromise patient safety
2. **Privacy**: HIPAA-compliant data handling
3. **Reliability**: 99.99% uptime requirement
```

**Generated Constitution Includes:**
- ✅ Patient safety validation
- ✅ Privacy compliance checks
- ✅ Reliability standards

## Customization

### After Generation

The generated constitution is a starting point. You can:

1. **Add domain-specific checks:**
   ```yaml
   core_principles:
     patient_safety:
       description: "Never compromise patient safety"
       enforcement: mandatory
       checks:
         - Implementation aligns with principle
         - Medical device standards followed
         - FDA compliance verified  # <-- Add custom checks
   ```

2. **Adjust enforcement levels:**
   ```yaml
   enforcement_levels:
     critical:
       applies_to:
         - core_principles
         - security
         - patient_safety  # <-- Add your critical items
   ```

3. **Add specific validations:**
   ```yaml
   technical_requirements:
     hipaa_compliance:  # <-- Add your requirements
       description: "Must be HIPAA compliant"
       checks:
         - Encryption at rest verified
         - Access logs implemented
   ```

## Regenerating

When your vision evolves:

```bash
# Update docs/product/vision.md with changes

# Regenerate constitution
python tools/agent-orchestration/pr-constitution-generator.py

# Review changes
git diff .github/agents/pr-merge-constitution.yaml

# Commit both vision and constitution together
git add docs/product/vision.md .github/agents/pr-merge-constitution.yaml
git commit -m "Update vision and regenerate constitution"
```

## Troubleshooting

### No Principles Extracted

**Problem:** Generated constitution has generic checks, not your principles.

**Solutions:**
- Check your vision has a "Guiding Principles" or "Principles" section
- Ensure principles are in a numbered or bulleted list
- Verify section heading contains word "principle"

Example that works:
```markdown
## Guiding Principles
1. **Principle 1**: Description
2. **Principle 2**: Description
```

### Wrong Domain Detected

**Problem:** Constitution says "domain: general" instead of your actual domain.

**Solutions:**
- Add more domain-specific keywords to your vision
- Explicitly mention your domain (healthcare, finance, education, etc.)
- The domain is for informational purposes - doesn't affect functionality

### Workflow Not Running

**Problem:** PR created but no constitutional review comment appears.

**Solutions:**
- Check `.github/workflows/pr-evaluation.yml` exists
- Verify workflow has proper permissions in GitHub Settings
- Check GitHub Actions tab for workflow execution status
- Ensure Python and PyYAML dependencies are available

## Advanced Usage

### Multiple Visions

For projects with sub-modules that have different visions:

```bash
# Generate constitution for sub-module
python tools/agent-orchestration/pr-constitution-generator.py \
    --repo-root ./sub-module \
    --output ./sub-module/.github/agents/pr-merge-constitution.yaml
```

### CI/CD Integration

Add to your CI pipeline:

```yaml
# In your .gitlab-ci.yml or .github/workflows/ci.yml
validate-pr:
  script:
    - python tools/agent-orchestration/pr-constitution-generator.py --dry-run
    - # Run additional validation
```

### Programmatic Access

Use the generator programmatically:

```python
from pr_constitution_generator import PRConstitutionGenerator

generator = PRConstitutionGenerator(repo_root='/path/to/repo')
constitution = generator.generate()

# Access the data
principles = constitution['core_principles']
for principle_id, data in principles.items():
    print(f"{principle_id}: {data['description']}")
```

## Best Practices

1. **Version Control**: Always commit vision and constitution together
2. **Review**: Review generated constitution before first use
3. **Iterate**: Start with basic vision, add details over time
4. **Document**: Note any manual customizations to constitution
5. **Communicate**: When regenerating, inform team of changes
6. **Test**: Create a test PR after setup to verify it works

## Getting Help

- See [PR Constitution Generator README](tools/agent-orchestration/README-pr-constitution.md)
- Check [MaSf-vision repository](https://github.com/McFuzzySquirrel/MaSf-vision)
- Review examples in `docs/product/vision.md`

## Next Steps

After setup:

1. ✅ Customize your vision document
2. ✅ Generate constitution
3. ✅ Open a test PR
4. ✅ Verify checks match your principles
5. ✅ Share with team
6. ✅ Iterate on vision as project evolves
