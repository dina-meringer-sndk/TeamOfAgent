# Team Agents VS Code Extension

This extension provides quick access to your team's validation agents directly from VS Code.

## Features

- **Quick Agent Loading**: Load agents with simple commands
- **Workspace Integration**: Automatically finds agent files in your workspace
- **Command Palette Access**: Use Ctrl+Shift+P to access agent commands

## Available Agents

### 🎯 Validation Strategist
Enterprise Strategic Validation Architect for comprehensive validation planning.
- **Command**: `Team Agents: Load Validation Strategist Agent`
- **File**: `validation_strategist.prompt.md`

### 🏭 Agents Factory  
Advanced Agent Ecosystem Architect for creating and managing agent ecosystems.
- **Command**: `Team Agents: Load Agents Factory`
- **File**: `agents_factory.prompt.md`

## Usage

1. **Open Command Palette**: Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
2. **Search for "Team Agents"**: Type "Team Agents" to see available commands
3. **Select Agent**: Choose the agent you want to load
4. **Follow Activation**: The agent file will open with activation instructions

## Installation

### Option 1: Package and Install
1. Install vsce: `npm install -g vsce`
2. Package extension: `vsce package`
3. Install: `code --install-extension team-agents-extension-1.0.0.vsix`

### Option 2: Development Mode
1. Open this folder in VS Code
2. Press `F5` to launch Extension Development Host
3. Test the extension in the new VS Code window

## Requirements

- VS Code 1.74.0 or higher
- Team agents workspace with `.fvteam-of-agents-core/agents/` structure

## Workspace Structure

The extension looks for agent files in:
```
workspace/
├── .fvteam-of-agents-core/
│   └── agents/
│       ├── validation_strategist.prompt.md
│       └── agents_factory.prompt.md
└── (or in workspace root)
```

## Commands

| Command | Description |
|---------|-------------|
| `Team Agents: Load Validation Strategist Agent` | Load the validation strategist for strategic validation planning |
| `Team Agents: Load Agents Factory` | Load the agents factory for creating new agents |

## Troubleshooting

### Agent File Not Found
- Ensure your workspace contains the `.fvteam-of-agents-core/agents/` folder
- Check that agent `.prompt.md` files exist in the correct location
- Open the correct workspace folder containing your team agents

### Extension Not Loading
- Check VS Code version (requires 1.74.0+)
- Reload VS Code window (`Ctrl+Shift+P` → "Developer: Reload Window")
- Check Output panel for extension logs

## Development

To modify this extension:
1. Edit `src/extension.ts`
2. Run `npm run compile`
3. Test with `F5` in VS Code

## Version History

- **1.0.0**: Initial release with Validation Strategist and Agents Factory support