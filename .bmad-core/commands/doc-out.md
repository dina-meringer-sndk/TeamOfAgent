# Command: doc-out

## Purpose
Output the documentation or prompt file for a specified agent, making it easy to review agent specifications.

## Usage
When invoked via `*doc-out`, this command:
1. Prompts user to select an agent (if not specified)
2. Displays the agent's main documentation or prompt file
3. Optionally saves the output to a file

## Parameters
- Agent name/identifier (optional - will prompt if not provided)
- Output format preference (display, save, both)

## Output Options
1. **Display**: Show content in the conversation
2. **Save**: Export to file in output directory
3. **Both**: Display and save simultaneously

## Supported File Types
- `*.prompt.md` - Main agent prompt files
- `README.md` - Agent documentation
- `summary.md` - Agent creation summaries
- Configuration files

## Output Format
```
## Agent Documentation: [Agent Name]
Source: [file path]

[File contents]
```

## Implementation Notes
- Handle missing files gracefully
- Support multiple documentation formats
- Provide clear source attribution
- Use numbered options for file selection if multiple docs exist
- Preserve original formatting

## Dependencies
- File reading capabilities
- Agent directory scanning
- Output formatting utilities