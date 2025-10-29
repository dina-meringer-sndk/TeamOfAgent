````markdown
# Agents Factory

The Agents Factory is a BMAD-compliant agent designed to help you create and revise new agents, agent templates, and agent environments through a structured, collaborative process.

## Agent Creation Flowchart

```mermaid
flowchart TD
    A[Start: User invokes Factory agent] --> B[Factory agent greets user and offers commands]
    B --> C{User selects 'create'}
    C --> D[Facilitate brainstorming session]
    D --> E[Elicit requirements: purpose, name, location, tools, knowledge base, outputs, commands, templates, tasks, checklists]
    E --> F[Summarize and confirm requirements]
    F --> G[Generate agent folder structure (BMAD-compliant)]
    G --> H[Create prompt, tasks, templates, checklists, data, utils, commands]
    H --> I[Generate summary of process in .md and .docx]
    I --> J[Output completion message and next steps]
    J --> K[End]
```

## Key Features
- Structured brainstorming and requirements gathering
- Automatic generation of all agent files and folders
- BMAD-compliant modular structure
- Summaries and documentation in both Markdown and Word formats
- Revision workflow for existing agents

For more details, see `.bmad-core/agents/agents_factory.prompt.md` and the templates, tasks, and checklists in `.bmad-core/`.

````