# Team Agents MCP Server

A Model Context Protocol (MCP) server that provides access to team agents via standardized tools.

## Features

- **Validation Strategist Agent**: Strategic guidance and validation for projects and decisions
- **Agents Factory**: Create and manage specialized agents for various tasks
- **Team Consultation**: Combined input from both validation strategist and agents factory

## Installation

```bash
npm install
npm run build
```

## Usage

### With VS Code

Add to your VS Code MCP configuration:

```json
{
  "mcpServers": {
    "team-agents": {
      "command": "node",
      "args": ["path/to/team-agents-mcp-server/build/index.js"]
    }
  }
}
```

### Direct Usage

```bash
npm run start
```

## Available Tools

### validation_strategist
Get guidance and validation from the validation strategist agent.

**Parameters:**
- `query` (required): The question or task you need validation strategy guidance on
- `context` (optional): Additional context about your current situation or project

### agents_factory
Access the agents factory for creating and managing specialized agents.

**Parameters:**
- `request` (required): What type of agent or factory service you need
- `specifications` (optional): Detailed specifications for the agent or service you want to create

### team_consultation
Get combined input from both validation strategist and agents factory.

**Parameters:**
- `topic` (required): The topic or problem you want to discuss with the team
- `validation_focus` (optional): Specific validation concerns you want the strategist to address
- `factory_needs` (optional): Any specific agent creation or factory services needed

## Development

```bash
npm run dev
```

## MCP Protocol

This server implements the Model Context Protocol specification for tool integration with AI applications.