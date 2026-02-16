# Fixing "Deprecated artifact v3" Error

## The Issue You're Experiencing

You're getting this error:
```
This request has been automatically failed because it uses a deprecated version of `actions/upload-artifact: v3`
```

## Why This Is Happening

You're running a workflow that still uses the old v3 version of the artifact actions. This happens because:

1. **You bootstrapped from the main branch** which hasn't been updated yet
2. **OR** You're running an old cached version of the workflow in your repository

## The Fix (Choose One Method)

### Method 1: Update Your Workflow File Directly (Fastest)

In your eZansiEdgeAI repository:

```bash
cd ~/Projects/ezansieedgeai

# Edit the workflow file
nano .github/workflows/autonomous-agent-execution.yml
```

Make these two changes:
- **Line ~59**: Change `uses: actions/upload-artifact@v3` to `uses: actions/upload-artifact@v4`
- **Line ~198**: Change `uses: actions/download-artifact@v3` to `uses: actions/download-artifact@v4`

Then:
```bash
git add .github/workflows/autonomous-agent-execution.yml
git commit -m "Fix deprecated artifact actions: upgrade to v4"
git push origin main  # Push to main branch!
```

### Method 2: Copy Updated Workflow from This Branch

```bash
cd ~/Projects/ezansieedgeai

# Download the fixed workflow
curl -o .github/workflows/autonomous-agent-execution.yml \
  https://raw.githubusercontent.com/McFuzzySquirrel/MaSf-vision/copilot/fix-api-not-found-error/.github/workflows/autonomous-agent-execution.yml

# Commit and push to main
git add .github/workflows/autonomous-agent-execution.yml
git commit -m "Fix deprecated artifact actions: upgrade to v4"
git push origin main
```

### Method 3: Wait for PR Merge (Then Re-bootstrap)

Once this PR is merged to main:
```bash
cd ~/Projects/ezansieedgeai
python ~/Projects/MaSf-vision/tools/agent-orchestration/bootstrap.py --target-repo .
# This will copy the updated workflow
```

## Verification

After applying the fix, verify it worked:

```bash
# Check the workflow file
grep "artifact@" .github/workflows/autonomous-agent-execution.yml

# You should see:
# actions/upload-artifact@v4
# actions/download-artifact@v4
```

Then run the workflow again:
```bash
gh workflow run autonomous-agent-execution.yml -f mode=sprint-planning
```

It should now complete without the deprecation error!

## Why v3 Was Deprecated

GitHub deprecated v3 of the artifact actions in April 2024 because v4 has:
- Better performance
- Improved reliability
- Enhanced security features

All workflows using v3 are now automatically failed by GitHub Actions.

## Additional Context

The fix has been applied in this PR (`copilot/fix-api-not-found-error` branch) but hasn't been merged to the main branch yet. That's why users bootstrapping from main still get the old version.

Once this PR is merged, new users will automatically get the correct v4 version.
