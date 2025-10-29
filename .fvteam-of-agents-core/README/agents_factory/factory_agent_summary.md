````markdown
# Agents Factory Agent: Design & Implementation Summary

## 1. User Requests
- Create a BMAD-compliant "Factory agent" to help users create and revise new agents, agent templates, and agent environments.
- The Factory agent must:
  - Drive a structured brainstorming process with the user for every new agent.
  - Elicit and document agent purpose, name, location, tools, input/output folders, file types, commands, templates, tasks, checklists, and environment needs.
  - Always generate a summary of requirements, brainstorming, and agent specs in both .md and .docx formats.
  - Always create a `utils` folder for each new agent, and ensure the agent's prompt instructs use of these utilities (e.g., for .docx read/write).
  - Maintain strict BMAD folder structure and prompting approach for all created agents.
  - Add a "revise" command for updating existing agents.
  - Include a flowchart in the main README.md to illustrate the agent creation process.
  - Add README.md files to all major folders for onboarding and discoverability.
  - Ensure all outputs are in both Markdown and Word formats.

## 2. Thought Process & Design Decisions
- **BMAD Compliance:**
  - All agent folders and files follow the BMAD modular structure: prompt, tasks, templates, commands, checklists, data, utils, output.
  - Prompts, templates, and checklists are explicit and discoverable.
- **User-Driven Workflow:**
  - The Factory agent always starts with a structured brainstorming session to clarify requirements and environment needs.
  - Numbered options protocol is enforced for all user choices.
- **Extensibility:**
  - README.md files in every folder explain purpose and extensibility.
  - Utilities folder is required for every agent, with at least one script (e.g., docx_utils.py).
- **Documentation & Reference:**
  - All major steps, requirements, and design choices are documented in this summary for future reference and onboarding.
- **Output Consistency:**
  - All summaries and documentation are generated in both .md and .docx formats for compatibility and user preference.

## 3. Final Factory Agent Specifications
- **Prompt:**
  - Persona, commands, tasks, dependencies, and core principles are clearly defined.
  - Explicit rules for BMAD compliance, user elicitation, and utils usage.
- **Tasks:**
  - `facilitate-brainstorming-session.md`: Guides the brainstorming process.
  - `create-agent.md`: Handles requirements gathering and agent generation.
  - `revise-agent.md`: Manages agent revision workflows.
- **Templates:**
  - `agent-summary-tmpl.md` and `.docx`: For summarizing requirements and process.
- **Checklists:**
  - `agent-creation-checklist.md`: Ensures all steps are followed.
- **Utils:**
  - `docx_utils.py`: For .docx read/write; extensible for more utilities.
- **Data:**
  - `agents_factory/` knowledge base for reference and improvement.
- **Output:**
  - All agent creation and revision summaries are saved in both .md and .docx formats in the agent's folder.
- **README.md:**
  - Main README includes a Mermaid flowchart of the agent creation process and onboarding info.

## 4. Folder and File Structure

```
.bmad-core/
  agents/
    agents_factory.prompt.md
  tasks/
    create-agent.md
    revise-agent.md
    facilitate-brainstorming-session.md
    README.md
  templates/
    agent-summary-tmpl.md
    agent-summary-tmpl.docx
    README.md
  checklists/
    agent-creation-checklist.md
    README.md
  data/
    agents_factory/
      README.md
    README.md
  utils/
    docx_utils.py
    README.md
  commands/
    README.md
output/
  README.md
README.md (main, with flowchart)
factory_agent_summary.md
factory_agent_summary.docx
```

---
This summary serves as a reference for users and future maintainers of the Factory agent. For any changes or extensions, follow the BMAD principles and update this summary accordingly.

````