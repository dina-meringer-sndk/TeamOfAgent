# Integrate Domain Knowledge Task

## Purpose

Apply 15+ years of validation engineering expertise to analyze requirements and integrate comprehensive domain knowledge for gap-free validation plan generation.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Domain Knowledge Loading and Application

**Load domain knowledge from data files:**
- **domain-expertise-database.md**: Load 15+ years validation engineering expertise, strategic decision-making patterns, test organization hierarchy, and stakeholder alignment expertise
- **validation-testing-environments.md**: Load environment capabilities (Model/HW/Oven/Platform), infrastructure constraints, test type constraints, and randomization rules
- **failure-mode-analysis.md**: Load comprehensive failure prevention framework, process failure modes, and quality assurance patterns

**Apply core expertise areas from loaded knowledge:**
- DVT/FVT testing methodologies and constraints (from domain-expertise-database.md)
- Model vs HW environment capabilities and limitations (from validation-testing-environments.md)
- Error injection techniques and feasibility (from validation-testing-environments.md)
- Infrastructure requirements - CTF/CVF, waypoints, ATB events (from validation-testing-environments.md)
- Performance testing protocols and restrictions (from validation-testing-environments.md)

**Apply validation philosophy from domain expertise:**
- Host-centric external behavior focus (from domain-expertise-database.md)
- Black-box vs grey-box approach selection (from domain-expertise-database.md)
- End-to-end systematic validation (from domain-expertise-database.md)
- Strategy gap identification through expert analysis (from domain-expertise-database.md)

### 2. Technical Constraint Integration (from validation-testing-environments.md)

**Environment Capability Assessment (load from validation-testing-environments.md):**
- Model advantages: Precise temperature, waypoints, error injection
- HW advantages: Real measurements (power, current, performance, latency)
- Platform needs: Real-world integration scenarios

**Infrastructure Requirement Analysis (load from validation-testing-environments.md):**
- CTF/CVF needs for SPEC features (UFS, NVMe)
- Waypoint requirements for timing control
- ATB event needs for internal monitoring
- FBCC requirements for diagnostic access

### 3. Test Strategy Expertise Application (from domain-expertise-database.md)

**Test Type Classification (load from domain-expertise-database.md):**
- DVT black-box: Host-facing, portable, no internal dependencies
- FVT grey-box: Internal process awareness, limited portability
- Performance/PLPT: Never randomized, real measurements required
- Stress testing: Cyclone allocation for high-throughput needs

**Randomization Strategy (load from domain-expertise-database.md):**
- Strategic randomization for coverage optimization
- Never randomize: Performance, latency, power, thermal parameters
- Configuration randomization for multiple combination coverage
- Version comparison integrity maintenance

### 4. Gap Analysis Using Expert Pattern Recognition (from failure-mode-analysis.md)

**Systematic Gap Detection (load patterns from failure-mode-analysis.md):**
- Coverage gaps: Missing user scenarios or edge cases
- Technical gaps: Infrastructure requirements not identified
- Integration gaps: Cross-feature interactions not considered
- Regression gaps: Backward compatibility not addressed

**Expert "Think Outside the Box" Analysis (apply domain-expertise-database.md methodology):**
- Question assumptions in original strategy
- Consider edge cases not explicitly mentioned
- Evaluate cross-feature dependencies using experience
- Assess failure modes based on historical patterns (from failure-mode-analysis.md)
- Identify customer scenarios beyond specification

### 5. Stakeholder Perspective Integration (from domain-expertise-database.md)

**System Architect Expertise (load from domain-expertise-database.md stakeholder alignment section):**
- System-level integration considerations
- Cross-feature dependency analysis (power, performance, security)
- Requirement traceability enforcement
- Product integration risk assessment

**FW Engineer Expertise (load from domain-expertise-database.md stakeholder alignment section):**
- Internal state machine validation approaches
- Error handling and recovery flow requirements
- Infrastructure feasibility assessment
- Low-level boundary condition identification

**Validation Engineer Expertise (load from domain-expertise-database.md stakeholder alignment section):**
- End-to-end workflow execution considerations
- Coverage gap identification between FW unit and system testing
- Test efficiency optimization strategies
- Resource allocation and prioritization guidance

### 6. Quality Standards Integration (from failure-mode-analysis.md and domain-expertise-database.md)

**Enterprise Quality Application (load from domain-expertise-database.md automation section):**
- Apply 15+ years of quality standards and best practices
- Integrate failure mode prevention based on experience (from failure-mode-analysis.md)
- Apply systematic validation methodologies
- Ensure compliance with industry standards and regulations

**Continuous Improvement Integration (load from domain-expertise-database.md):**
- Lessons learned from previous validation projects
- Best practice application across similar features
- Process optimization based on experience
- Knowledge transfer and documentation standards

### 7. Domain Knowledge Synthesis (integrate all data sources)

**Create integrated knowledge assessment using all data files:**
- Technical feasibility validation using domain expertise (domain-expertise-database.md)
- Risk assessment based on failure mode patterns (failure-mode-analysis.md)
- Resource requirement estimation using environment constraints (validation-testing-environments.md)
- Timeline validation based on similar project patterns (domain-expertise-database.md)

**Generate expert recommendations from integrated knowledge:**
- Priority areas based on risk and impact assessment (failure-mode-analysis.md)
- Infrastructure setup sequence based on experience (validation-testing-environments.md)
- Test execution strategy optimized for efficiency (domain-expertise-database.md)
- Quality assurance approach tailored to feature complexity (failure-mode-analysis.md)

### 8. Knowledge Integration Validation

**Expert review of integration:**
- Verify all domain knowledge areas properly applied
- Confirm technical constraints accurately assessed
- Validate stakeholder perspectives comprehensively integrated
- Ensure quality standards appropriately applied

**Integration completeness check:**
- All expertise areas covered
- No conflicting recommendations
- Stakeholder alignment achieved
- Quality standards met

## Success Criteria

- All 15+ years of domain expertise appropriately applied
- Technical constraints accurately integrated
- Stakeholder perspectives comprehensively considered
- Gap analysis complete using expert pattern recognition
- Quality standards and best practices applied
- Knowledge synthesis ready for validation plan generation

## Blocking Conditions

- Insufficient strategy analysis input
- Unresolved technical constraint questions
- Missing stakeholder perspective information
- Incomplete domain knowledge application
- Quality standards not met

## Output Format

Comprehensive domain knowledge integration report including technical assessments, gap analysis, stakeholder considerations, and expert recommendations ready for validation plan generation.