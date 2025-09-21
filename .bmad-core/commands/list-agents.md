# Command: list-agents

## Purpose
Display all available agents in the system in a clear, organized format.

## Usage
When invoked via `*list-agents`, this command scans for and displays all agents available in the workspace.

## Output Format
```
## Available Agents
1. Agent Name - Brief description (Location: path/to/agent)
2. Another Agent - Brief description (Location: path/to/agent)
...
```

## Search Locations
- `.bmad-core/agents/` - Core agent definitions
- `agents/` - User-created agents (if exists)
- Other configured agent directories

## Information Displayed
For each agent:
- Agent name and title
- Brief description/purpose
- File location
- Status (active/inactive if applicable)

## Implementation Notes
- Use numbered list format for consistency
- Include location for user reference
- Sort alphabetically for easy browsing
- Handle cases where no agents are found
- Support filtering options if needed

## Dependencies
- File system scanning capabilities
- Agent metadata parsing
- Standard output formatting