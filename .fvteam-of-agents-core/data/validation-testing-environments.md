# Validation Testing Environments Knowledge Base

## Environment Capabilities and Constraints

### Model Testing Environment

**Advantages:**
- **Precise Temperature Control**: Can set exact required temperatures vs. oven approximations
- **Waypoint Support**: Stop execution at specific points when HW process is too fast
- **Error Injection Capabilities**: Codeword-level control and complex error scenarios
- **Simulation Flexibility**: Test scenarios difficult or impossible to reproduce in hardware

**Capabilities:**
- Program failure simulation
- Erase failure simulation  
- Factory marked bad blocks
- Power loss scenarios
- Status command failures
- Complex error scenarios with precise control
- Reliable error reproduction

**Limitations:**
- Cannot measure real current consumption
- Cannot measure real power consumption
- Cannot measure real performance metrics
- Cannot measure real latency
- No real-world hardware constraints

**When to Use Model:**
- Precise timing control needed
- Complex error injection required
- Temperature simulation preferred over physical oven
- Waypoint debugging necessary
- Early development phase testing

### Hardware Testing Environment

**Advantages:**
- **Real Measurements**: Actual current consumption, power, performance, latency
- **Higher Confidence**: Closer to real-life conditions
- **Authentic Constraints**: Real hardware limitations and behaviors
- **Customer-Like Environment**: Actual hardware responses

**Capabilities:**
- TMM-based HW error injection test cases
- Basic error types (program failures, erase failures)
- Factory marked bad blocks testing
- Power loss scenarios
- Status command failures
- Real performance and latency measurements
- Actual power and current consumption data

**Limitations:**
- Hard to reach specific temperatures exactly in oven
- Cannot work with waypoints (no precise timing control)
- Limited error injection granularity compared to model
- Less reliable error scenario reproduction

**When to Use Hardware:**
- Real measurements required (performance, power, latency, current)
- Final validation phase
- Customer scenario validation
- Authentic hardware behavior verification

### Oven Testing Environment

**Purpose:**
- Temperature-controlled testing
- Thermal stress validation
- Environmental condition simulation

**Capabilities:**
- Temperature range testing
- Thermal stress scenarios
- Environmental validation

**Limitations:**
- Difficulty reaching exact temperatures
- Model simulation often more precise for temperature control
- Limited to thermal-related testing

**When to Use Oven:**
- Thermal validation required
- Environmental stress testing
- Temperature-related behavior verification

### Platform Testing Environment

**Purpose:**
- Real-life scenario validation using actual OEM phones or chipset evaluation boards
- Comprehensive ecosystem testing

**Capabilities:**
- Real-world data storage scenarios
- File system integration testing
- WiFi, cellular, Bluetooth interaction testing
- Multi-component system validation
- Authentic user scenario reproduction

**When to Use Platforms:**
- System validation (SV) complementary discipline
- Real-life scenarios missed in other disciplines
- Customer environment simulation
- Multi-component interaction testing

## Environment Decision Matrix

### DVT (Design Verification Testing) - Black-box Approach

**Environment Constraints:**
- Must be agnostic to Model vs HW (no internal event dependencies)
- Focus on host-facing external behavior
- Should be portable across projects without changes
- No reliance on ATB events as pass/fail criteria
- Exception: ATB events for abort/VDET within specific locations

**Preferred Environments:**
- Model and HW equally suitable for most DVT tests
- Choose based on measurement requirements, not internal visibility

### FVT (Function Verification Testing) - Grey-box Approach

**Environment Constraints:**
- Can use internal events and waypoints
- Limited portability due to event/waypoint dependencies
- Relies on internal device processes

**Environment Selection:**
- Model: When waypoints and internal timing control needed
- HW: When real measurements and authentic behavior required

### Performance/Latency/Power/Thermal (PLPT) Testing

**Critical Requirements:**
- **NEVER randomize parameters** for version comparison consistency
- Must use identical conditions for "apples to apples" comparison
- Real measurements required

**Environment Requirements:**
- HW mandatory for: Power consumption, current consumption, performance, latency
- Model acceptable for: Thermal simulation with precise control
- Oven alternative for: Temperature testing when precision not critical

## Infrastructure Dependencies

### Waypoint Support
- **Availability**: Model-only capability
- **Purpose**: Stop execution at specific timing points
- **Requirement Detection**: When test needs precise timing control
- **Alternative**: Post-operation state verification for HW testing

### ATB Events
- Guidance for Registration Method Selection:
	- Using ATB events in a test is not a goal, but a last resort. The agent must first consider all other registration methods (Smart report counters, FBCC, HBA counters, diagnostic tools, etc.) for covering the required flows.
	- ATB events should only be used if there is no other way to cover a specific flow, and the agent must document and explain why alternative methods are insufficient.
	- For every test that uses ATB events, the agent must provide a clear justification for their necessity, describing the flows that cannot be validated by other means.
	- Access: Internal-only (not customer accessible)
	- Customer Alternative: FBCC, diagnostic tools
	- DVT Constraint: Cannot rely on ATB events for pass/fail
	- FVT Usage: Allowed for internal process validation, but only when justified as above.

### Error Injection Capabilities

**Hardware Error Injection:**
- TMM-based HW error injection
- Program/erase failures
- Factory marked bad blocks
- Power loss scenarios
- Status command failures

**Model Error Injection:**
- All hardware capabilities PLUS:
- Codeword-level precision control
- Complex error scenarios
- Reliable error reproduction
- Difficult/impossible HW scenarios

## Environment Allocation Strategy

### Phase 1: Basic Functionality
- Prefer Model for early development and debugging
- Use HW when real measurement data needed
- Focus on test stabilization and core functionality

### Phase 2: Cross Features and Stress
- Model for complex interaction scenarios
- Platform for real-world integration scenarios

### Final Phase: PLPT
- HW mandatory for performance measurements
- Model acceptable for controlled thermal testing
- No randomization allowed in any PLPT testing

## Infrastructure Framework Requirements

### CTF (for mobile projects)/CVF (- for PCs and servers) Framework Requirements
**SPEC Feature Dependencies**: CTF/CVF support is required only if there is an addition to the SPEC (rare case). Normally, when a product supports a new SPEC, the CTF group implements all requirements. If a feature is added in a later phase, it will be indicated as a change request in the strategy or architecture file.
**Attribute Support**: UFS, NVMe features may need specific attribute implementation only for such change requests.
**Timeline Impact**: Infrastructure for new features must be ready before test execution, as indicated in the strategy/architecture documentation.
**Prerequisites**: Feature attributes and properties for change requests must be added to the validation framework.

## Test Type Constraints

### DVT (Design Verification Testing) Constraints
**Approach**: Black-box validation
**Constraint**: Must be environment-agnostic (Model/HW compatible)
**Limitation**: No reliance on ATB events for pass/fail criteria
**Portability**: Must survive FW internal design changes
**Exception**: ATB events acceptable for abort/VDET at specific locations
**Customer Verification**: Internal data used must be customer-accessible

### FVT (Function Verification Testing) Constraints
**Approach**: Grey-box validation with internal process awareness
**Constraint**: Limited portability due to internal event dependencies
**Capability**: Can use waypoints and ATB events
**Limitation**: Changes required when events/waypoints change across projects
**Environment**: Model preferred when internal visibility required

### Performance/Latency/Power/Thermal (PLPT) Constraints
**Critical Rule**: NEVER randomize any parameters
**Rationale**: Must maintain "apples to apples" comparison between versions
**Environment**: Hardware required for real measurements
**Consistency**: Identical conditions mandatory for version comparisons
**Validation**: Real measurement data required for authentic results

## Randomization Constraints

### Never Randomize Categories
**Performance Metrics**: Latency, throughput, response time
**Power Measurements**: Current consumption, power consumption
**Thermal Metrics**: Temperature-related measurements
**Rationale**: Version comparison integrity requires identical conditions

### Strategic Randomization Applications
**Configuration Parameters**: Multiple device configuration options
**Coverage Optimization**: Handle excessive combination scenarios
**Efficiency**: Avoid creating hundreds of tests for configuration coverage
**Method**: All cases covered through repeated randomized execution

## Framework Integration Constraints

### Brownfield Framework Compatibility
**Requirement**: Tests must integrate with existing validation framework
**Constraint**: Framework capabilities limit test design options
**Adaptation**: Test procedures must match framework patterns
**Legacy**: Existing framework strengths and limitations must be considered

### Automation Requirements
**Mandate**: All tests must run fully automatically
**Constraint**: No manual intervention allowed in test procedures
**Design**: Self-contained execution and validation required
**Validation**: Automated pass/fail determination mandatory

## Quality Assurance Checks

### Environment Assignment Validation
- Verify measurement requirements match environment capabilities
- Confirm infrastructure dependencies are available
- Check phase appropriateness for environment selection
- Validate technical feasibility for assigned environment

### Constraint Compliance
- DVT tests environment-agnostic where possible
- FVT internal dependency requirements met
- PLPT deterministic parameter requirements enforced
- Error injection capability matching requirements