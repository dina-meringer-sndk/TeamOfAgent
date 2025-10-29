<!-- Powered by FVTeamOfAgents Core -->
# Create Agent Task

## Purpose

To create a complete BMAD agent ecosystem including agent prompt file, supporting tasks, templates, checklists, data files, and utilities. This task ensures the new agent follows BMAD framework patterns and includes all necessary supporting infrastructure.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Load Core Configuration and Initialize

- Load `.bmad-core/core-config.yaml` from the project root
- If the file does not exist, HALT and inform the user: "core-config.yaml not found. This file is required for agent creation. Please add and configure core-config.yaml before proceeding."
- Get target directory from brainstorming session requirements
- **Check for existing .bmad-core structure at user-specified path:**
  - If exists: Analyze existing files and folders
  - If missing: Create complete structure
- Create agent working directory structure at user-specified path:
  ```
  {user_target_path}/.bmad-core/
  ├── agents/
  ├── tasks/
  ├── templates/
  ├── checklists/
  ├── data/
  └── utils/
  ```

### 2. Analyze Existing Files (if .bmad-core exists)

- **Scan existing structure for:**
  - Existing task files in `/tasks/` folder
  - Existing template files in `/templates/` folder
  - Existing checklist files in `/checklists/` folder
  - Existing data files in `/data/` folder
  - Existing utility files in `/utils/` folder
- **Create inventory of existing files to avoid conflicts**
- **Identify reusable components** that don't need recreation

### 2. Conduct Brainstorming Session

- Execute task `facilitate-brainstorming-session.md` to gather comprehensive requirements
- Ensure all required information is collected:
  - Agent purpose and role
  - Workflows the agent will execute
  - Content the agent will generate
  - Validation/quality control needs
  - Knowledge bases required
  - File operations needed
  - External tools/APIs required

### 3. Generate Agent Prompt File

- **Check for existing agent file**: `{user_target_path}/.bmad-core/agents/{agent_id}.md`
- **If exists**: Ask user "Agent file already exists. Overwrite, rename, or skip?"
- Use template `agent-prompt-tmpl.yaml` to create the main agent .md file
- Location: `{user_target_path}/.bmad-core/agents/{agent_id}.md`
- Ensure proper BMAD structure with all required sections
- Include all dependencies identified in brainstorming

### 4. Generate Supporting Task Files

- For each workflow identified in brainstorming:
  - **Check for existing task file**: `{user_target_path}/.bmad-core/tasks/{workflow-name}.md`
  - **If exists**: Ask user "Task '{workflow-name}' already exists. Overwrite, rename, reuse, or skip?"
  - **If reuse**: Add to agent dependencies without recreating
  - Use template `task-file-tmpl.yaml` to create task .md file
  - Location: `{user_target_path}/.bmad-core/tasks/{workflow-name}.md`
  - Include proper task structure with sequential steps
  - Add elicitation patterns where user interaction required

### 5. Generate Template Files

- For each content type the agent will generate:
  - Use template `content-template-tmpl.yaml` to create template .yaml file
  - Location: `{user_target_path}/.bmad-core/templates/{content-type}-tmpl.yaml`
  - Include proper sections, elicitation, and variable substitution
- Create data file template if agent manages knowledge:
  - Use template `data-file-tmpl.yaml`
  - Location: `{user_target_path}/.bmad-core/templates/{data-type}-tmpl.yaml`

### 6. Generate Checklist Files

- For each validation need identified:
  - Use template `checklist-file-tmpl.yaml` to create checklist .md file
  - Location: `{user_target_path}/.bmad-core/checklists/{validation-name}-checklist.md`
  - Include comprehensive validation steps and criteria

### 7. Generate Data/Knowledge Files

- For each knowledge base identified:
  - Use template `data-file-tmpl.yaml` to create data .md file
  - Location: `{user_target_path}/.bmad-core/data/{knowledge-topic}.md`
  - Include relevant reference information and examples

### 8. Generate Utility Files

- For each file operation identified:
  - Create utility .py file with basic structure
  - Location: `{user_target_path}/.bmad-core/utils/{operation}_utils.py`
  - Include function stubs and documentation

### 9. Generate Documentation Summary

- Use template `agent-summary-tmpl.yaml` to create comprehensive summary
- Include all design decisions, file purposes, and usage instructions
- Save as both .md and .docx formats

### 10. Validate Complete Ecosystem

- Execute validation using checklist `agent-creation-checklist.md`
- Verify all files created and properly structured
- Confirm BMAD compliance using checklist `quality-compliance-checklist.md`
- Test that agent can be loaded without errors

### 11. Final Handoff

- Present complete file structure to user
- Provide usage instructions for the new agent
- Explain how to extend or modify the agent ecosystem
- Save all creation artifacts for future reference

## Blocking Conditions

- Missing core-config.yaml
- Incomplete brainstorming session (missing required information)
- Template generation failures
- BMAD compliance validation failures
- File creation permissions issues

## Success Criteria

- Complete agent ecosystem created with all supporting files
- Agent follows BMAD framework patterns
- All validation checklists pass
- Documentation is comprehensive and accurate
- Agent can be activated and used immediately

## Files Created

This task will create a complete ecosystem including:
- 1 agent prompt file (.md)
- N task files (.md) based on workflows
- N template files (.yaml) based on content generation needs
- N checklist files (.md) based on validation needs
- N data files (.md) based on knowledge requirements
- N utility files (.py) based on file operations
- 1 comprehensive summary (.md and .docx)ate-agent

## Purpose
Guide the user through brainstorming and requirements gathering, then generate the new agent’s structure and files.

## Steps
1. Initiate brainstorming session (purpose, name, location, tools, knowledge base, outputs, commands, templates, tasks, checklists).
2. Summarize and confirm requirements.
3. Generate agent folder structure (BMAD-compliant).
4. Create prompt, tasks, templates, checklists, data, utils, and commands folders/files.
5. Generate summary of process in both .md and .docx formats.
6. Output completion message and next steps.
