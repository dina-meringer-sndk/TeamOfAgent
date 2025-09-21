# Command: exit

## Purpose
Gracefully end the current Agents Factory session with proper cleanup and farewell.

## Usage
When invoked via `*exit`, this command:
1. Performs any necessary cleanup
2. Saves session state if applicable
3. Provides a polite farewell message
4. Terminates the agent session

## Process Flow
1. **Cleanup Check**
   - Verify no pending operations
   - Save any unsaved work
   - Close open files or connections

2. **Session Summary** (if applicable)
   - Brief summary of session activities
   - Note any important outcomes
   - Provide references for follow-up

3. **Farewell**
   - Thank user for the session
   - Provide guidance for future use
   - Offer contact/support information

## Output Example
```
## Session Complete

Thank you for using the Agents Factory! 

Session Summary:
- [Brief summary of activities]

To restart the factory agent, simply invoke it again with your preferred method.

For documentation and support, refer to the README.md files in the .bmad-core directory.

Goodbye! 👋
```

## Implementation Notes
- Always provide a clean exit
- Ensure no data loss
- Leave the workspace in a clean state
- Be polite and helpful in farewell
- Provide clear restart instructions