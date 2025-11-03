<!-- Powered by FVTeamOfAgents Core -->

# Git Workflow Guide

## Purpose

Step-by-step procedural guide for professional Git workflow execution when delivering generated test code. This guide provides specific Git commands, procedures, and best practices for seamless team collaboration and code integration.

## Git Workflow Procedures

### **Phase 1: Repository Preparation**

#### **Repository State Verification**
```
PROCEDURE: Pre-workflow Repository Check
1. Verify current repository status
   Command: git status
   Expected: Clean working directory with no uncommitted changes
   
2. Check current branch and synchronization
   Command: git branch -v
   Command: git remote -v
   Expected: Current branch identified, remote connections verified
   
3. Update local repository with remote changes
   Command: git fetch origin
   Command: git pull origin main  # or develop, depending on project
   Expected: Local repository synchronized with remote
   
4. Verify Git configuration
   Command: git config user.name
   Command: git config user.email
   Expected: Proper user identification configured
```

**Permission and Access Validation**
```
PROCEDURE: Access Rights Verification
1. Test repository write access
   Command: git ls-remote origin
   Expected: Successful connection and repository listing
   
2. Verify branch creation permissions
   Note: Attempt branch creation in test area if uncertain
   
3. Check team branching policies and restrictions
   - Review repository settings for branch protection
   - Understand required review processes
   - Verify naming convention requirements
   
4. Validate CI/CD integration requirements
   - Understand automated testing triggers
   - Review quality gate requirements
   - Check integration with project management tools
```

#### **Workspace Preparation**
```
PROCEDURE: Workspace Organization
1. Organize generated test files for inclusion
   - Verify file locations match project structure
   - Check file permissions and executable status
   - Remove any temporary or debug files
   - Validate file content completeness
   
2. Prepare commit scope and messaging
   - Identify all files to be included in commit
   - Prepare commit message following project conventions
   - Document test generation scope and coverage
   - Prepare PR description and metadata
   
3. Backup current work state
   Command: git stash push -m "Backup before test generation workflow"
   Purpose: Safety backup for recovery if needed
```

### **Phase 2: Branch Creation and Management**

#### **Branch Creation Procedures**
```
PROCEDURE: Feature Branch Creation
1. Ensure clean working directory
   Command: git status
   Expected: No uncommitted changes
   
2. Create feature branch with descriptive name
   Command: git checkout -b feature/test-generation-[module-name]-[date]
   Example: git checkout -b feature/test-generation-payment-processor-20231103
   Alternative: git switch -c feature/test-generation-[module-name]
   
3. Verify branch creation and checkout
   Command: git branch
   Expected: New branch created and currently checked out (marked with *)
   
4. Set up remote tracking (if required)
   Command: git push -u origin feature/test-generation-[module-name]
   Purpose: Establish remote tracking for collaboration
```

**Branch Naming Conventions**
```
NAMING STANDARDS:
Standard Format: [type]/[scope]-[description]-[optional-date]

Common Types:
- feature/    : New functionality or test generation
- bugfix/     : Bug fixes or test corrections  
- hotfix/     : Critical fixes requiring immediate attention
- refactor/   : Code restructuring or test improvement

Examples:
- feature/test-generation-user-authentication
- feature/tests-payment-processing-module
- bugfix/test-validation-edge-cases
- refactor/test-organization-cleanup

Project-Specific Conventions:
[Document specific naming requirements for your project]
```

#### **Branch Validation and Safety**
```
PROCEDURE: Branch Safety Verification
1. Confirm branch isolation
   Command: git log --oneline -5
   Expected: Clean branch history starting from base branch
   
2. Verify no unintended files included
   Command: git ls-files
   Purpose: Ensure only intended files are tracked
   
3. Test branch switching
   Command: git checkout main  # Switch to main
   Command: git checkout feature/your-branch-name  # Switch back
   Expected: Clean switching without errors
   
4. Validate branch permissions and policies
   - Check if branch name follows project conventions
   - Verify compliance with team branching strategies
   - Ensure branch creation aligns with project workflow
```

### **Phase 3: Commit Process**

#### **File Staging and Commit Preparation**
```
PROCEDURE: Commit Content Preparation
1. Review all changes and additions
   Command: git diff --cached  # Review staged changes
   Command: git diff  # Review unstaged changes
   Command: git status  # Overview of all changes
   
2. Stage generated test files systematically
   Command: git add src/test/java/com/example/PaymentProcessorTest.java
   Command: git add src/test/java/com/example/UserAuthenticationTest.java
   # Add each file individually for precision
   
3. Verify staged content
   Command: git diff --cached
   Expected: Only intended test files and changes staged
   
4. Check for accidentally included files
   Command: git status
   Look for: Temporary files, IDE files, personal configurations
   Remove if found: git reset HEAD unwanted-file.txt
```

**Commit Message Creation**
```
PROCEDURE: Professional Commit Message Writing
Format Template:
[Type]: [Brief description in imperative mood]

[Optional longer description explaining what and why]

- Generated tests for [specific modules/classes]
- Coverage includes [types of tests: unit/integration/edge cases]
- PlantUML source: [reference to source diagram]
- Framework: [testing framework used]
- Integration: [compatibility notes]

Example Commit Message:
feat: Generate comprehensive test suite for PaymentProcessor module

Generated complete test coverage for payment processing functionality
including unit tests, edge cases, and error condition validation.

- Generated tests for PaymentProcessor, PaymentValidator, and PaymentGateway classes
- Coverage includes happy path, boundary conditions, and exception scenarios  
- PlantUML source: payment-processing-v2.1.puml
- Framework: JUnit 5 with Mockito for mocking
- Integration: Compatible with existing test suite structure
```

#### **Commit Execution and Validation**
```
PROCEDURE: Commit Creation and Verification
1. Create commit with descriptive message
   Command: git commit -m "feat: Generate test suite for [module]
   
   [Additional description lines]"
   
   Alternative multi-line approach:
   Command: git commit
   # Opens editor for detailed commit message composition
   
2. Verify commit creation
   Command: git log --oneline -1
   Expected: New commit appears with correct message
   
3. Validate commit content
   Command: git show HEAD --stat
   Expected: Only intended files included with appropriate change statistics
   
4. Check commit integrity
   Command: git fsck
   Expected: No repository integrity issues
```

### **Phase 4: Pull Request Creation**

#### **Remote Push Procedures**
```
PROCEDURE: Branch Push to Remote Repository
1. Push branch to remote repository
   Command: git push origin feature/test-generation-[module-name]
   Expected: Successful push without conflicts
   
2. Verify remote branch creation
   Command: git ls-remote origin | grep feature/test-generation
   Expected: New branch visible in remote repository
   
3. Set up branch tracking (if not done during creation)
   Command: git branch --set-upstream-to=origin/feature/test-generation-[module-name]
   Purpose: Enable easy future pushes and pulls
   
4. Validate push success
   # Check repository web interface for new branch
   # Verify all commits pushed successfully
   # Confirm file content accuracy in remote repository
```

**Pull Request Preparation**
```
PROCEDURE: PR Creation and Documentation
1. Navigate to repository web interface (GitHub, GitLab, etc.)
   
2. Create new pull request from feature branch
   - Source branch: feature/test-generation-[module-name]
   - Target branch: main (or develop, per project convention)
   
3. Complete PR title and description using template:

Title: Generate comprehensive test suite for [Module Name]

Description Template:
## Summary
Generated comprehensive test coverage for [specific modules] based on PlantUML specifications.

## Changes Made
- Generated test classes: [list of test classes]
- Test coverage includes: [types of scenarios covered]
- Framework integration: [testing framework and patterns used]
- Project integration: [compatibility and integration notes]

## PlantUML Source
- Source diagram: [filename or reference]
- Validation status: [passed/issues resolved]
- Architect review: [if applicable]

## Testing and Validation
- All generated tests pass: ✓
- Integration with existing test suite verified: ✓
- Code quality standards met: ✓
- Performance impact assessed: ✓

## Review Notes
- Generated code follows project conventions
- Test scenarios cover business requirements
- Integration approach maintains architectural integrity
- Maintenance considerations documented

## Related Issues
[Link any related tickets, user stories, or issues]
```

#### **PR Metadata and Configuration**
```
PROCEDURE: PR Configuration and Assignment
1. Apply appropriate labels
   - test-generation
   - enhancement  
   - [module-specific-label]
   - auto-generated (if applicable)
   
2. Assign reviewers
   - Primary reviewer: [team lead or senior developer]
   - Secondary reviewer: [domain expert if applicable]
   - Architect reviewer: [if architectural changes involved]
   
3. Set milestone and project assignment
   - Milestone: [current sprint or release]
   - Project board: [add to appropriate project]
   
4. Configure merge settings
   - Merge strategy: [squash/merge/rebase per project preference]
   - Delete branch after merge: [yes/no per project policy]
   - Required status checks: [ensure CI/CD requirements met]
```

### **Phase 5: Post-Creation Procedures**

#### **Documentation and Handoff**
```
PROCEDURE: Completion Documentation
1. Generate workflow summary document
   - PR link and access information
   - Review process guidance for reviewers
   - Integration notes and special considerations
   - Merge timeline and dependencies
   
2. Notify relevant stakeholders
   - Development team notification
   - Architect notification (if applicable)
   - Project management updates
   - Documentation updates required
   
3. Monitor PR progress
   - Track review feedback and comments
   - Respond to reviewer questions and requests
   - Monitor automated testing and validation
   - Address any integration issues discovered
```

**Quality Assurance and Validation**
```
PROCEDURE: Workflow Quality Verification
1. Validate Git workflow completion
   Command: git log --graph --oneline -10
   Expected: Clean commit history with proper branch management
   
2. Verify PR creation and accessibility
   - Confirm PR visible and accessible to team
   - Validate all metadata and assignments correct
   - Check automated testing trigger success
   - Verify documentation completeness
   
3. Confirm integration readiness
   - All quality gates passed
   - No merge conflicts present
   - CI/CD pipeline execution successful
   - Team notification completed appropriately
```

## Git Command Reference

### **Essential Git Commands for Test Generation Workflow**

#### **Repository Management**
```
# Repository status and information
git status                          # Check working directory status
git branch -v                       # List branches with last commit info
git remote -v                       # List remote repositories
git log --oneline -10               # Recent commit history

# Repository synchronization  
git fetch origin                    # Fetch remote changes
git pull origin main                # Pull changes from main branch
git push origin branch-name         # Push branch to remote
```

#### **Branch Operations**
```
# Branch creation and management
git checkout -b feature/branch-name # Create and switch to new branch
git switch -c feature/branch-name   # Alternative branch creation syntax
git branch                          # List all local branches
git branch -r                       # List remote branches
git checkout main                   # Switch to main branch
git branch -d feature/branch-name   # Delete local branch (after merge)
```

#### **Commit Operations**
```
# File staging and committing
git add file1.java file2.java      # Stage specific files
git add src/test/                   # Stage directory
git diff --cached                   # Review staged changes
git commit -m "Commit message"      # Commit with message
git commit                          # Commit with editor for detailed message
git show HEAD                       # Show last commit details
```

#### **Remote Operations**
```
# Remote repository interaction
git push origin feature/branch-name # Push new branch
git push -u origin feature/branch   # Push and set upstream tracking
git ls-remote origin                # List remote references
git remote show origin              # Show remote repository information
```

## Troubleshooting Common Issues

### **Common Git Workflow Problems**

#### **Permission and Access Issues**
```
PROBLEM: Permission denied or authentication failures
SOLUTIONS:
1. Verify SSH key setup: ssh -T git@github.com
2. Check HTTPS authentication: git config credential.helper
3. Validate repository access permissions with team lead
4. Refresh authentication tokens if using token-based auth
```

#### **Merge Conflicts and Branch Issues**
```
PROBLEM: Merge conflicts or branch synchronization issues
SOLUTIONS:
1. Update local repository: git fetch origin && git pull origin main
2. Rebase feature branch: git rebase origin/main
3. Resolve conflicts manually and continue: git add . && git rebase --continue
4. Alternative: merge approach: git merge origin/main
```

#### **Commit and Push Problems**
```
PROBLEM: Commit or push failures
SOLUTIONS:
1. Check file permissions: ls -la affected-files
2. Verify file content and encoding: file filename
3. Check repository status: git status && git fsck
4. Reset and retry: git reset --soft HEAD~1 (to undo last commit)
```

### **Recovery Procedures**

#### **Workflow Recovery Commands**
```
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) - USE WITH CAUTION
git reset --hard HEAD~1

# Recover from stash
git stash list
git stash apply stash@{0}

# Create recovery branch from specific commit
git checkout -b recovery/branch-name commit-hash
```

## Best Practices Summary

### **Professional Git Workflow Standards**
- Always verify repository state before starting workflow
- Use descriptive, consistent branch names following project conventions  
- Create atomic commits with clear, detailed commit messages
- Test branch isolation and verify staged content before committing
- Document PR thoroughly with clear description and context
- Monitor workflow completion and address issues promptly

### **Quality Assurance Guidelines**
- Validate all Git commands before execution, especially destructive operations
- Maintain clean commit history and branch management
- Ensure PR creation follows team standards and review requirements
- Document workflow decisions and rationale for future reference
- Test integration and compatibility before finalizing workflow