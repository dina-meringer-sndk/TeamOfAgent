# Agents Factory - Quick Start Guide

Welcome to the Agents Factory! This guide will help you get started with creating and managing AI agents using the BMAD framework.

## 🚀 Quick Start

### 1. Activate the Factory Agent
To begin using the factory agent, you'll typically activate it through your preferred AI platform with the prompt file:
```
Load: .bmad-core/agents/agents_factory.prompt.md
```

### 2. Basic Commands
Once activated, the factory agent supports these numbered commands:

```
## Available Commands
1. *help - Show this command list
2. *create - Start agent creation (brainstorm, then build)
3. *revise - Start revision process for an existing agent  
4. *list-agents - Show all available agents
5. *doc-out - Output the agent's documentation or prompt file
6. *exit - End session
```

### 3. Creating Your First Agent

#### Step 1: Start Creation
Type: `*create` or select option `2`

#### Step 2: Brainstorming Session
The factory will guide you through:
- **Purpose**: What should your agent do?
- **Name**: What will you call it?
- **Location**: Where should it be created?
- **Tools**: What integrations does it need?
- **Outputs**: What should it produce?
- **Commands**: How will users interact with it?

#### Step 3: Automatic Generation
The factory will create:
- Complete BMAD folder structure
- Agent prompt file
- Task workflows
- Templates and checklists
- Utility scripts
- Documentation

## 📁 Understanding the BMAD Structure

Your new agent will have this structure:
```
your-agent/
├── .bmad-core/
│   ├── agents/          # Agent prompt definitions
│   ├── tasks/           # Workflow processes
│   ├── templates/       # Output templates
│   ├── commands/        # User commands
│   ├── checklists/      # Quality validation
│   ├── data/           # Knowledge base
│   └── utils/          # Supporting tools
├── output/             # Generated content
└── README.md          # Agent documentation
```

## 🔧 Advanced Usage

### Revising Existing Agents
1. Use `*revise` command
2. Select agent to modify
3. Specify what needs updating
4. Follow guided revision process

### Quality Assurance
- All agents include validation checklists
- Documentation is generated in both Markdown and Word formats
- BMAD compliance is automatically verified

### Integration
- Agents can integrate with external tools
- Utility scripts handle file operations
- Template system ensures consistent outputs

## 📚 Learning Resources

### Key Files to Review
- `factory_agent_summary.md` - Complete overview
- `.bmad-core/data/agents_factory/bmad-principles.md` - Framework guidelines
- `.bmad-core/data/agents_factory/agent-patterns.md` - Design patterns
- Individual README files in each directory

### Example Workflow
1. **Research**: Review patterns and examples
2. **Plan**: Define agent purpose and scope
3. **Create**: Use factory to generate structure
4. **Customize**: Modify generated files as needed
5. **Test**: Validate agent functionality
6. **Document**: Update documentation and examples

## 🛠️ Troubleshooting

### Common Issues
- **Missing Dependencies**: Check required Python packages
- **File Permissions**: Ensure write access to target directories
- **Template Errors**: Verify template files are properly formatted

### Getting Help
- Review README files in each directory
- Check the knowledge base in `.bmad-core/data/agents_factory/`
- Use `*doc-out` to examine existing agent configurations
- Follow the troubleshooting guide (planned feature)

## 🎯 Best Practices

1. **Start Simple**: Begin with basic agents and add complexity gradually
2. **Follow Patterns**: Use established patterns from the knowledge base
3. **Document Everything**: Maintain clear documentation for all customizations
4. **Test Thoroughly**: Validate agents before deployment
5. **Iterate**: Use the revision workflow to improve agents over time

## 🔄 Continuous Improvement

The Agents Factory itself can be enhanced:
- Add new templates and patterns
- Extend utility functions
- Improve workflow processes
- Update knowledge base with lessons learned

---

**Ready to create your first agent?** 
Just activate the factory agent and type `*create` to begin!

For detailed technical documentation, see `factory_agent_summary.md`.