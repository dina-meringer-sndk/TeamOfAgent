<!-- Powered by FVTeamOfAgents Core -->

# Agent Creation Checklist

## Purpose

Ensure complete and proper creation of FVTeamOfAgents agent ecosystems with all required files and structures.

## When to Use

Execute this checklist after completing the agent creation process to validate that all components have been properly generated and configured.

## Prerequisites

- Agent creation task has been completed
- All files have been generated in the .bmad-core structure
- Brainstorming session requirements are available

## Checklist Items

### Agent Prompt File
- [ ] Agent .md file created in `.bmad-core/agents/`
- [ ] File follows FVTeamOfAgents agent structure (IDE-FILE-RESOLUTION, activation-instructions, etc.)
- [ ] Agent name, ID, title, and icon are properly defined
- [ ] Persona section is complete and accurate
- [ ] Core principles are clearly defined
- [ ] All commands are listed with proper descriptions
- [ ] Dependencies section lists all required files
- [ ] YAML structure is valid and complete

### Task Files
- [ ] All identified workflows have corresponding task .md files
- [ ] Task files are located in `.bmad-core/tasks/`
- [ ] Each task has clear purpose and sequential execution steps
- [ ] Blocking conditions and success criteria are defined
- [ ] Tasks reference appropriate templates and dependencies
- [ ] Elicitation patterns are included where user interaction required

### Template Files
- [ ] All content generation needs have corresponding template .yaml files
- [ ] Templates are located in `.bmad-core/templates/`
- [ ] Each template has proper FVTeamOfAgents structure with sections
- [ ] Variable substitution patterns are defined
- [ ] Elicitation patterns are included for user input
- [ ] Output formats and file naming are specified

### Checklist Files
- [ ] All validation needs have corresponding checklist .md files
- [ ] Checklists are located in `.bmad-core/checklists/`
- [ ] Each checklist has clear purpose and validation criteria
- [ ] Prerequisites and when-to-use sections are defined
- [ ] Checklist items are comprehensive and actionable
- [ ] Failure actions are specified

### Data Files
- [ ] All knowledge base needs have corresponding data .md files
- [ ] Data files are located in `.bmad-core/data/`
- [ ] Each data file has clear overview and purpose
- [ ] Content is well-organized with examples
- [ ] References and maintenance information included

### Utility Files
- [ ] All file operations have corresponding utility .py files
- [ ] Utilities are located in `.bmad-core/utils/`
- [ ] Each utility has proper function definitions
- [ ] Documentation and error handling included
- [ ] Dependencies and imports are specified

### Documentation
- [ ] Agent creation summary generated
- [ ] Summary includes all design decisions and rationale
- [ ] Usage instructions are clear and complete
- [ ] File structure is documented
- [ ] Extension points are identified

### Integration
- [ ] Agent dependencies correctly reference created files
- [ ] Task workflows properly use templates
- [ ] Commands correctly map to task executions
- [ ] All file paths and references are accurate

## Validation Criteria

- All required files exist in correct locations
- File naming follows FVTeamOfAgents conventions
- YAML syntax is valid in all template files
- Markdown structure is proper in all .md files
- Dependencies are correctly mapped
- Agent can be loaded without errors

## Actions on Failure

- Identify missing or incorrect files
- Re-run appropriate generation steps
- Validate file contents and structure
- Test agent loading and command execution
- Update documentation if changes made

## Completion

All checklist items are marked complete, validation criteria are met, and the agent ecosystem is ready for use.
