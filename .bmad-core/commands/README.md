# Commands

The commands directory contains specific command implementations for the Agents Factory.

## Available Commands

### Core Agent Commands
- `help.md` - Display available commands with numbered options
- `create.md` - Initiate agent creation workflow
- `revise.md` - Start agent revision process
- `list-agents.md` - Show all available agents in the system
- `doc-out.md` - Output agent documentation or prompt files
- `exit.md` - End the current session

## Command Structure

Each command file should contain:
- **Purpose**: Clear description of what the command does
- **Usage**: How to invoke and use the command
- **Parameters**: Any required or optional parameters
- **Output**: Expected results and format
- **Examples**: Sample usage scenarios

## Adding New Commands

When creating new commands:
1. Follow the BMAD structure principles
2. Ensure commands are discoverable via the help system
3. Update the main agent prompt to include new commands
4. Add documentation for the command in this directory
5. Test thoroughly in the agent workflow

## Integration Notes

Commands are referenced in:
- `.bmad-core/agents/agents_factory.prompt.md` (main command list)
- Task files that may invoke specific commands
- User interface through the numbered options protocol