# Generate Validation Plan Task

## Purpose

To generate comprehensive validation plans using the analyzed strategy requirements, applying 15+ years of domain expertise and following the Validation Plan Template structure for both Word and Confluence output.

## Knowledge Base Integration

**Load and apply comprehensive domain expertise from existing knowledge bases. This knowledge is for design decisions but should NOT be included as detailed explanations in validation plan documents.**

### Required Knowledge Base Files
1. **domain-expertise-database.md** - Load complete 15+ years validation engineering expertise
2. **validation-testing-environments.md** - Load complete environment capabilities and constraints

### Application Instructions
- Apply all strategic frameworks from domain-expertise-database.md
- Use environment decision matrix from validation-testing-environments.md
- Follow validation method hierarchy and quality assurance frameworks
- Reference but do not duplicate methodology explanations in output documents

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Plan Structure Initialization

**Load Validation Plan Template structure:**
- Administrative sections: Revision History, Table of Contents
- Overview: Introduction, General Information, Reference Documents, Terms (ONLY feature-specific abbreviations directly used in testing - exclude generic industry terms like JEDEC, ATB, UFS unless they are central to the feature functionality)
- Context: Background, Validation Strategy narrative
- Core Content: Test Cases organized by type hierarchy
- Requirements: External Dependencies (FW/Livet/VTF/CTF)
- Issues: Open Issues tracking

**Initialize document metadata:**
- Package Name: [From analysis]
- SV POC: [User provided]
- FW POC: [User provided] 
- Environment: Model/HW [From analysis]
- Project: [From analysis]
- Protocols: [From analysis]
- VLD epic: [User provided]

**CRITICAL**: For Terms and Abbreviations section, include ONLY:
- Feature-specific acronyms that appear in test procedures
- EXCLUDE generic industry terms (JEDEC, ATB, UFS, etc.) unless they are central to the specific feature
- EXCLUDE general validation terms (DVT, FVT) unless they are part of test names

### 2. Validation Strategy Narrative Generation

**Create comprehensive strategy description based on analysis:**

**Feature Background Integration:**
- Synthesize feature purpose and architecture context
- Include relevant flow charts and technical diagrams
- Reference architecture/design document insights
- Establish validation approach rationale

**Strategy Approach Definition:**
- Environment allocation: Apply validation-testing-environments.md decision matrix and capabilities
- Test approach: Apply domain-expertise-database.md strategic hierarchy (DVT black-box, FVT grey-box with justification)
- Performance/latency focus: Follow PLPT constraints
- Error injection strategy: Leverage Model precision vs Hardware authenticity per environment capabilities
- Cross-feature validation: Apply evidence-based decision framework

**Test Philosophy Statement:**
- "Basic flow will verify proper behavior using [Smart Report/HBA counters/FBCC diagnostics] following validation method hierarchy"
- "Tests will include exceptions of different types to verify proper feature behavior"
- "Environment distribution: [X%] Model for [precise control rationale], [Y%] Hardware for [real measurement rationale] per environment decision matrix"
- Integration with brownfield validation framework leveraging established capabilities
- Apply host-centric validation approach focusing on customer-observable behavior

**IMPORTANT**: Do NOT include detailed explanations of DVT/FVT methodologies in the validation plan document. These are covered in the knowledge base and should only be referenced for test design decisions.

**Apply Knowledge Base Frameworks:**
- Use environment decision matrix for technical allocation decisions
- Apply validation method hierarchy: Smart Report → HBA counters → FBCC → ATB events (last resort with justification)
- Follow test organization mastery: Test Type → Environment → Feature Area
- Apply quality assurance checks from multi-stakeholder perspectives

### 3. Test Case Generation by Hierarchy

**Apply test organization hierarchy: Test Type → Environment → Feature Area (per domain-expertise-database.md)**

**Environment Selection:** Apply validation-testing-environments.md decision matrix:
- Model: When precise control needed (temperature, waypoints, complex error injection)
- Hardware: When real measurements required (power, latency, performance)
- Platform: When real-world ecosystem validation needed


#### 3.1 Preconditions (Optional)
**Generate if needed based on feature complexity:**
- Precondition Name: [Descriptive name]
- Integration Phase: [1 or 2 based on complexity]
- Platform: Model/HW/HAPS
- Description: High-level precondition setup
- Flow: Step-by-step precondition establishment with verification points

#### 3.2 Functional Tests (Phase 1 - Basic Functionality)
**For each core functional requirement (apply host-centric validation approach):**
- Test Name: Test_D_[FeatureArea]_[Purpose] (descriptive, indicates flow)
- Priority: [Apply evidence-based decision framework]
- Integration Phase: 1 (basic functionality)
- Platform: [Apply environment decision matrix from validation-testing-environments.md]
- Description: High-level test purpose and scope (focus on host-observable behavior)
- Precondition: [Reference if needed]
- Test Flow: Detailed step-by-step procedure with verification points using validation method hierarchy
- Covers Polarion item: [Requirement traceability]
- Jira Test Case: [Project tracking]

#### 3.3 Invalid Input Tests
**Generate invalid input scenarios:**
- Boundary condition testing
- Malformed command validation
- Out-of-range parameter testing
- Invalid state transition attempts

#### 3.4 Reset, Abort, and VDET Tests
**System robustness validation:**

**GSD (Graceful Shutdown):**
- Normal shutdown procedure validation
- Data persistence verification
- State preservation testing

**UGSD/Aborts:**
- Ungraceful shutdown scenarios
- Abort handling validation
- Recovery after unexpected termination

**VDET (Vendor Defined Error Threshold):**
- Error threshold configuration testing
- VDET trigger validation
- Error reporting verification

#### 3.5 Cross Features (Phase 2)
**Integration testing with other features:**
- Feature interaction scenarios
- Dependency validation
- Concurrent operation testing

#### 3.6 Performance Tests (Final Phase - PLPT)
**Test_D_[Feature]_PLPT naming convention (apply PLPT constraints from validation-testing-environments.md):**
- Performance measurements (NEVER randomize - per domain-expertise-database.md)
- Latency validation (deterministic parameters for version comparison)
- Power consumption testing (Hardware mandatory for real measurements)
- Thermal behavior validation (Model acceptable for precise control, Hardware for authentic stress)

**Critical PLPT Rules:**
- Hardware environment mandatory for: Power, current consumption, performance, latency
- Model acceptable for: Thermal simulation with precise temperature control
- Never randomize any parameters (version comparison integrity)
- Identical conditions required for "apples to apples" comparison

#### 3.7 Specialized Testing
**Based on feature requirements:**

**Smart Report:** Counter verification if applicable
**Customer Scenarios:** Real-world trace validation
**Stress Testing:** Link to Cyclone test design doc
**Platform Testing:** Link to Platform test design doc

### 4. External Requirements Generation

**Systematic dependency identification using infrastructure knowledge:**

#### 4.1 FW Requirements

**Waypoints (Model-only per validation-testing-environments.md):**
- Name: [Descriptive waypoint name]
- Parameters: [Required parameters]
- Description: [Purpose and usage - justify why timing control needed]
- Status: Exist/Not Exist/Requires Modification
- **Justification Required**: Why Smart Report/HBA counters/FBCC insufficient

**FBCC (Customer diagnostic access - higher priority than ATB):**
- Name: [FBCC capability name]
- Parameters: [Access parameters]
- Description: [Diagnostic purpose]
- Status: Exist/Not Exist/Requires Modification

**ATB Events (Last resort per domain-expertise-database.md):**
- Name: [Event name]
- Parameters: [Event parameters]
- Description: [Monitoring purpose]
- Status: Exist/Not Exist/Requires Modification
- **Mandatory Justification**: Why Smart Report/HBA/FBCC cannot cover the required flows

#### 4.2 Infrastructure Requirements

**Apply validation-testing-environments.md constraints:**

**Livet (Model environment):**
- Error injection capabilities needed (specify precision requirements)
- Timing control requirements (justify waypoint necessity)
- Temperature simulation needs (vs oven testing trade-offs)

**VTF/CTF (Validation frameworks per validation-testing-environments.md):**
- SPEC feature attribute support (only if new attributes added - rare case)
- Framework enhancements needed (document specific requirements)
- Compatibility requirements (brownfield integration)

### 5. Quality Assurance Integration

**Apply domain-expertise-database.md quality assurance framework:**

**Evidence-Based Decision Framework:**
- Verify environment assignments match technical capabilities (per validation-testing-environments.md)
- Confirm infrastructure requirements are complete and feasible
- Validate validation method hierarchy properly applied (Smart Report → HBA → FBCC → ATB)
- Check SDR capacity vs command intensity calculations

**Multi-Stakeholder Perspective Validation:**

**Validation Engineer Perspective:**
- End-to-end workflow validation from host perspective prioritized
- Host-centric validation approach properly applied
- Strategy baseline compliance with extension for missed cases
- Automation requirements (fully automatic, no manual intervention) met

### 6. Document Generation

**Generate Markdown validation plan:**
- Create complete validation plan in Markdown format
- Use filename: `{feature_name}_Validation_Plan.md`
- Include all template sections with generated content
- Ensure proper Markdown formatting and structure

**Generate Word document using docx_utils:**
- Import and use `docx_utils.create_docx_from_md()` function from `.fvteam-of-agents-core/utils/`
- Read the generated Markdown file content
- Convert to Word document format using: `create_docx_from_md(md_content, '{feature_name}_Validation_Plan.docx')`
- Ensure professional formatting with proper headings and structure
- Save in same directory as Markdown file

**Generate Confluence content:**
- Convert Word content to Confluence format
- Maintain structure and readability
- Include proper links and navigation
- Enable collaborative review and updates

### 7. Final Validation and Handoff

**Execute comprehensive review:**
- All template sections completed
- Test naming conventions followed
- Environment assignments technically sound
- Infrastructure requirements complete
- Traceability established
- Quality standards met

**Present to user:**
- Complete validation plan documentation
- Summary of key decisions and rationale
- Infrastructure setup timeline
- Next steps for implementation

## Success Criteria

- Complete validation plan generated following template structure
- All test cases properly organized by hierarchy with detailed procedures
- Infrastructure requirements comprehensively identified
- **Both Markdown (.md) and Word (.docx) formats generated automatically**
- Word document properly formatted using docx_utils conversion
- Quality assurance validation passed
- Stakeholder review readiness confirmed
- Zero gaps in coverage or technical feasibility

## Blocking Conditions

- Incomplete strategy analysis input
- Unresolved infrastructure capability questions
- Missing technical context for environment decisions
- Template structure violations
- Quality compliance failures
- Stakeholder requirement conflicts

## Output Format

Complete validation plan in **both Markdown (.md) and Word (.docx) formats**, Confluence content, infrastructure requirements summary, and implementation roadmap ready for stakeholder review and execution.

**Required Deliverables:**
1. `{feature_name}_Validation_Plan.md` - Complete Markdown validation plan
2. `{feature_name}_Validation_Plan.docx` - Professionally formatted Word document (auto-generated using docx_utils)
3. Confluence-ready content formatting
4. Infrastructure requirements summary
5. Implementation roadmap