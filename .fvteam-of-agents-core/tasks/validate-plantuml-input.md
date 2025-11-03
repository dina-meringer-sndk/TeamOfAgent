<!-- Powered by FVTeamOfAgents Core -->

# Validate PlantUML Input Task

## Purpose

Systematically validate PlantUML class diagrams for syntax correctness, semantic completeness, and integration compatibility with the existing project. This critical quality gate prevents generation of problematic test code by identifying issues that require architect intervention.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Syntax Validation

- **Parse PlantUML syntax** using plantuml-validation-guide.md procedures
- **Verify class definitions** are syntactically correct and complete
- **Check relationship syntax** for inheritance, associations, and dependencies
- **Validate attribute and method** declarations for correct format
- **Report syntax errors** with specific line numbers and correction suggestions

### 2. Semantic Analysis

- **Analyze class relationships** for logical consistency and completeness
- **Verify method signatures** include appropriate parameters and return types
- **Check for missing dependencies** or undefined class references
- **Validate business logic** representation against domain knowledge
- **Identify incomplete specifications** requiring clarification

### 3. Project Integration Validation

- **Compare against existing codebase** patterns and conventions
- **Check naming consistency** with project standards
- **Verify architectural alignment** with existing design patterns
- **Identify potential conflicts** with existing classes or interfaces
- **Assess integration complexity** and potential issues

### 4. Existing Code Conflict Detection

- **Cross-reference PlantUML classes** against existing code inventory from project knowledge base
- **Identify overlapping functionality**: classes/methods that already exist in the codebase
- **Evaluate reusability potential**: can existing code be extended instead of creating new?
- **Apply decision framework**: determine extend vs create vs hybrid approach for each component
- **Flag conflicts for clarification**: when PlantUML specifies creating existing functionality
- **Generate recommendations**: specific guidance on reusing vs replacing existing code
- **Document integration strategy**: how new code will interact with existing utilities

### 5. Quality Gate Decision

- **Apply plantuml-validation-checklist.md** for comprehensive quality assessment
- **Determine PROCEED or ESCALATE** based on validation results
- **Document all issues found** with severity levels and recommendations
- **Generate validation report** for user review and decision
- **Provide specific guidance** for issue resolution if escalation needed

### 5. Issue Communication

- **Present validation results** in clear, actionable format
- **Explain impact of issues** on test code generation quality
- **Provide specific recommendations** for architect consultation if needed
- **Offer alternative approaches** when possible for minor issues
- **Ensure user understanding** before proceeding or escalating

## Blocking Conditions

- Malformed or unparseable PlantUML syntax
- Critical semantic errors that prevent code generation
- Major conflicts with existing project architecture
- Missing essential class or method information
- Validation checklist failures indicating quality risks

## Success Criteria

- PlantUML input completely validated for syntax and semantics
- All potential integration issues identified and assessed
- Clear PROCEED or ESCALATE decision made with supporting rationale
- Comprehensive validation report generated with actionable recommendations
- User informed of validation results and next steps

## Dependencies

This task depends on:
- Project knowledge base from learn-project-context.md (including existing code inventory)
- plantuml-validation-guide.md for validation procedures
- plantuml-validation-checklist.md for quality assessment criteria
- project-integration-checklist.md for compatibility verification
- brownfield-integration-patterns.md for conflict detection

## Outputs

This task produces:
- PlantUML validation report with syntax and semantic analysis
- Existing code conflict analysis and reusability recommendations
- Quality gate decision (PROCEED/ESCALATE) with detailed rationale
- Issue documentation with severity levels and recommendations
- Integration strategy recommendations (extend vs create vs hybrid)
- Integration compatibility assessment
- Architect referral documentation if escalation required