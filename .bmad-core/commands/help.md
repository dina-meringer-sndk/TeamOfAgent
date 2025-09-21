# Command: help

## Purpose
Display the available commands for the Agents Factory in a numbered list format for easy user selection.

## Usage
When invoked via `*help`, this command displays all available commands with descriptions.

## Output Format
```
## Available Commands
1. *help - Show this command list
2. *create - Start agent creation (brainstorm, then build)
3. *revise - Start revision process for an existing agent  
4. *list-agents - Show all available agents
5. *doc-out - Output the agent's documentation or prompt file
6. *exit - End session
```

## Implementation Notes
- Always use numbered list format
- Keep descriptions concise but clear
- Update this list when new commands are added
- Automatically invoked on agent activation