# Validation Strategy Analysis Guide

## Purpose

Analyze architecture and validation strategy documents to create a comprehensive, structured Markdown report for the Validation Plan Creator agent. This involves deep document analysis, interactive user clarification, and systematic gap identification.

## Core Objectives

1. **Extract complete feature understanding** from strategy and architecture documents
2. **Verify technical implementation details** through targeted user interaction
3. **Identify validation gaps and missing coverage** systematically
4. **Generate structured analysis report** containing all necessary information for validation plan creation

## Process Overview

**4 Sequential Phases:**
1. **Document Collection** (5 min) - Gather strategy, architecture, and supporting documents
2. **Analysis & Verification** (15-20 min) - Extract information and verify understanding with user
3. **Gap Identification** (10 min) - Find missing elements through systematic analysis and user input
4. **Output Generation** (5 min) - Create structured Markdown analysis report

**Total Time: 35-40 minutes**

## Critical Rules

- **Sequential execution**: Complete each phase before proceeding to the next
- **User interaction**: Wait for user responses before continuing
- **Complete extraction**: Capture specific technical identifiers, not generic descriptions
- **Comprehensive output**: Include ALL conversation content in narrative format

## Phase 1: Document Collection

**Ask for documents in sequence:**

1. **"Please provide your validation strategy document (Word/PDF format)"**
   - Wait for strategy document upload

2. **"Please provide the architecture document referenced in the strategy"**  
   - Wait for architecture document upload

3. **"Upload any additional charts, diagrams, or reference materials (optional)"**
   - Wait for response (may be "none")

**Only proceed to Phase 2 after receiving all documents.**

## Phase 2: Analysis & Verification

**Extract information from documents FIRST, then verify understanding through targeted questions.**

### 2.1 Feature Understanding

**Document Analysis:**
- Extract core feature functionality and purpose
- Identify feature scope, boundaries, and variants
- Map use cases and customer scenarios
- Understand business value and impact

**Present complete understanding:**
*"Based on analysis of your documents, here's my understanding of this feature: [detailed feature description including functionality, purpose, scope, and use cases]"*

**Verification Questions (1-3 max):**
- Ask only about unclear boundaries or missing use cases
- Wait for each response before proceeding

### 2.2 Technical Implementation  

**Document Analysis:**
- Extract architectural components and dependencies
- Identify protocols, interfaces, and technical mechanisms
- Find specific technical identifiers (counters, parameters, state machines)
- Map system integration points

**Present complete technical understanding:**
*"Here's my understanding of the technical implementation: [system integration, dependencies, protocols, specific technical components]"*

**Verification Questions (1-3 max):**
- Ask only about missing technical dependencies or unclear implementation details
- Wait for each response before proceeding

### 2.3 Test Environment & Coverage

**Document Analysis:**
- Extract test environment requirements (Model, HW, Platform)
- Identify performance measurements and specialized hardware
- Understand coverage scope and pass/fail criteria

**Verification Questions (1-4 max):**
- "Test environments specified: [extracted info]. Any additional environments needed?"
- "Performance measurements mentioned: [extracted info]. Any additional measurements required?"
- "Coverage scope described: [extracted info]. Any missing edge cases or criteria?"
- Wait for each response before proceeding

## Phase 3: Gap Identification

**Systematic analysis with mandatory user confirmation for all gaps.**

### 3.1 Technical Detail Extraction

**CRITICAL REQUIREMENT: Create comprehensive Technical Inventory**

**MANDATORY TECHNICAL INVENTORY - COMPREHENSIVE EXTRACTION:**
The analysis MUST contain a dedicated "Technical Inventory" section within "Feature Overview and Technical Inventory" that lists EVERY technical identifier found in the documents. Generic descriptions are NOT ACCEPTABLE.

**Extract ALL Technical Names and Identifiers (exact names, not descriptions):**

**Hardware/Firmware Identifiers:**
- Counters/Registers, FBCC Commands/Parameters, State Machine States, Interface Names
- Error Codes/Messages, Configuration Parameters, Memory/Buffer Names, Register Addresses

**Software/Protocol Identifiers:**  
- Command Opcodes, Status Fields, Event/Alert Names, Protocol Specifications
- Module/Component Names, Test Point Names, Debug/Trace Names, Threshold Values

**CRITICAL:** Extract actual names (e.g., `FBCC_TIMEOUT_ERROR`, `performance_counter_0x1001`) not generic descriptions (e.g., "error handling mechanism"). Include ANY OTHER TECHNICAL IDENTIFIER found in documents.

**VALIDATION CHECKPOINT:** Before completing analysis, verify Technical Inventory contains EVERY ACTUAL TECHNICAL NAME AND IDENTIFIER found in documents. If specific technical identifiers are not found, explicitly state: "Technical identifiers not specified in documents - requires clarification from stakeholders"

### 3.2 Infrastructure Analysis

**Feature-Specific Infrastructure Analysis:**
- SPEC Feature Infrastructure: CTF/CVF requirements analysis
- High-Throughput Requirements: Cyclone requirement calculation (>500K commands)
- Timing Validation Methods: Smart Report, HBA Counters, FBCC Diagnostics, ATB/waypoint needs

**For each potential infrastructure need:**
1. Present analysis: "This feature appears to require [specific infrastructure] because [technical justification]"
2. Ask user: "Do you confirm this infrastructure requirement?"
3. Record only confirmed requirements

### 3.3 Coverage Gap Analysis

**MANDATORY USER INPUT FOR GAPS:** Present each potential gap to user and ask for confirmation before considering it a gap.

**Analysis Categories:**
- Test Type Coverage: DVT black-box, FVT grey-box, Performance, Platform testing
- Verification Level Assessment: Python-level vs Firmware-level verification needs
- Cross-Feature Interactions: Based on architectural dependencies in documents
- Edge Cases and Scenarios: Missing critical scenarios with technical specifications

**For each potential coverage gap:**
1. Present analysis: "I don't see coverage for [specific scenario] in the strategy"
2. Ask user: "Should this scenario be included in validation?"
3. Record only confirmed gaps

### 3.4 Assumption Validation

**Assumption Validation (question strategy assumptions):**
- Capability assumptions: Does strategy assume capabilities not verified?
- Environment assumptions: Does strategy assume environment capabilities?
- Integration assumptions: Does strategy assume integration points work?
- Record: [Questionable assumptions: list for clarification]

**For each questionable assumption:**
1. Present concern: "The strategy assumes [specific assumption] but this isn't verified"
2. Ask user: "Can you confirm this assumption is valid?"
3. Record assumptions that need verification

**Ask ONE question at a time and wait for responses.**

### 3.5 Apply Domain Expertise

**Apply domain expertise from data files:**
- Load domain-expertise-database.md for validation strategy principles
- Load validation-testing-environments.md for environment selection criteria  
- Load timing-validation-methodology.md for comprehensive timing validation assessment
- Apply feature-specific analysis rather than generic patterns

**Feature-Specific Context Analysis:**
- Feature type identification: Classify specific feature (SPEC/performance/power/etc.)
- Infrastructure impact assessment: Determine actual infrastructure needs for this specific feature
- Test type requirements: Identify DVT/FVT/Performance requirements based on feature characteristics
- Environment allocation: Select optimal environments based on feature validation needs

## Phase 4: Output Generation

**BEFORE CREATING THE FILE:** Review all content and prepare optimal organization
- **Complete content collection**: Gather ALL validation strategy content, architecture details, and session interactions
- **Content reorganization**: Redistribute all information optimally across the 5 sections for validation planning effectiveness
- **Strategic restructuring**: Organize content by validation planning needs, NOT by source document structure
- **Session synthesis**: Transform all Q&A exchanges, gaps, clarifications, and user insights into narrative format
- **Optimal information flow**: Ensure each section contains the most relevant content for its validation planning purpose
- **Cross-reference validation**: Verify 100% content preservation while achieving optimal organization

### 4.1 Gap Prioritization

**Organize confirmed gaps by priority:**
- **Critical**: Must fix before proceeding (blocking issues)
- **High**: Significant quality impact  
- **Medium**: Process improvement opportunities

### 4.2 Final Content Verification

**MANDATORY PRE-CREATION VALIDATION:** Before generating the analysis file, perform comprehensive verification

**Test Creation Readiness Checklist:**
1. **Feature Behavior Completeness**
   - ✓ All feature triggers and activation conditions documented (specific commands, inputs, states)
   - ✓ Expected behaviors and outputs clearly defined (exact responses, measurements, state changes)
   - ✓ Success/failure criteria specified for each scenario (numerical thresholds, status codes, error messages)
   - ✓ Edge cases and boundary conditions identified (limit values, error conditions, timeout scenarios)

2. **Technical Implementation Details**
   - ✓ All specific technical identifiers captured (exact FBCC commands, counter names, register addresses)
   - ✓ System dependencies and integration points documented (required modules, interfaces, protocols)
   - ✓ Performance thresholds and measurement criteria specified (timing requirements, bandwidth limits, latency targets)
   - ✓ Error conditions and recovery mechanisms detailed (error codes, diagnostic procedures, fallback behaviors)

3. **Test Environment Requirements**
   - ✓ Hardware/platform requirements clearly specified (specific models, configurations, capabilities)
   - ✓ Infrastructure needs documented (CTF/CVF setup, Cyclone requirements, network topology)
   - ✓ Configuration requirements and setup procedures outlined (initialization steps, parameter settings)
   - ✓ Tool and measurement dependencies identified (required software, debug interfaces, monitoring tools)

4. **Validation Coverage Verification**
   - ✓ All test scenarios and use cases covered (positive/negative testing, stress conditions, integration scenarios)
   - ✓ Verification levels specified (Python-level simulation, firmware verification, hardware validation)
   - ✓ Test data and stimulus requirements documented (input patterns, data sets, load conditions)
   - ✓ Pass/fail determination criteria clearly defined (acceptance thresholds, comparison methods, validation procedures)

5. **Gap and Risk Assessment**
   - ✓ All identified gaps documented with priority (missing test coverage, unclear requirements, undefined behaviors)
   - ✓ Risk mitigation strategies outlined (alternative approaches, contingency plans, escalation procedures)
   - ✓ Dependencies and assumptions clearly stated (prerequisite conditions, external dependencies, system assumptions)
   - ✓ Follow-up actions and clarifications needed specified (stakeholder contacts, additional documentation, verification steps)

**VALIDATION GATE:** Only proceed to file creation if ALL checklist items are verified complete.

### 4.3 Create Analysis Report

**Generate file:** `validation-strategy-analysis-[feature-name]-[date].md`

**Required Structure (exact titles, exact order):**
1. **Feature Motivation and Market Context**
2. **Feature Overview and Technical Inventory** (with mandatory Technical Inventory section)
3. **Architecture and Design Details**
4. **Test Strategy and Validation Methods - Key Points to Be Addressed**
5. **Technical Gaps and Open Issues**

**Essential Content Requirements:**
- **100% content preservation**: ALL validation strategy content, architecture details, and session interactions included
- **Optimal organization**: Content redistributed across sections for maximum validation planning effectiveness (not source structure)
- **Complete session capture**: Every gap identified, user clarification, confirmation, and insight integrated narratively
- **Strategic content placement**: Information positioned where most useful for validation plan creation
- **Technical Inventory** with specific identifiers (FBCC commands, counters, state machines, etc.)
- **Feature triggers, behavior, and success criteria** for test creation
- **Test environment and infrastructure requirements** clearly specified
- **All identified gaps** (confirmed and potential) with user context and priority
- **User expertise and insights** woven throughout appropriate sections
- **Enhanced analysis**: Original content elevated with session insights and gap analysis

**CRITICAL: Comprehensive Content Integration**
Transform and optimally organize ALL content:
- ❌ Wrong: Copying source document structure or leaving content in original sections
- ✅ Correct: Redistributing ALL content optimally across the 5 validation-focused sections
- Include EVERY gap, user insight, clarification, assumption, and technical detail
- Reorganize information by validation planning utility, not source document organization
- Present all session discoveries as enhanced analysis within appropriate validation contexts
- Ensure each section contains the most strategically relevant content for its validation purpose

**File Creation:** Use create_file tool to generate the analysis document

**Structure Validation:**
- ✓ Uses exact 5 section titles in specified order
- ✓ Technical Inventory contains specific identifiers (not generic descriptions)
- ✓ ALL content optimally redistributed for validation planning effectiveness
- ✓ Complete session content integrated narratively (gaps, insights, clarifications)
- ✓ Information organized by validation utility, not source document structure
- ✓ Enhanced analysis combining original content with user expertise
- ✓ 100% content preservation with optimal organization for validation plan creation
- ✓ **VERIFIED: Contains everything needed for immediate test development without additional clarification**

## Success Criteria

**Analysis Quality:**
- Complete feature understanding verified by user
- All technical implementation details extracted with specific identifiers
- Systematic gap identification with user confirmation
- Infrastructure requirements clearly documented

**Process Efficiency:**
- Completed within 35-40 minutes
- Minimal redundant questions
- User satisfaction with analysis completeness

**Output Completeness:**
- Comprehensive analysis report generated using create_file tool
- All conversation content preserved in narrative format
- **VERIFIED: Complete test development readiness - no additional clarification needed for test creation**
- Ready for validation plan creation

## Blocking Conditions

**Critical blockers that halt the task:**
- Missing validation strategy or architecture documents
- Unanswered verification questions from Phase 2
- Task attempted out of sequence
- Output file not created using the 5 mandatory section structure
- Technical Inventory contains generic descriptions instead of specific identifiers