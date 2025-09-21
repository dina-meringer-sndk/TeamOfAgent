# Command: revise

## Purpose
Start the agent revision workflow to update an existing agent's structure, capabilities, or configuration.

## Usage
When invoked via `*revise`, this command:
1. Lists available agents for selection
2. Identifies what aspects need revision
3. Facilitates focused brainstorming for changes
4. Updates the agent structure and files
5. Generates revision summary

## Process Flow
1. **Agent Selection**
   - Display numbered list of available agents
   - User selects agent to revise

2. **Change Identification**
   - Determine what aspects need updating:
     - Commands and workflows
     - Tools and integrations
     - Prompt modifications
     - Template updates
     - New tasks or checklists

3. **Focused Brainstorming**
   - Explore revision requirements
   - Consider impact on existing functionality
   - Plan implementation approach

4. **Implementation**
   - Update relevant files
   - Maintain BMAD compliance
   - Preserve existing functionality where possible

5. **Documentation**
   - Generate revision summary
   - Update agent documentation
   - Note changes for future reference

## Output
- Updated agent files and structure
- Revision summary in both .md and .docx formats
- Updated documentation

## Dependencies
- `revise-agent.md` task
- `facilitate-brainstorming-session.md` task
- Agent template files
- Existing agent structure