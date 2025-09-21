# Command: create

## Purpose
Start the agent creation workflow by facilitating a brainstorming session and then building the complete agent structure.

## Usage
When invoked via `*create`, this command:
1. Initiates a structured brainstorming session
2. Gathers all required agent specifications
3. Creates the BMAD-compliant folder structure
4. Generates all necessary files and documentation

## Process Flow
1. **Brainstorming Phase**
   - Agent purpose and goals
   - Name and location
   - Required tools and integrations
   - Knowledge base needs
   - Output requirements
   - Commands and workflows

2. **Confirmation Phase**
   - Summary of requirements
   - User approval before proceeding

3. **Generation Phase**
   - Create folder structure
   - Generate prompt file
   - Create tasks, templates, checklists
   - Set up utilities and commands
   - Generate documentation

## Output
- Complete agent folder with BMAD structure
- Summary document in both .md and .docx formats
- All required configuration files

## Dependencies
- `facilitate-brainstorming-session.md` task
- `create-agent.md` task
- `agent-summary-tmpl.md` and `.docx` templates
- `agent-creation-checklist.md`