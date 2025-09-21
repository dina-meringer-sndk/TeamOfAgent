# BMAD Framework Principles

## Overview
BMAD (Branched Modular Agent Design) is a framework for creating organized, maintainable, and extensible AI agents.

## Core Principles

### 1. Modular Structure
Every agent follows a standardized folder structure:
```
.bmad-core/
├── agents/           # Agent prompt definitions
├── tasks/           # Workflow task definitions
├── templates/       # Document and output templates
├── commands/        # Command implementations
├── checklists/      # Validation and quality checklists
├── data/           # Knowledge base and reference data
└── utils/          # Utility scripts and tools
```

### 2. Clear Separation of Concerns
- **Agents**: Core behavior and personality
- **Tasks**: Structured workflows and processes
- **Templates**: Standardized output formats
- **Commands**: User interaction patterns
- **Checklists**: Quality assurance and validation
- **Data**: Knowledge base and references
- **Utils**: Supporting tools and utilities

### 3. Discoverability
- Every folder contains a README.md explaining its purpose
- All components are well-documented
- Clear naming conventions throughout
- Structured navigation and references

### 4. Extensibility
- Easy to add new capabilities
- Modular components can be reused
- Clear interfaces between components
- Scalable architecture

### 5. User-Centric Design
- Numbered options protocol for user interaction
- Clear command structure
- Consistent output formats
- Helpful documentation and guidance

## Implementation Guidelines

### Agent Creation
1. Always start with requirements gathering
2. Follow structured brainstorming process
3. Use established templates and patterns
4. Validate against quality checklists
5. Generate comprehensive documentation

### File Organization
- Use clear, descriptive names
- Follow established naming conventions
- Maintain consistent structure across agents
- Include proper cross-references

### Documentation
- Every component must have documentation
- Use both Markdown and Word formats when needed
- Include examples and usage patterns
- Maintain up-to-date references

### Quality Assurance
- Use validation checklists
- Test all workflows thoroughly
- Peer review when possible
- Continuous improvement mindset