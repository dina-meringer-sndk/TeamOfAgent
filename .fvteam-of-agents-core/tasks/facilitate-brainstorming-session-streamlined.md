<!-- Powered by FVTeamOfAgents Core -->
# Facilitate Brainstorming Session Task

## Purpose

Guide the user through an engaging, collaborative brainstorming session to discover and define all requirements for creating a complete BMAD agent ecosystem. Uses proven elicitation techniques to ensure comprehensive requirement gathering while maintaining user engagement and creativity.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Session Setup and Rapport Building

**OPENING ENERGY:**
- "Let's co-create something amazing together! We're going to design your ideal AI agent."
- **Session Contract**: "This will be collaborative - I'll ask questions, but feel free to interrupt with ideas, concerns, or 'what ifs' at any time."
- **SKIP POLICY**: "You can skip ANY question by saying 'skip', 'not sure', or 'pass'. I'll create smart placeholders and we'll come back to them later. No pressure to have perfect answers!"
- **Duration**: "15-25 minutes of focused exploration"

**SKIP TRACKING SETUP:**
Initialize tracking system for placeholder management:
- **Skipped Items Log**: Track all skipped questions by section
- **Placeholder Counter**: Number placeholders sequentially
- **Completion Priority**: Assign priority levels to each skip
- **Follow-up Actions**: Document specific next steps for each placeholder

**ENERGY CHECK:**
- "On a scale of 1-10, how excited are you about this agent idea?"
- "What's driving your enthusiasm for creating this agent?"

### 2. Core Agent Vision Discovery

**INTERACTIVE VISION CASTING:**
Ask questions one at a time, wait for response, then proceed to next:

**Q1:** "If your agent were a person in your organization, what would their job title be?"
*[If skip: LOG "VISION-01: Agent role/title TBD"]*

**Q2:** "Where should we build this agent's home base? (Provide full path for .bmad-core structure)"
*[If skip: LOG "VISION-02: Target directory TBD, using default"]*

**Q3:** "What should we call this agent? (Think of a name that captures its essence)"
*[If skip: LOG "VISION-03: Agent name TBD, using temp name"]*

**Q4:** "In one sentence, what problem does this agent solve for its users?"
*[If skip: LOG "VISION-04: Problem definition TBD - HIGH PRIORITY"]*

**Q5:** "Who's the main person who'll interact with this agent daily?"
*[If skip: LOG "VISION-05: User persona TBD - MEDIUM PRIORITY"]*

**SECTION COMPLETION:** "Great! We have your agent's basic identity. Remember, you can always refine the skipped items later."

### 3. Workflow Discovery (→ Creates Task Files)

**INTERACTIVE STORYTELLING:**

**Opening:** "Let's walk through a day in the life of your agent. A user comes to your agent with [typical problem]. Your agent says 'Great! Let me help you with that.' What happens next?"
*[If skip: LOG "WORKFLOW-01: Primary workflow TBD - HIGH PRIORITY"]*

**For Each Workflow Discovered:**

**Q1:** "What would you call this workflow? What triggers it?"
*[If skip: LOG "WORKFLOW-[N]-NAME: Workflow name/trigger TBD"]*

**Q2:** "Walk me through the steps - what happens first?"
*[If skip: LOG "WORKFLOW-[N]-STEPS: Workflow steps TBD - HIGH PRIORITY"]*

**Q3:** "Where does the user need to provide input or make decisions?"
*[If skip: LOG "WORKFLOW-[N]-INPUT: User interaction points TBD"]*

**Q4:** "How do we know this workflow succeeded? What does success look like?"
*[If skip: LOG "WORKFLOW-[N]-SUCCESS: Success criteria TBD"]*

**Q5:** "What could go wrong, and how should the agent handle it?"
*[If skip: LOG "WORKFLOW-[N]-ERROR: Error handling TBD"]*

**DISCOVERY LOOP:** "Are there other workflows this agent should handle?" *[Continue until complete]*

**MAPPING CONFIRMATION:**
"I'm planning to create [N] task files: [list names]. Does this capture all your workflows correctly?"

**ADAPTIVE HANDLING:** If vague answers, probe: "Can you walk me through one specific example?"

### 4. Content Generation Discovery (→ Creates Template Files)

**Opening:** "Now let's think about what your agent creates. Show me an example of something similar your agent should create, or describe it."
*[If skip: LOG "CONTENT-01: Content types TBD"]*

**For Each Content Type:**

**Q1:** "What would you call this type of content? What's its main purpose?"
*[If skip: LOG "CONTENT-[N]-PURPOSE: Content purpose TBD"]*

**Q2:** "Who's the audience for this content?"
*[If skip: LOG "CONTENT-[N]-AUDIENCE: Target audience TBD"]*

**Q3:** "If your agent made the perfect version of this, what sections or parts would it have?"
*[If skip: LOG "CONTENT-[N]-STRUCTURE: Content structure TBD"]*

**Q4:** "What information would the user need to provide vs. what should the agent figure out?"
*[If skip: LOG "CONTENT-[N]-INPUT: Input requirements TBD"]*

**Q5:** "What format should the final output be? Where does it go?"
*[If skip: LOG "CONTENT-[N]-FORMAT: Output format TBD"]*

**DISCOVERY LOOP:** "Are there other types of content this agent should generate?"

**MAPPING CONFIRMATION:**
"I'm planning [N] template files: [list names]. Will these handle all the content your agent needs to generate?"

### 5. Quality Assurance Discovery (→ Creates Checklist Files)

**Opening:** "Let's imagine this agent fails spectacularly. What went wrong?"
*[If skip: LOG "QUALITY-01: Quality standards TBD"]*

**Q1:** "Now flip that - when this agent produces something excellent, what makes it excellent?"
*[If skip: LOG "QUALITY-02: Excellence criteria TBD"]*

**Q2:** "If you were reviewing this agent's work, what's the first thing you'd check?"
*[If skip: LOG "QUALITY-03: Primary validation TBD"]*

**Q3:** "What's the second thing you'd check?"
*[If skip: LOG "QUALITY-04: Secondary validation TBD"]*

**Q4:** "What would make you immediately reject the agent's output?"
*[If skip: LOG "QUALITY-05: Rejection criteria TBD"]*

**Q5:** "If the agent's output fails your checks, what should happen next?"
*[If skip: LOG "QUALITY-06: Failure actions TBD"]*

**DISCOVERY LOOP:** "Are there other quality standards or validation areas we should consider?"

**MAPPING CONFIRMATION:**
"For quality control, I'll create [N] checklist files: [list names]. Do these cover all your validation needs?"

### 6. Knowledge Discovery (→ Creates Data Files)

**SECTION REMINDER:** "Remember, you can skip any questions you're unsure about!"

**Opening:** "Let's map the expertise your agent needs to be world-class at its job."
*[If skip: LOG "KNOWLEDGE-01: Knowledge areas TBD"]*

**Q1:** "What are the 3-4 major branches of knowledge your agent needs?"
*[If skip: LOG "KNOWLEDGE-02: Knowledge branches TBD"]*

**For Each Knowledge Branch:**

**Q2:** "For [knowledge branch], what do novices always get wrong?"
*[If skip: LOG "KNOWLEDGE-[N]-MISTAKES: Common mistakes TBD"]*

**Q3:** "What shortcuts or best practices would save users time?"
*[If skip: LOG "KNOWLEDGE-[N]-TIPS: Expert tips TBD"]*

**Q4:** "Where does this knowledge come from? Who's the authority?"
*[If skip: LOG "KNOWLEDGE-[N]-SOURCE: Knowledge sources TBD"]*

**Q5:** "How often does this information change?"
*[If skip: LOG "KNOWLEDGE-[N]-UPDATE: Update frequency TBD"]*

**DISCOVERY LOOP:** "Are there other areas of expertise this agent needs?"

**MAPPING CONFIRMATION:**
"I'll create [N] knowledge/data files: [list names]. Does this organize your agent's expertise correctly?"

### 7. Integration Discovery (→ Creates Utility Files)

**INTERACTIVE ECOSYSTEM MAPPING:**

**Opening:** "Your agent doesn't exist in isolation. Let's map its relationships with the world."
*[If "skip": "That's fine! We'll start with basic file operations and you can add integrations later."]*

**Q1:** "Where does your agent get its raw materials? What data sources does it need?"
*[If skip: default to "file-based input"]*

**Q2:** "Where do your agent's results need to end up? Who or what receives the output?"
*[If skip: default to "file-based output"]*

**Q3:** "What external services would make your agent incredibly powerful?"
*[If skip: include placeholder for "future integrations"]*

**For Each Integration, Ask:**

**Q4:** "For [specific integration], what exactly does it do?"
*[If skip: create generic integration placeholder]*

**Q5:** "Does your agent read from it, write to it, or both?"
*[If skip: assume "read/write capability"]*

**Q6:** "What kind of data gets transformed or processed?"
*[If skip: include generic data transformation placeholder]*

**DISCOVERY LOOP:** "Are there other external systems or services this agent should connect to?" *[If "skip", proceed to confirmation]*

**MAPPING CONFIRMATION:**
"For integrations, I'll create [N] utility files: [list names]. Will these handle all your agent's external connections?"

**ADAPTIVE HANDLING:** If uncertain, focus on: "What's the simplest way your agent could get and share information?"

### 8. Technical Constraints

**INTERACTIVE REALITY CHECK:**

**Q1:** "What tools and technologies are already in your environment?"
*[If skip: note as "TBD - environment assessment needed"]*

**Q2:** "Are there any security, compliance, or organizational constraints I should know about?"
*[If skip: include placeholder for "constraint review needed"]*

**Q3:** "What would 'good enough' performance look like for this agent?"
*[If skip: assume "reasonable response time for user interaction"]*

### 9. Final Validation and Mapping

**INTERACTIVE COMPREHENSIVE REVIEW:**

**Opening:** "Let me summarize what we've designed together and confirm it's right."
*[Present summary, wait for confirmation]*

**FILE CREATION SUMMARY:**
- **TASK FILES**: [List workflow names → task files]
- **TEMPLATE FILES**: [List content types → template files]  
- **CHECKLIST FILES**: [List validation areas → checklist files]
- **DATA FILES**: [List knowledge areas → data files]
- **UTILITY FILES**: [List integrations → utility files]

**VALIDATION QUESTIONS (Ask One at a Time):**

**Q1:** "Does this agent have everything it needs to succeed?"
*[If "skip" or "not sure": "We'll create it with expansion capabilities for future enhancement."]*

**Q2:** "Do all the pieces fit together logically?"
*[If skip: proceed with current design]*

**Q3:** "Will this actually solve your original problem?"
*[If skip: note as "validation needed after creation"]*

**PRIORITY RANKING (Ask Sequentially):**

**Q4:** "What's absolutely critical for version 1? (Must Have)"
*[If skip: treat all components as "Should Have"]*

**Q5:** "What's important but could wait for version 2? (Should Have)"
*[If skip: use intelligent defaults based on complexity]*

**Q6:** "What would be nice but isn't essential? (Could Have)"
*[If skip: mark advanced features as "Could Have"]*

**SKIP SUMMARY:** "No problem with the skipped questions! I've created smart placeholders and defaults. You can always refine these later."

**ADAPTIVE COMPLETION STRATEGY:**
Based on information completeness (80%+ = full ecosystem, 60-80% = robust core with placeholders, 40-60% = MVP with expansion hooks, <40% = discovery-focused agent)

### 10. Documentation and Handoff

**REQUIREMENTS COMPILATION:**
Transform brainstorming insights into structured data ready for template generation with:
- Target directory path and existing file analysis
- Agent definition with persona and technical specs
- File mappings with clear naming conventions
- Priority matrix and version planning
- Success criteria for agent creation

**SKIPPED ITEMS TRACKING:**
Maintain comprehensive record of all skipped questions and placeholders created:

**PLACEHOLDER INVENTORY:**
- **Vision Gaps**: [List any TBD items from section 2]
- **Workflow Gaps**: [List any workflow placeholders or TODO items]
- **Content Gaps**: [List any template placeholders or TBD items]
- **Quality Gaps**: [List any validation criteria placeholders]
- **Knowledge Gaps**: [List any TBD knowledge areas or sources]
- **Integration Gaps**: [List any placeholder integrations or connections]
- **Technical Gaps**: [List any TBD constraints or requirements]

**COMPLETION ROADMAP:**
For each placeholder, document:
- **What's Missing**: Specific information needed
- **How to Gather**: Suggested methods for getting the information
- **Priority Level**: Must Have / Should Have / Could Have
- **Completion Tasks**: Specific next steps to fill the gap

**FOLLOW-UP PLAN:**
Create structured approach for addressing skipped items:
1. **Immediate Creation**: Create agent with current information plus smart placeholders
2. **Phase 1 Refinement**: Address "Must Have" placeholders within first week
3. **Phase 2 Enhancement**: Address "Should Have" placeholders within first month
4. **Phase 3 Optimization**: Address "Could Have" placeholders as needed

**AGENT INTEGRATION FOR COMPLETION:**
Ensure the created agent includes mechanisms to complete placeholders:

**Built-in Completion Tasks:**
- `refine-agent-vision.md` - Task to complete vision placeholders
- `enhance-workflows.md` - Task to flesh out workflow placeholders  
- `improve-content-templates.md` - Task to refine content generation
- `strengthen-quality-checks.md` - Task to enhance validation criteria
- `expand-knowledge-base.md` - Task to complete knowledge gaps
- `add-integrations.md` - Task to implement placeholder integrations

**Completion Tracking Template:**
- `completion-tracker-tmpl.yaml` - Template for tracking placeholder completion progress

**Agent Commands for Self-Improvement:**
- `*review-placeholders` - Show all incomplete items
- `*complete-item [ID]` - Guide user through completing specific placeholder
- `*status` - Show completion progress
- `*prioritize` - Help user prioritize which placeholders to address first

**User Reminders:**
Agent will periodically remind user about incomplete items:
- "I notice we still have [N] areas to refine. Would you like to work on any of them?"
- "Your agent has [N] placeholders. The highest priority ones are: [list]"
- "Ready to make your agent even better? Let's complete [specific item]"

**MOMENTUM PRESERVATION:**
"You've done incredible thinking here. I've tracked [N] areas for future refinement, but your agent will be fully functional right away. Ready to see your vision come to life?"

**COMPLETION GUARANTEE:**
Ensure the created agent includes self-improvement capabilities:
- **Placeholder Inventory File**: `completion-status.md` documenting all skipped items
- **Built-in Refinement Tasks**: Tasks specifically for completing each type of placeholder
- **Progress Tracking**: Agent tracks and reports completion progress
- **User Guidance**: Agent provides step-by-step guidance for completing each placeholder
- **Periodic Reminders**: Agent reminds user about incomplete areas during normal usage

**SKIP SUMMARY:** "Great session! I tracked [N] items you skipped and created smart placeholders for all of them. Your agent will work perfectly right away AND help you complete these areas whenever you're ready."

**SUCCESS HANDOFF:**
"Your agent is ready to use immediately AND will help you complete the remaining [N] placeholders over time. It's designed to grow smarter as you provide more information!"

## Success Criteria

- User is energized and excited about their agent vision
- All critical aspects identified, others marked for discovery
- Requirements are specific, actionable, and well-defined
- User confirms completeness and accuracy of gathered requirements
- Clear priority understanding and file mapping validated
- User ready and eager to proceed with agent creation

## Dependencies

- References: `/data/brainstorming-techniques.md` for detailed elicitation methods
- References: `/data/answer-mapping-guide.md` for detailed mapping rules
- References: `/data/incomplete-session-handling.md` for adaptive strategies
- Uses: `/templates/session-output-tmpl.yaml` for structured documentation