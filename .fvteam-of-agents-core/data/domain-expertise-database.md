# Domain Expertise Database

## 15+ Years Validation Engineering Knowledge

### Strategic Validation Philosophy

#### Host-Centric Validation Approach
**Core Principle**: Focus on what the host can experience from the outside
- Instead of verifying internal state machines → Ask what flows reach each state machine
- Instead of internal validation → Focus on host end result if device doesn't follow state machine
- **Benefit**: Tests remain valid even if FW changes internal design
- **Application**: Systematic end-to-end validation from host perspective

#### Test Strategy Hierarchy

**DVT - Black-box Approach:**
- **Mindset**: Verify device as black box without ATB event reliance
- **Portability**: Tests should be portable across projects without changes
- **Environment Agnostic**: Should work on both HW and Model
- **Exception**: ATB events acceptable for abort/VDET within specific locations
- **Customer Verifiability**: If using internal data, must be customer-accessible (e.g., Smart Report)

**FVT - Grey-box Approach:**
- **Mindset**: Include awareness of internal device processes
- **Tool Usage**: Typically rely on internal events and waypoints
- **Portability**: Limited to extent that events/waypoints don't change
- **Change Impact**: Typically non-negligible changes required across projects

### Strategic Decision Making

#### Environment Selection Strategy
**Decision Framework**: Choose environment based on validation goals, not technical convenience
- **Model Selection**: When precision control outweighs real measurement needs
- **HW Selection**: When authentic measurements are validation-critical
- **Cyclone Selection**: When command intensity exceeds framework limitations
- **Platform Selection**: When real-world ecosystem interactions are essential

#### Randomization Strategy Expertise

**Strategic Randomization Principles:**
- **Purpose**: Handle excessive configuration combinations efficiently
- **Method**: Randomize parameters to cover all cases over multiple executions
- **Efficiency**: Avoid creating hundreds of tests for configuration coverage
- **Coverage**: All cases covered through repeated randomized execution

**Never Randomize Categories:**
- **Performance Testing**: Latency, performance metrics
- **Power Testing**: Power consumption, current consumption
- **Measurement Validation**: Any comparative measurements
- **Rationale**: Version comparison integrity requires identical conditions

**Randomization Candidates:**
- **Configuration Parameters**: Multiple device configuration options
- **Test Sequences**: When order doesn't affect core functionality
- **Data Patterns**: When specific patterns not functionally critical
- **Environmental Conditions**: When variation increases coverage

### Advanced Strategic Decision Making

#### Test Organization Mastery

**Hierarchical Test Organization:**
1. **First Level**: Test Type (DVT/FVT/Performance/Stress/Platform)
2. **Second Level**: Environment (Model/HW/Oven/Platform)
3. **Third Level**: Feature Area

**Integration Phase Strategy:**
- **Phase 1**: Basic functionality (Test_D_ prefix)
- **Phase 2**: Cross-feature integration, stress testing
- **Final Phase**: PLPT (Performance/Latency/Power/Thermal)

**Test Naming Conventions:**
- **Test_D_**: Direct tests (basic functionality)
- **Test_R_**: Random tests (coverage optimization)
- **Test_D_[Feature]_PLPT**: Performance/Power/Latency/Thermal tests
- **Descriptive Names**: Short but clear indication of test flow/purpose

### Quality Assurance Expertise

#### Evidence-Based Decision Framework

**Infrastructure Requirements Validation:**
- **SPEC Features**: Only flag CTF/CVF when new attributes are added
- **High-Throughput**: Calculate command intensity before suggesting Cyclone
- **Timing Validation**: Exhaust Smart Report/HBA/FBCC before ATB/waypoints
- **Cross-Feature**: Require architectural documentation for interaction claims

**Validation Method Hierarchy:**
1. **Primary**: Smart Report analysis
2. **Secondary**: HBA counters monitoring
3. **Tertiary**: FBCC diagnostics
4. **Last Resort**: ATB events/waypoints (with justification)

#### Feature-Specific Analysis Principles

**System Architect Perspective:**
- Feature coverage alignment with system requirements
- Cross-feature dependencies (power, performance, security)
- Traceability from requirements to validation
- System-level gap prevention

**FW Engineer Perspective:**
- Internal state machine and error handling coverage
- Negative testing and recovery flow validation
- Test realism with actual FW hooks and debug tools
- Low-level boundary condition coverage

**Validation Engineer Perspective:**
- End-to-end workflow validation from host perspective
- Edge case and combination coverage beyond specification
- Strategy baseline compliance with extension for missed cases
- Coverage gap identification between FW unit and system validation
- Efficiency optimization with proper prioritization

### Automation and Framework Integration

**Full Automation Requirements:**
- All tests must run completely automatically
- No manual intervention allowed
- Self-contained execution and validation
- Automated pass/fail determination

**Brownfield Framework Integration:**
- Work with existing validation framework
- Understand framework capabilities and limitations
- Generate tests compatible with framework patterns
- Leverage framework strengths while compensating for gaps

**Test Structure Standardization:**
- **Preconditions**: Device configuration (strict or randomized) + state setup
- **Main Flow**: Core test execution sequence
- **Pass/Fail Criteria**: Predefined success/failure determination
- **Verification Points**: Systematic validation throughout execution

### Meta-Strategic Knowledge

#### Expertise Application Patterns
**When to Apply Deep Technical Knowledge**: 
- Environment selection requires understanding technical trade-offs
- Test design needs infrastructure constraint awareness
- Failure mode analysis demands technical feasibility assessment

**When to Apply Strategic Thinking**:
- Gap analysis requires thinking beyond provided specifications
- Stakeholder alignment needs perspective-taking and requirement synthesis
- Quality assurance demands systematic failure mode prevention

**When to Apply Domain Experience**:
- Test organization benefits from proven hierarchical patterns
- Randomization strategies leverage 15+ years of coverage optimization
- Automation integration requires framework compatibility expertise

This expertise database serves as the foundation for all validation planning decisions, ensuring comprehensive coverage while maintaining technical feasibility and stakeholder satisfaction.