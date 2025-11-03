<!-- Powered by FVTeamOfAgents Core -->

# Generate Test Code Task

## Purpose

Generate high-quality test code from validated PlantUML diagrams using project-specific patterns, conventions, and frameworks. This produces test code that seamlessly integrates with existing brownfield projects while maintaining professional quality standards.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Test Generation Planning

- **Review validated PlantUML** and clarified requirements from previous tasks
- **Load project knowledge base** with patterns, conventions, and framework details
- **Plan test structure** based on existing project testing organization
- **Identify test categories** needed: unit tests, integration tests, specific scenarios
- **Create generation roadmap** with file organization and naming conventions

### 2. Test Class Structure Generation

- **Generate test class templates** following project naming conventions
- **Apply appropriate base classes** and framework patterns from project analysis
- **Create proper imports** and dependencies based on project structure
- **Implement setup and teardown** methods following existing patterns
- **Generate class-level documentation** consistent with project standards

### 3. Test Method Implementation

- **Generate test methods** for each public method and significant functionality
- **Create meaningful test scenarios**: happy path, edge cases, error conditions
- **Implement proper assertions** using project's testing framework patterns
- **Generate test data** and mock objects following project conventions
- **Apply business logic validation** based on domain knowledge

### 4. Quality Enhancement

- **Apply test-code-quality-checklist.md** for comprehensive quality verification
- **Ensure code coverage** of critical functionality and edge cases
- **Validate test independence** and proper isolation between tests
- **Check performance considerations** for test execution efficiency
- **Review integration patterns** for compatibility with existing test suites

### 5. Code Integration and Formatting

- **Format generated code** according to project style guidelines
- **Organize imports** and dependencies following project conventions
- **Add appropriate comments** and documentation consistent with codebase
- **Ensure proper package structure** and file organization
- **Validate compilation readiness** before proceeding to verification

### 6. Incremental Version Control

- **Create incremental commits** for logical generation milestones (e.g., after each test class)
- **Use meaningful commit messages** describing the specific functionality implemented
- **Track progress** through Git history for transparency and rollback capability
- **Save intermediate work** to prevent loss during extended generation sessions
- **Enable early collaboration** by pushing intermediate commits for team visibility

## Blocking Conditions

- Missing or incomplete project knowledge base
- Unresolved issues from validation or clarification phases
- Testing framework incompatibilities or unsupported features
- Critical project pattern conflicts that cannot be resolved
- Insufficient PlantUML specifications for meaningful test generation

## Success Criteria

- Complete test code generated following all project patterns and conventions
- All test methods properly implemented with appropriate scenarios and assertions
- Generated code passes initial quality checklist validation
- Test structure seamlessly integrates with existing project organization
- Code ready for compilation and execution verification

## Dependencies

This task depends on:
- Validated PlantUML from validate-plantuml-input.md
- Project knowledge base from learn-project-context.md
- Clarified requirements from interactive-clarification-session.md
- test-code-quality-checklist.md for quality standards
- code-quality-standards.md for detailed quality criteria
- testing-frameworks-knowledge.md for framework-specific implementation

## Outputs

This task produces:
- Complete test code files organized according to project structure
- Generated test classes with comprehensive method coverage
- Properly formatted and documented test code
- Integration-ready test files following project conventions
- Quality-validated test implementation ready for verification