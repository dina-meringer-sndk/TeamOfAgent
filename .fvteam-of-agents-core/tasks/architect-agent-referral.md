<!-- Powered by FVTeamOfAgents Core -->

# Architect Agent Referral Task

## Purpose

Handle professional escalation to the Software Architect Agent when PlantUML validation reveals critical quality issues that require architectural expertise. This maintains quality gates and ensures proper resolution of design-level problems before proceeding with test code generation.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Issue Documentation and Analysis

- **Compile comprehensive issue report** from validation results
- **Categorize problems** by severity: critical, major, minor, advisory
- **Document specific examples** of each identified issue with context
- **Analyze impact** on test generation quality and project integration
- **Prepare clear recommendations** for architect review and resolution

### 2. Quality Gate Decision Documentation

- **Document rationale** for escalation decision based on validation criteria
- **Reference specific checklist items** that triggered escalation requirement
- **Explain potential consequences** of proceeding without resolution
- **Provide evidence** from project analysis supporting quality concerns
- **Create clear case** for architect intervention necessity

### 3. Professional Referral Communication

- **Generate formal referral document** with issue summary and recommendations
- **Provide context** about the test generation request and project scope
- **Include relevant PlantUML** and project information for architect review
- **Suggest specific areas** requiring architect attention and expertise
- **Offer to collaborate** in resolution process once architect provides guidance

### 4. User Communication and Guidance

- **Explain escalation necessity** to user with clear reasoning
- **Provide specific guidance** on approaching the Software Architect Agent
- **Suggest questions to ask** and information to provide to architect
- **Set expectations** for resolution timeline and process
- **Offer to resume** test generation once architect provides updated PlantUML

### 5. Process Suspension and Documentation

- **Formally suspend** test generation process until quality issues resolved
- **Document current state** and progress made before escalation
- **Preserve all analysis** and validation work for future resumption
- **Create handoff documentation** for smooth process continuation
- **Confirm user understanding** of next steps and escalation process

## Blocking Conditions

- Unable to generate comprehensive issue documentation
- User requests to proceed despite quality gate failures
- Communication channels to architect agent unavailable
- Critical issues that cannot be clearly articulated for architect review
- Missing context or information needed for effective referral

## Success Criteria

- Comprehensive issue documentation created with clear examples and impact analysis
- Professional referral communication generated with specific guidance for architect
- User properly informed about escalation necessity and next steps
- Test generation process appropriately suspended with preserved work state
- Clear path established for resumption after architect resolution

## Dependencies

This task depends on:
- Validation results from validate-plantuml-input.md
- plantuml-validation-checklist.md for quality criteria reference
- Quality gate failure documentation and evidence
- Project context and integration analysis from previous tasks

## Outputs

This task produces:
- Comprehensive issue report with severity analysis and specific examples
- Formal referral document for Software Architect Agent review
- User guidance document with escalation instructions and expectations
- Process suspension documentation with preserved work state
- Clear resumption criteria and procedures for post-architect resolution