# Team Agents MCP Server````markdown

# Agents Factory

A Model Context Protocol (MCP) server that provides access to specialized AI agents for validation strategy and agent factory services.

The Agents Factory is a BMAD-compliant agent designed to help you create and revise new agents, agent templates, and agent environments through a structured, collaborative process.

## Overview

## Agent Creation Flowchart

This MCP server exposes three powerful tools that give you access to:

```mermaid

- **Validation Strategist**: Get strategic guidance and validation for your projects, decisions, and implementationsflowchart TD

- **Agents Factory**: Create and access specialized agents tailored to your specific needs    A[Start: User invokes Factory agent] --> B[Factory agent greets user and offers commands]

- **Team Consultation**: Combined input from both agents working together on your challenges    B --> C{User selects 'create'}

    C --> D[Facilitate brainstorming session]

## Features    D --> E[Elicit requirements: purpose, name, location, tools, knowledge base, outputs, commands, templates, tasks, checklists]

    E --> F[Summarize and confirm requirements]

- 🔧 **Three MCP Tools**: validation_strategist, agents_factory, and team_consultation    F --> G[Generate agent folder structure (BMAD-compliant)]

- 📝 **Rich Prompt Integration**: Uses comprehensive prompt files from the .fvteam-of-agents-core    G --> H[Create prompt, tasks, templates, checklists, data, utils, commands]

- 🔌 **VS Code Integration**: Pre-configured for GitHub Copilot in VS Code    H --> I[Generate summary of process in .md and .docx]

- 🛡️ **TypeScript**: Fully typed with robust error handling    I --> J[Output completion message and next steps]

- 🚀 **Easy Setup**: Simple installation and configuration process    J --> K[End]

```

## Prerequisites

## Key Features

- Node.js 18.0.0 or higher- Structured brainstorming and requirements gathering

- npm or yarn package manager- Automatic generation of all agent files and folders

- TypeScript (installed as dev dependency)- BMAD-compliant modular structure

- Summaries and documentation in both Markdown and Word formats

## Installation- Revision workflow for existing agents



1. **Clone or navigate to this directory**:For more details, see `.bmad-core/agents/agents_factory.prompt.md` and the templates, tasks, and checklists in `.bmad-core/`.

   ```bash

   cd "c:\team of agents"````
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Build the server**:
   ```bash
   npm run build
   ```

## Usage

### With VS Code GitHub Copilot

The server is pre-configured to work with VS Code GitHub Copilot through the `.vscode/mcp.json` file.

1. Open VS Code in this directory
2. The MCP server will be automatically available to GitHub Copilot
3. Use the tools through Copilot chat by referencing the agent tools

### With MCP Inspector (Testing)

To test the server with MCP Inspector:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

This will start the inspector web interface where you can test all three tools.

### Manual Command Line

You can also run the server directly:

```bash
npm start
# or
node build/index.js
```

## Available Tools

### 1. validation_strategist

Get strategic validation guidance for your projects and decisions.

**Parameters:**
- `query` (required): The question or task you need validation strategy guidance on
- `context` (optional): Additional context about your current situation or project

**Example usage:**
```
I need to validate my microservices architecture approach for a high-traffic e-commerce platform.
```

### 2. agents_factory

Access the agents factory for creating and managing specialized agents.

**Parameters:**
- `request` (required): What type of agent or factory service you need
- `specifications` (optional): Detailed specifications for the agent or service you want to create

**Example usage:**
```
I need an agent specialized in API security testing for REST endpoints.
```

### 3. team_consultation

Get coordinated input from both the validation strategist and agents factory.

**Parameters:**
- `topic` (required): The topic or problem you want to discuss with the team
- `validation_focus` (optional): Specific validation concerns you want the strategist to address
- `factory_needs` (optional): Any specific agent creation or factory services needed

**Example usage:**
```
I'm planning a migration from monolith to microservices and need both validation strategy and specialized agents for the process.
```

## Project Structure

```
team-agents-mcp-server/
├── src/
│   └── index.ts          # Main MCP server implementation
├── build/                # Compiled JavaScript (generated)
├── .vscode/
│   └── mcp.json         # VS Code MCP configuration
├── .fvteam-of-agents-core/
│   └── agents/          # Prompt files for agents
│       ├── validation_strategist.prompt.md
│       └── agents_factory.prompt.md
├── package.json         # Dependencies and scripts
├── tsconfig.json        # TypeScript configuration
└── README.md           # This file
```

## Development

### Available Scripts

- `npm run build` - Compile TypeScript to JavaScript
- `npm run dev` - Watch mode for development
- `npm start` - Run the compiled server
- `npm run clean` - Remove build directory

### Making Changes

1. Edit source files in `src/`
2. Run `npm run build` to compile
3. Test with MCP Inspector: `npx @modelcontextprotocol/inspector node build/index.js`

### Adding New Tools

To add a new MCP tool:

1. Add the tool registration in `src/index.ts`:
   ```typescript
   server.registerTool(
     "tool_name",
     {
       description: "Tool description",
       inputSchema: {
         param: z.string().describe("Parameter description")
       }
     },
     async ({ param }) => {
       // Tool implementation
       return {
         content: [{ type: "text", text: "Response" }]
       };
     }
   );
   ```

2. Rebuild with `npm run build`

## Configuration

### VS Code Integration

The `.vscode/mcp.json` file configures the server for GitHub Copilot:

```json
{
  "mcpServers": {
    "team-agents-mcp-server": {
      "command": "node",
      "args": [
        "c:\\team of agents\\build\\index.js"
      ]
    }
  }
}
```

### Environment Variables

Currently, no environment variables are required. All configuration is handled through the MCP protocol.

## Troubleshooting

### Common Issues

1. **Build fails**: Ensure TypeScript is installed and `npm install` completed successfully
2. **Prompt files not found**: Verify the `.fvteam-of-agents-core/agents/` directory contains the required `.prompt.md` files
3. **VS Code doesn't see the server**: Check that the path in `.vscode/mcp.json` is correct and absolute

### Debug Mode

To see detailed logging, the server outputs debug information to stderr:

```bash
node build/index.js 2>debug.log
```

### Testing Connection

Use MCP Inspector to verify the server is working:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

## Contributing

1. Make your changes in the `src/` directory
2. Test with `npm run build` and MCP Inspector
3. Update this README if adding new features
4. Ensure all TypeScript compiles without errors

## License

MIT

## Support

For issues related to:
- **MCP Protocol**: Visit [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- **VS Code Integration**: Check [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- **Agent Prompts**: Refer to the `.fvteam-of-agents-core` documentation

---

**Note**: This MCP server requires the `.fvteam-of-agents-core` directory with agent prompt files to function properly. Make sure these files are present before running the server.