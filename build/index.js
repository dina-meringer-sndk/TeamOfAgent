#!/usr/bin/env node
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { readFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
// Helper function to read prompt files
function readPromptFile(filename) {
    try {
        const promptPath = join(__dirname, "../../.fvteam-of-agents-core/agents", filename);
        return readFileSync(promptPath, "utf8");
    }
    catch (error) {
        console.error(`Error reading prompt file ${filename}:`, error);
        return `Error: Could not read ${filename}`;
    }
}
// Create the MCP server
const server = new McpServer({
    name: "team-agents-mcp-server",
    version: "1.0.0",
});
// Register validation_strategist tool
server.registerTool("validation_strategist", {
    description: "Get guidance and validation from the validation strategist agent",
    inputSchema: {
        query: z.string().describe("The question or task you need validation strategy guidance on"),
        context: z.string().optional().describe("Additional context about your current situation or project")
    }
}, async ({ query, context }) => {
    const prompt = readPromptFile("validation_strategist.prompt.md");
    const fullPrompt = `${prompt}

USER QUERY: ${query}

${context ? `ADDITIONAL CONTEXT: ${context}` : ""}

Please provide your strategic validation guidance based on the above query and context.`;
    return {
        content: [
            {
                type: "text",
                text: fullPrompt
            }
        ]
    };
});
// Register agents_factory tool
server.registerTool("agents_factory", {
    description: "Access the agents factory for creating and managing specialized agents",
    inputSchema: {
        request: z.string().describe("What type of agent or factory service you need"),
        specifications: z.string().optional().describe("Detailed specifications for the agent or service you want to create")
    }
}, async ({ request, specifications }) => {
    const prompt = readPromptFile("agents_factory.prompt.md");
    const fullPrompt = `${prompt}

FACTORY REQUEST: ${request}

${specifications ? `SPECIFICATIONS: ${specifications}` : ""}

Please process this factory request and provide guidance on creating or accessing the appropriate agent.`;
    return {
        content: [
            {
                type: "text",
                text: fullPrompt
            }
        ]
    };
});
// Register a combined tool for accessing both agents
server.registerTool("team_consultation", {
    description: "Get combined input from both validation strategist and agents factory",
    inputSchema: {
        topic: z.string().describe("The topic or problem you want to discuss with the team"),
        validation_focus: z.string().optional().describe("Specific validation concerns you want the strategist to address"),
        factory_needs: z.string().optional().describe("Any specific agent creation or factory services needed")
    }
}, async ({ topic, validation_focus, factory_needs }) => {
    const validationPrompt = readPromptFile("validation_strategist.prompt.md");
    const factoryPrompt = readPromptFile("agents_factory.prompt.md");
    const fullPrompt = `# Team Consultation Session

## Topic: ${topic}

---

## Validation Strategist Input
${validationPrompt}

VALIDATION FOCUS: ${topic}
${validation_focus ? `SPECIFIC CONCERNS: ${validation_focus}` : ""}

---

## Agents Factory Input
${factoryPrompt}

FACTORY CONSULTATION: ${topic}
${factory_needs ? `SPECIFIC NEEDS: ${factory_needs}` : ""}

---

Please provide coordinated guidance from both the validation strategist and agents factory perspectives on the above topic.`;
    return {
        content: [
            {
                type: "text",
                text: fullPrompt
            }
        ]
    };
});
// Main function to run the server
async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error("Team Agents MCP Server running on stdio");
}
// Handle graceful shutdown
process.on('SIGINT', async () => {
    console.error("Received SIGINT, shutting down gracefully...");
    process.exit(0);
});
process.on('SIGTERM', async () => {
    console.error("Received SIGTERM, shutting down gracefully...");
    process.exit(0);
});
// Start the server
main().catch((error) => {
    console.error("Fatal error in main():", error);
    process.exit(1);
});
//# sourceMappingURL=index.js.map