# Task: revise-agent

## Purpose
Guide the user through revising an existing agent, updating its structure and files as needed while maintaining BMAD compliance.

## Prerequisites
- Existing agent to revise
- Clear revision requirements
- Understanding of current agent structure

## Steps

### 1. Agent Selection and Analysis
- List all available agents in numbered format
- Allow user to select agent to revise
- Analyze current agent structure and capabilities
- Identify key components (prompt, tasks, templates, etc.)

### 2. Revision Requirements Gathering
- Determine specific aspects that need updating:
  - **Prompt modifications**: Persona, commands, behavior changes
  - **Task updates**: New workflows, modified processes
  - **Template changes**: Output format modifications
  - **Command additions/modifications**: New user interactions
  - **Tool integrations**: Additional utilities or dependencies
  - **Knowledge base updates**: New data or references

### 3. Impact Assessment
- Analyze how changes affect existing functionality
- Identify dependencies and potential conflicts
- Plan migration strategy for existing data/outputs
- Consider backward compatibility requirements

### 4. Focused Brainstorming Session
- Explore revision options and alternatives
- Consider implementation approaches
- Validate changes against BMAD principles
- Refine requirements based on discussion

### 5. Implementation Planning
- Create detailed implementation plan
- Prioritize changes by importance and complexity
- Identify validation criteria for each change
- Plan testing and verification approach

### 6. File Structure Updates
- Backup existing agent structure
- Update agent prompt file with new specifications
- Modify or create new task files as needed
- Update templates and checklists
- Add new utilities or commands if required

### 7. Documentation and Validation
- Update all README files to reflect changes
- Generate revision summary in both .md and .docx formats
- Validate changes against agent creation checklist
- Test updated agent functionality

### 8. Completion and Handoff
- Provide clear summary of all changes made
- Document any breaking changes or migration notes
- Offer guidance for testing and validation
- Save revision documentation in agent folder

## Output Requirements
- **Revision Summary**: Comprehensive document in both Markdown and Word formats
- **Change Log**: Detailed list of modifications made
- **Migration Notes**: Guidelines for transitioning to updated agent
- **Updated Documentation**: All README and help files current

## Quality Validation
- [ ] All changes maintain BMAD compliance
- [ ] Agent functionality verified and tested
- [ ] Documentation updated and accurate
- [ ] Backup of original agent preserved
- [ ] Revision summary generated in both formats
- [ ] User provided with clear next steps

## Dependencies
- Access to existing agent files
- `facilitate-brainstorming-session.md` task
- `agent-summary-tmpl.md` and `.docx` templates
- `docx_utils.py` for document generation
- Agent creation checklist for validation