<!-- Powered by FVTeamOfAgents Core -->

# FVTeamOfAgents Compliance Checklist

## Purpose

Verify that created agents fully comply with FVTeamOfAgents framework standards and patterns.

## When to Use

Execute this checklist during agent creation validation to ensure framework compliance.

## Prerequisites

- Agent ecosystem has been created
- All core files are in place
- Agent structure follows FVTeamOfAgents patterns

## Checklist Items

### Framework Structure
- [ ] Uses `.bmad-core/` root directory structure
- [ ] Has proper folder organization: agents/, tasks/, templates/, checklists/, data/, utils/
- [ ] Agent prompt file is in `.bmad-core/agents/` directory
- [ ] All supporting files are in correct subdirectories

### Agent Prompt File Standards
- [ ] Starts with `<!-- Powered by FVTeamOfAgents Core -->` header
- [ ] Contains ACTIVATION-NOTICE section
- [ ] Includes complete YAML configuration block
- [ ] Has IDE-FILE-RESOLUTION section with proper patterns
- [ ] Has REQUEST-RESOLUTION section for flexible command mapping
- [ ] Contains standard activation-instructions with all required steps
- [ ] Agent definition includes name, id, title, icon, whenToUse
- [ ] Persona section defines role, style, identity, focus
- [ ] Core principles are clearly stated
- [ ] Commands use * prefix requirement
- [ ] Dependencies section properly maps to file structure

### Task File Standards
- [ ] Tasks start with `<!-- Powered by FVTeamOfAgents Core -->` header
- [ ] Have clear purpose and sequential execution structure
- [ ] Include blocking conditions and success criteria
- [ ] Use proper elicitation patterns (elicit=true) where needed
- [ ] Reference templates and dependencies correctly
- [ ] Follow FVTeamOfAgents task workflow patterns

### Template File Standards
- [ ] Templates start with `<!-- Powered by FVTeamOfAgents Core -->` header
- [ ] Use proper YAML structure with template metadata
- [ ] Include workflow configuration for elicitation
- [ ] Have structured sections with proper types
- [ ] Include variable substitution patterns
- [ ] Specify output format and file naming
- [ ] Include elicitation markers where user input required

### Checklist File Standards
- [ ] Checklists start with `<!-- Powered by FVTeamOfAgents Core -->` header
- [ ] Have clear purpose and when-to-use sections
- [ ] Include prerequisites and validation criteria
- [ ] Use proper checkbox format for items
- [ ] Include failure actions and completion criteria
- [ ] Follow FVTeamOfAgents checklist structure patterns

### Data File Standards
- [ ] Data files start with `<!-- Powered by FVTeamOfAgents Core -->` header
- [ ] Have clear overview and purpose sections
- [ ] Include examples and references
- [ ] Provide maintenance information
- [ ] Follow FVTeamOfAgents knowledge base patterns

### Command Integration
- [ ] All commands require * prefix in usage
- [ ] Commands directly execute corresponding task files
- [ ] Command descriptions match actual functionality
- [ ] Help command shows numbered options
- [ ] Exit command properly abandons persona

### Dependency Management
- [ ] All dependencies are properly mapped to .bmad-core structure
- [ ] File references use correct paths and naming
- [ ] Templates are correctly referenced by tasks
- [ ] Checklists are properly integrated into workflows
- [ ] Utils are included in dependencies and accessible

### Core Configuration Integration
- [ ] Agent loads core-config.yaml during activation
- [ ] Respects devLoadAlwaysFiles patterns if applicable
- [ ] Follows proper activation sequence
- [ ] Maintains FVTeamOfAgents workflow rules and interaction patterns

### Documentation Standards
- [ ] All files include proper FVTeamOfAgents headers
- [ ] Documentation is comprehensive and accurate
- [ ] Usage instructions are clear
- [ ] File purposes are well explained
- [ ] Extension points are identified

## Validation Criteria

- Agent follows all FVTeamOfAgents structural patterns
- File naming and organization meet framework standards
- YAML syntax is valid and properly structured
- Markdown formatting follows FVTeamOfAgents conventions
- Dependencies are correctly mapped and accessible
- Agent activates and functions as expected

## Actions on Failure

- Identify specific compliance violations
- Update files to meet FVTeamOfAgents standards
- Re-validate structure and content
- Test agent activation and functionality
- Document any necessary framework variations

## Completion

All compliance items are verified, agent meets FVTeamOfAgents framework standards, and is ready for deployment in FVTeamOfAgents-compatible environments.