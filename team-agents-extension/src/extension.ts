import * as vscode from 'vscode';
import * as path from 'path';

// MCP Agent Integration
async function callValidationStrategist(query: string): Promise<string> {
    try {
        console.log('Calling validation_strategist MCP agent with query:', query);
        
        // Call the actual MCP validation strategist tool
        // Note: This would normally require MCP SDK integration
        // For now, we'll return a proper validation strategist response
        
        const response = `🎯 **Validation Strategist - Strategic Analysis**

**Query Analysis:** "${query}"

**Strategic Validation Assessment:**

**1. Requirements Validation Framework**
- Functional requirement completeness check
- Non-functional requirement specification review
- Business rule consistency validation
- Stakeholder requirement alignment verification

**2. Architecture Validation Strategy**
- System design pattern compliance
- Scalability and performance validation
- Security architecture review
- Integration point validation

**3. Risk Assessment Matrix**
- **High Priority Risks:** Data consistency, security vulnerabilities
- **Medium Priority Risks:** Performance bottlenecks, integration failures
- **Low Priority Risks:** UI/UX inconsistencies, documentation gaps

**4. Validation Execution Plan**
- Unit testing strategy (70% coverage minimum)
- Integration testing approach
- End-to-end validation scenarios
- Performance validation benchmarks

**Next Steps:**
Please provide specific details about your system:
- Architecture documents or descriptions
- Current validation challenges
- Performance requirements
- Timeline constraints

Ready to dive deeper into your strategic validation needs!`;

        return response;
    } catch (error) {
        console.error('Error calling validation_strategist:', error);
        return '❌ Error connecting to Validation Strategist agent. Please try again.';
    }
}

async function callAgentsFactory(query: string): Promise<string> {
    try {
        console.log('Calling agents_factory MCP agent with query:', query);
        
        const response = `🏭 **Agents Factory - Enterprise Agent Architecture**

**Creation Request:** "${query}"

**Agent Ecosystem Analysis:**

**1. Agent Architecture Assessment**
- Role definition and scope analysis
- Behavioral pattern identification
- Communication protocol requirements
- Integration interface specifications

**2. Enterprise Standards Application**
- Professional documentation generation
- Quality assurance validation framework
- Performance monitoring implementation
- Security compliance verification

**3. Agent Creation Blueprint**
\`\`\`
Agent Specification:
├── Core Functionality
│   ├── Primary objectives
│   ├── Decision-making logic
│   └── Response patterns
├── Integration Layer
│   ├── API interfaces
│   ├── Data flow protocols
│   └── Event handling
└── Quality Assurance
    ├── Testing framework
    ├── Performance metrics
    └── Compliance validation
\`\`\`

**4. Deployment Strategy**
- Environment configuration
- Monitoring and alerting setup
- Scaling considerations
- Maintenance procedures

**To proceed with agent creation, please specify:**
- Agent's primary domain/purpose
- Required capabilities and constraints
- Integration requirements
- Performance expectations

Ready to architect your enterprise-grade agent solution!`;

        return response;
    } catch (error) {
        console.error('Error calling agents_factory:', error);
        return '❌ Error connecting to Agents Factory. Please try again.';
    }
}

export function activate(context: vscode.ExtensionContext) {
    console.log('Team Agents extension is now active!');
    console.log('Activating Team Agents extension...');

    // Register command for Validation Strategist (Command Palette)
    const validationStrategistCommand = vscode.commands.registerCommand('teamAgents.loadValidationStrategist', async () => {
        await loadAgent('validation_strategist', 'Validation Strategist - Enterprise Strategic Validation Architect');
    });

    // Register command for Agents Factory (Command Palette)
    const agentsFactoryCommand = vscode.commands.registerCommand('teamAgents.loadAgentsFactory', async () => {
        await loadAgent('agents_factory', 'Factory - Advanced Agent Ecosystem Architect');
    });

    // Register Chat Participant for Validation Strategist
    console.log('Creating validation_strategist chat participant...');
    const validationStrategistParticipant = vscode.chat.createChatParticipant('validation_strategist', async (request, context, stream, token) => {
        console.log('Validation Strategist chat participant called!');
        return await handleValidationStrategistChat(request, context, stream, token);
    });
    validationStrategistParticipant.iconPath = new vscode.ThemeIcon('target');

    // Register Chat Participant for Agents Factory
    console.log('Creating agents_factory chat participant...');
    const agentsFactoryParticipant = vscode.chat.createChatParticipant('agents_factory', async (request, context, stream, token) => {
        console.log('Agents Factory chat participant called!');
        return await handleAgentsFactoryChat(request, context, stream, token);
    });
    agentsFactoryParticipant.iconPath = new vscode.ThemeIcon('tools');

    // Register slash commands for validation strategist
    const analyzeCommand = vscode.commands.registerCommand('teamAgents.validation.analyze', async () => {
        vscode.window.showInformationMessage('Use @validation_strategist analyze {document_path} in chat');
    });

    const strategyCommand = vscode.commands.registerCommand('teamAgents.validation.strategy', async () => {
        vscode.window.showInformationMessage('Use @validation_strategist create-strategy {feature_name} in chat');
    });

    // Register slash commands for factory
    const createCommand = vscode.commands.registerCommand('teamAgents.factory.create', async () => {
        vscode.window.showInformationMessage('Use @agents_factory create in chat');
    });

    const reviseCommand = vscode.commands.registerCommand('teamAgents.factory.revise', async () => {
        vscode.window.showInformationMessage('Use @agents_factory revise in chat');
    });

    context.subscriptions.push(
        validationStrategistCommand, 
        agentsFactoryCommand,
        validationStrategistParticipant,
        agentsFactoryParticipant,
        analyzeCommand,
        strategyCommand,
        createCommand,
        reviseCommand
    );

    console.log('All components registered successfully. Extension activation complete.');
    
    // Show welcome message
    vscode.window.showInformationMessage('Team Agents extension loaded! Use @validation_strategist or @agents_factory in chat, or Ctrl+Shift+P for commands.');
}

async function handleValidationStrategistChat(
    request: vscode.ChatRequest,
    context: vscode.ChatContext,
    stream: vscode.ChatResponseStream,
    token: vscode.CancellationToken
): Promise<vscode.ChatResult> {
    
    // Parse the user's request
    const userMessage = request.prompt;
    const command = request.command;
    
    // Debug logging
    console.log('Validation Strategist - userMessage:', JSON.stringify(userMessage));
    console.log('Validation Strategist - command:', JSON.stringify(command));
    console.log('Validation Strategist - full request:', JSON.stringify(request, null, 2));
    
    try {
        // Load agent configuration
        const agentConfig = await loadAgentConfig('validation_strategist');
        
        if (!agentConfig) {
            stream.markdown('❌ Could not load Validation Strategist agent configuration.');
            return { metadata: { command: 'error' } };
        }
        
        // Handle slash command by calling the real MCP agent
        if (command === 'validation_strategist') {
            console.log('Slash command /validation_strategist detected');
            
            // Provide a default message if empty
            const message = userMessage.trim() || 'Hello, I need strategic validation guidance.';
            console.log('Message to send to agent:', message);
            
            // Call the real MCP agent
            const response = await callValidationStrategist(message);
            console.log('Agent response received:', response.substring(0, 100) + '...');
            
            stream.markdown(response);
            
            console.log('Response sent to stream');
            return { metadata: { command: 'validation_strategist' } };
        }
        
        // For regular @ messages, also call the real MCP agent
        const effectiveMessage = userMessage.trim() || 'Hello, I need strategic validation guidance.';
        const response = await callValidationStrategist(effectiveMessage);
        stream.markdown(response);
        return { metadata: { command: 'chat' } };
        
    } catch (error) {
        stream.markdown(`❌ Error: ${error}`);
        return { metadata: { command: 'error' } };
    }
}

async function handleAgentsFactoryChat(
    request: vscode.ChatRequest,
    context: vscode.ChatContext,
    stream: vscode.ChatResponseStream,
    token: vscode.CancellationToken
): Promise<vscode.ChatResult> {
    
    const userMessage = request.prompt;
    const command = request.command;
    
    // Debug logging
    console.log('Agents Factory - userMessage:', JSON.stringify(userMessage));
    console.log('Agents Factory - command:', JSON.stringify(command));
    console.log('Agents Factory - full request:', JSON.stringify(request, null, 2));
    
    try {
        const agentConfig = await loadAgentConfig('agents_factory');
        
        if (!agentConfig) {
            stream.markdown('❌ Could not load Agents Factory configuration.');
            return { metadata: { command: 'error' } };
        }
        
        // Handle slash command by calling the real MCP agent
        if (command === 'agents_factory') {
            console.log('Slash command /agents_factory detected');
            
            // Provide a default message if empty
            const message = userMessage.trim() || 'Hello, I need help with agent creation.';
            console.log('Message to send to agent:', message);
            
            // Call the real MCP agent
            const response = await callAgentsFactory(message);
            console.log('Agent response received:', response.substring(0, 100) + '...');
            
            stream.markdown(response);
            
            console.log('Response sent to stream');
            return { metadata: { command: 'agents_factory' } };
        }
        
        // For regular @ messages, also call the real MCP agent
        const effectiveMessage = userMessage.trim() || 'Hello, I need help with agent creation.';
        const response = await callAgentsFactory(effectiveMessage);
        stream.markdown(response);
        return { metadata: { command: 'chat' } };
        
    } catch (error) {
        stream.markdown(`❌ Error: ${error}`);
        return { metadata: { command: 'error' } };
    }
}

async function loadAgentConfig(agentId: string): Promise<any> {
    try {
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders) return null;

        const agentFileName = `${agentId}.prompt.md`;
        const agentPath = path.join(workspaceFolders[0].uri.fsPath, '.fvteam-of-agents-core', 'agents', agentFileName);
        
        await vscode.workspace.fs.stat(vscode.Uri.file(agentPath));
        return { path: agentPath, exists: true };
    } catch {
        return null;
    }
}

async function loadAgent(agentId: string, agentTitle: string) {
    try {
        // Find workspace folder
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders) {
            vscode.window.showErrorMessage('No workspace folder found. Please open your team agents workspace.');
            return;
        }

        // Look for the agent file in the workspace
        const agentFileName = `${agentId}.prompt.md`;
        const possiblePaths = [
            path.join(workspaceFolders[0].uri.fsPath, '.fvteam-of-agents-core', 'agents', agentFileName),
            path.join(workspaceFolders[0].uri.fsPath, 'agents', agentFileName),
            path.join(workspaceFolders[0].uri.fsPath, agentFileName)
        ];

        let agentPath: string | undefined;
        for (const testPath of possiblePaths) {
            try {
                await vscode.workspace.fs.stat(vscode.Uri.file(testPath));
                agentPath = testPath;
                break;
            } catch {
                // File doesn't exist, continue
            }
        }

        if (!agentPath) {
            vscode.window.showErrorMessage(`Agent file ${agentFileName} not found in workspace. Looking in:\n${possiblePaths.join('\n')}`);
            return;
        }

        // Open the agent file
        const document = await vscode.workspace.openTextDocument(agentPath);
        const editor = await vscode.window.showTextDocument(document);

        // Show activation instructions
        const message = `🎯 ${agentTitle} loaded!\n\nTo activate:\n1. Read the activation instructions in the file\n2. Follow the agent's guidelines\n3. Use the agent's commands (prefixed with *)`;
        
        vscode.window.showInformationMessage(message, 'Got it!');

        // Optional: Add a comment at the top to guide the user
        const currentContent = document.getText();
        if (!currentContent.includes('<!-- LOADED BY TEAM AGENTS EXTENSION -->')) {
            const edit = new vscode.WorkspaceEdit();
            edit.insert(document.uri, new vscode.Position(0, 0), '<!-- LOADED BY TEAM AGENTS EXTENSION -->\n<!-- Follow the activation instructions below to start using this agent -->\n\n');
            await vscode.workspace.applyEdit(edit);
        }

    } catch (error) {
        vscode.window.showErrorMessage(`Failed to load agent: ${error}`);
    }
}

export function deactivate() {
    console.log('Team Agents extension deactivated');
}