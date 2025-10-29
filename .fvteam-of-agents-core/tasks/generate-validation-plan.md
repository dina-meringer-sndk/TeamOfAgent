# Generate Validation Plan Task

## Purpose

To generate comprehensive FVT validation plans using the analyzed strategy requirements, applying 15+ years of domain expertise and following the FVT Validation Plan Template structure for both Word and Confluence output.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Plan Structure Initialization

**Load FVT Validation Plan Template structure:**
- Administrative sections: Revision History, Table of Contents
- Overview: Introduction, General Information, Reference Documents, Terms
- Context: Background, Validation Strategy narrative
- Core Content: Test Cases organized by type hierarchy
- Requirements: External Dependencies (FW/Livet/VTF/CTF/SV Infra)
- Issues: Open Issues tracking

**Initialize document metadata:**
- Package Name: [From analysis]
- SV POC: [User provided]
- FW POC: [User provided] 
- Environment: Model/HW [From analysis]
- Project: [User provided]
- Protocols: [From feature analysis]
- VLD branch location: [User provided]
- VLD epic: [User provided]

### 2. Validation Strategy Narrative Generation

**Create comprehensive strategy description based on analysis:**

**Feature Background Integration:**
- Synthesize feature purpose and architecture context
- Include relevant flow charts and technical diagrams
- Reference architecture/design document insights
- Establish validation approach rationale

**Strategy Approach Definition:**
- DVT black-box approach: Host-facing validation without internal events
- FVT grey-box approach: Internal event validation where needed
- Performance/latency focus: Real measurement requirements
- Error injection strategy: Model vs HW capability allocation
- Cross-feature validation: Dependency testing approach

**Test Philosophy Statement:**
- "Basic flow will verify proper behavior using [counters/waypoints/data integrity]"
- "Tests will include exceptions of different types to verify proper feature behavior"
- "Majority of tests will run on [Model/HW] since [specific technical rationale]"
- Integration with brownfield validation framework approach

### 3. Test Case Generation by Hierarchy

**Apply test organization hierarchy: Test Type → Environment → Feature Area**

#### 3.1 Preconditions (Optional)
**Generate if needed based on feature complexity:**
- Precondition Name: [Descriptive name]
- Integration Phase: [1 or 2 based on complexity]
- Platform: Model/HW/HAPS
- Description: High-level precondition setup
- Flow: Step-by-step precondition establishment with verification points

#### 3.2 Functional Tests (Phase 1 - Basic Functionality)
**For each core functional requirement:**
- Test Name: Test_D_[FeatureArea]_[Purpose] (descriptive, indicates flow)
- Priority: [Defined with SV Architect input]
- Integration Phase: 1 (basic functionality)
- Platform: [Model/HW based on technical needs]
- Description: High-level test purpose and scope
- Precondition: [Reference if needed]
- Test Flow: Detailed step-by-step procedure with verification points
- Covers Polarion item: [Requirement traceability]
- Jira Test Case: [Project tracking]

#### 3.3 Invalid Input Tests
**Generate invalid input scenarios:**
- Boundary condition testing
- Malformed command validation
- Out-of-range parameter testing
- Invalid state transition attempts

#### 3.4 Exception Handling Tests
**Comprehensive exception coverage:**

**Read Failures:**
- Simulated read errors using appropriate injection method
- Error recovery validation
- Host notification verification

**Program Failures:**
- Program operation failure scenarios
- Error handling and recovery flows
- Data integrity verification after failures

**Erase Failures:**
- Erase operation failure simulation
- Block management verification
- Recovery mechanism validation

#### 3.5 Reset, Abort, and VDET Tests
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

#### 3.6 Cross Features (Phase 2)
**Integration testing with other features:**
- Feature interaction scenarios
- Dependency validation
- Concurrent operation testing

#### 3.7 Performance Tests (Final Phase - PLPT)
**Test_D_[Feature]_PLPT naming convention:**
- Performance measurements (no randomization)
- Latency validation (deterministic parameters)
- Power consumption testing (fixed conditions)
- Thermal behavior validation (controlled environment)

#### 3.8 Specialized Testing
**Based on feature requirements:**

**Smart Report:** Counter verification if applicable
**Customer Scenarios:** Real-world trace validation
**Stress Testing:** Link to Cyclone test design doc
**Platform Testing:** Link to Platform test design doc

### 4. External Requirements Generation

**Systematic dependency identification:**

#### 4.1 FW Requirements

**Waypoints (Model-only):**
- Name: [Descriptive waypoint name]
- Parameters: [Required parameters]
- Description: [Purpose and usage]
- Status: Exist/Not Exist/Requires Modification

**FBCC (Customer diagnostic access):**
- Name: [FBCC capability name]
- Parameters: [Access parameters]
- Description: [Diagnostic purpose]
- Status: Exist/Not Exist/Requires Modification

**ATB Events (Internal monitoring):**
- Name: [Event name]
- Parameters: [Event parameters]
- Description: [Monitoring purpose]
- Status: Exist/Not Exist/Requires Modification

#### 4.2 Infrastructure Requirements

**Livet (Model environment):**
- Error injection capabilities needed
- Timing control requirements
- Specific simulation needs

**VTF/CTF (Validation frameworks):**
- New SPEC feature attribute support
- Framework enhancements needed
- Compatibility requirements

**SV Infra (System validation infrastructure):**
- Test environment setup needs
- Tool and utility requirements
- Reporting and analysis capabilities

### 5. Quality Assurance Integration

**Apply failure mode prevention:**
- Verify no missing edge cases through systematic boundary analysis
- Confirm infrastructure requirements are complete and feasible
- Validate environment assignments match technical constraints
- Ensure coverage addresses all stakeholder perspectives
- Check test descriptions are sufficiently detailed
- Verify document organization follows template hierarchy
- Confirm traceability from requirements to test cases

**Stakeholder validation:**
- System Architect: Coverage aligns with feature objectives
- FW Engineer: Requirements are technically feasible and reasonable
- Validation Engineer: Tests are executable with clear procedures

### 6. Document Generation

**Generate Word document following FVT template:**
- Complete all template sections with generated content
- Include tables with proper formatting
- Add charts and diagrams where beneficial
- Ensure professional formatting and structure

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

- Complete FVT validation plan generated following template structure
- All test cases properly organized by hierarchy with detailed procedures
- Infrastructure requirements comprehensively identified
- Word and Confluence formats generated
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

Complete FVT validation plan in Word format, Confluence content, infrastructure requirements summary, and implementation roadmap ready for stakeholder review and execution.