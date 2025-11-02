# Team Agents MCP Server - Setup and Usage Guide

## 🎉 Congratulations!

You have successfully created a Model Context Protocol (MCP) server that makes your team agents accessible through standardized tools. This provides a much better solution than the VS Code extension approach, as MCP servers work with multiple clients and don't have the "/" command limitations we encountered.

## 📦 What Was Installed

The following packages were installed:

### Core Dependencies
- `@modelcontextprotocol/sdk` - Official MCP TypeScript SDK
- `zod` - Schema validation library for input validation

### Development Dependencies  
- `@types/node` - TypeScript definitions for Node.js
- `tsx` - TypeScript execution engine for development
- `typescript` - TypeScript compiler

## 🏗️ Project Structure

```
team-agents-mcp-server/
├── src/
│   └── index.ts              # Main MCP server implementation
├── build/                    # Compiled JavaScript output
├── scripts/
│   └── setup.js             # Setup automation script
├── .vscode/                  # VS Code debugging configuration
├── package.json             # Project dependencies and scripts
├── tsconfig.json            # TypeScript configuration
├── mcp.json                 # MCP server configuration
└── README.md                # Documentation
```

## 🚀 Available Tools

Your MCP server provides three powerful tools:

### 1. `validation_strategist`
- **Purpose**: Get strategic guidance and validation
- **Parameters**:
  - `query` (required): Your question or task
  - `context` (optional): Additional context

### 2. `agents_factory` 
- **Purpose**: Create and manage specialized agents
- **Parameters**:
  - `request` (required): Type of agent or service needed
  - `specifications` (optional): Detailed specifications

### 3. `team_consultation`
- **Purpose**: Combined input from both agents
- **Parameters**:
  - `topic` (required): The topic to discuss
  - `validation_focus` (optional): Specific validation concerns
  - `factory_needs` (optional): Agent creation needs

## 🔧 How to Use with VS Code

### Option 1: Add to VS Code Settings
1. Open VS Code settings (JSON)
2. Add this to your MCP servers configuration:

```json
{
  "mcp.servers": {
    "team-agents": {
      "command": "node",
      "args": ["c:\\team of agents\\team-agents-mcp-server\\build\\index.js"]
    }
  }
}
```

### Option 2: Add to Claude Desktop
If you have Claude Desktop installed, add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "team-agents": {
      "command": "node", 
      "args": ["c:\\team of agents\\team-agents-mcp-server\\build\\index.js"]
    }
  }
}
```

## 🧪 Testing the Server

The server has been tested and is working correctly! You can verify it by running:

```bash
cd "c:\team of agents\team-agents-mcp-server"
node build/index.js
```

You should see: "Team Agents MCP Server running on stdio"

## 🔄 Development Workflow

1. **Make changes** to `src/index.ts`
2. **Rebuild** with: `npx tsc`
3. **Test** with: `node build/index.js`
4. **Restart** your MCP client (VS Code, Claude Desktop, etc.)

## 🎯 Next Steps

1. **Configure your MCP client** (VS Code or Claude Desktop) 
2. **Restart the client** to load the new server
3. **Test the tools** by asking questions that would benefit from validation or agent creation
4. **Customize the responses** in `src/index.ts` to connect to your actual agents (currently using mock responses)

## 🔗 Integration with Real Agents

To connect to your actual validation_strategist and agents_factory tools, modify the functions in `src/index.ts`:

- `callValidationStrategist()` - Replace with actual agent call
- `callAgentsFactory()` - Replace with actual agent call  
- `callTeamConsultation()` - Coordinate real agent interactions

## ✅ Success!

Your team agents are now accessible via the Model Context Protocol, which provides:
- ✅ Standardized tool interface
- ✅ Works with multiple clients (VS Code, Claude Desktop, etc.)
- ✅ No "/" command limitations
- ✅ Better integration and discoverability
- ✅ Professional, scalable approach

The MCP server approach is much more robust and widely supported than the VS Code extension approach we tried initially!