<!-- Powered by FVTeamOfAgents Core -->

# Execute Verification Tests Task

## Purpose

Execute comprehensive self-verification of generated test code through compilation, test execution, and integration validation. This ensures all generated code functions correctly within the project environment before creating pull requests.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Compilation Verification

- **Attempt compilation** of all generated test files
- **Resolve compilation errors** by analyzing and fixing issues
- **Verify dependency resolution** and import correctness
- **Check framework compatibility** and version alignment
- **Confirm successful build** with no compilation warnings or errors

### 2. Test Execution Validation

- **Execute generated unit tests** using project's testing framework
- **Verify all tests pass** without failures or errors
- **Analyze test output** for proper assertion behavior and coverage
- **Check test execution time** for performance acceptability
- **Validate test isolation** and independence between test methods

### 3. Integration Testing

- **Run integration with existing test suite** to ensure no conflicts
- **Verify test discovery** by testing framework and build system
- **Check CI/CD compatibility** if applicable to project setup
- **Validate test categorization** and organization within existing structure
- **Ensure no interference** with existing test execution

### 4. Quality Validation

- **Apply comprehensive quality checks** using test-code-quality-checklist.md
- **Analyze code coverage** and test effectiveness
- **Review test scenarios** for completeness and edge case handling
- **Validate adherence** to project testing standards and conventions
- **Check documentation quality** and code comments

### 5. Issue Resolution

- **Identify and categorize** any issues discovered during verification
- **Implement fixes** for compilation, execution, or quality issues
- **Re-execute verification** after implementing fixes
- **Document any limitations** or known issues that cannot be resolved
- **Prepare status report** for successful verification or issue escalation

## Blocking Conditions

- Compilation failures that cannot be resolved
- Test execution failures indicating fundamental issues
- Integration conflicts with existing test suite
- Critical quality checklist failures
- Framework or dependency compatibility issues

## Success Criteria

- All generated test code compiles successfully without errors
- All generated tests execute and pass within acceptable time limits
- Integration with existing test suite completed without conflicts
- Comprehensive quality validation passed with acceptable results
- Verification report generated confirming readiness for delivery

## Dependencies

This task depends on:
- Generated test code from generate-test-code.md
- Project testing framework and build system setup
- test-code-quality-checklist.md for quality standards
- project-integration-checklist.md for integration validation
- testing-frameworks-knowledge.md for framework-specific execution

## Outputs

This task produces:
- Comprehensive verification report with execution results
- Quality validation summary with any identified issues
- Integration compatibility confirmation
- Performance analysis of test execution
- Confirmed test code ready for Git workflow and pull request creation