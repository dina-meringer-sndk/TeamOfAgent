<!-- Powered by FVTeamOfAgents Core -->

# PlantUML Validation Guide

## Purpose

Step-by-step procedural guide for validating PlantUML class diagrams systematically to ensure they meet quality standards for test code generation. This guide provides specific procedures and commands for comprehensive UML validation.

## Validation Procedures

### **Phase 1: Syntax Validation**

#### **Basic Syntax Parsing**
**Step 1: Initial Parse Validation**
```
PROCEDURE: Basic Syntax Check
1. Copy PlantUML content to validation workspace
2. Check for required @startuml and @enduml tags
3. Validate overall structure and indentation
4. Look for obvious syntax errors (missing brackets, quotes)
5. Verify character encoding and special character handling
```

**Step 2: Class Definition Validation**
```
PROCEDURE: Class Structure Validation
1. Identify all class definitions using pattern: "class ClassName"
2. Verify each class has opening and closing braces if used
3. Check class name validity (valid identifiers, no conflicts)
4. Validate visibility modifiers (+, -, #, ~) if specified
5. Confirm stereotype usage syntax if applicable
```

**Step 3: Attribute Syntax Validation**
```
PROCEDURE: Attribute Declaration Check
1. For each class, extract attribute declarations
2. Verify attribute syntax: [visibility] attributeName : dataType
3. Check data type validity and spelling
4. Validate special characters in attribute names
5. Confirm no duplicate attribute names within classes
```

**Step 4: Method Signature Validation**
```
PROCEDURE: Method Declaration Check
1. Extract all method declarations from classes
2. Verify method syntax: [visibility] methodName(parameters) : returnType
3. Validate parameter list syntax and type specifications
4. Check return type declarations (including void)
5. Confirm constructor method syntax if present
```

### **Phase 2: Relationship Validation**

#### **Inheritance Relationship Validation**
```
PROCEDURE: Inheritance Syntax Check
1. Identify inheritance relationships using "--|>" pattern
2. Verify both parent and child classes are defined
3. Check for circular inheritance dependencies
4. Validate inheritance syntax correctness
5. Confirm logical inheritance relationships
```

**Association and Dependency Validation**
```
PROCEDURE: Association Relationship Check
1. Identify association relationships using "-->" or other connectors
2. Verify all referenced classes exist in diagram
3. Check multiplicity syntax if specified (1..*, 0..1, etc.)
4. Validate association direction and meaning
5. Confirm no contradictory relationships
```

**Composition and Aggregation Validation**
```
PROCEDURE: Composition/Aggregation Check
1. Identify composition (*--) and aggregation (o--) relationships
2. Verify relationship syntax and direction
3. Check logical validity of ownership relationships
4. Validate multiplicity specifications
5. Confirm proper use of composition vs aggregation semantics
```

### **Phase 3: Semantic Analysis**

#### **Business Logic Consistency**
```
PROCEDURE: Business Logic Validation
1. Review class purposes and responsibilities
2. Verify method signatures align with expected functionality
3. Check attribute types match business domain requirements
4. Validate relationship logic matches business rules
5. Identify missing essential business methods or attributes
```

**Domain Model Completeness**
```
PROCEDURE: Domain Completeness Check
1. Compare against known business domain requirements
2. Identify missing critical business entities
3. Verify essential business operations are represented
4. Check for incomplete or placeholder implementations
5. Validate domain constraint representation
```

**Data Type and Constraint Validation**
```
PROCEDURE: Data Type Appropriateness Check
1. Review all attribute data types for business appropriateness
2. Verify method parameter types match expected inputs
3. Check return types align with business value expectations
4. Validate constraint representations (required fields, formats)
5. Confirm appropriate level of detail for implementation
```

### **Phase 4: Project Integration Analysis**

#### **Naming Convention Compliance**
```
PROCEDURE: Project Naming Standard Check
1. Load project naming conventions from knowledge base
2. Compare class names against project standards
3. Verify method naming follows project patterns
4. Check attribute naming consistency with codebase
5. Validate package/namespace organization alignment
```

**Architectural Pattern Compliance**
```
PROCEDURE: Architecture Alignment Check
1. Review project architectural patterns from knowledge base
2. Verify UML design aligns with architectural constraints
3. Check layer separation and dependency direction compliance
4. Validate design pattern usage consistency
5. Identify potential architectural conflicts
```

**Framework and Technology Compatibility**
```
PROCEDURE: Technology Stack Compatibility Check
1. Verify UML constructs compatible with project technology stack
2. Check framework-specific pattern requirements
3. Validate database mapping considerations if applicable
4. Confirm testing framework compatibility for generated tests
5. Identify technology-specific constraint violations
```

### **Phase 5: Test Generation Readiness Assessment**

#### **Testability Analysis**
```
PROCEDURE: Test Generation Feasibility Check
1. Verify all public methods have sufficient detail for test generation
2. Check for appropriate method visibility for testing
3. Validate parameter and return type specificity
4. Identify methods requiring special testing considerations
5. Confirm error scenario testability
```

**Test Scenario Derivation**
```
PROCEDURE: Test Scenario Identification
1. For each method, identify happy path test scenarios
2. Derive edge case scenarios from parameter types and constraints
3. Identify exception scenarios from method signatures
4. Determine required test data and setup scenarios
5. Validate completeness of testable business scenarios
```

**Mock and Dependency Analysis**
```
PROCEDURE: Test Dependency Assessment
1. Identify external dependencies requiring mocking
2. Analyze relationship complexities for test isolation
3. Determine test data requirements and generation strategies
4. Validate framework compatibility for mocking needs
5. Assess integration test scenario requirements
```

## Validation Commands and Tools

### **Manual Validation Procedures**

#### **Syntax Checking Commands**
```
VALIDATION CHECKLIST:
□ PlantUML syntax parser validation (if tool available)
□ Manual line-by-line syntax review
□ Class definition completeness check
□ Relationship syntax validation
□ Character encoding and special character verification
```

**Semantic Validation Procedures**
```
VALIDATION CHECKLIST:
□ Business logic consistency review
□ Domain model completeness assessment
□ Data type appropriateness validation
□ Constraint representation verification
□ Integration compatibility analysis
```

### **Automated Validation Integration**

#### **Tool-Based Validation**
```
AUTOMATED CHECKS (if tools available):
1. PlantUML syntax validation tool execution
2. Automated relationship consistency checking
3. Naming convention compliance verification
4. Architecture pattern alignment validation
5. Test generation readiness assessment
```

**Integration with Project Tools**
```
PROJECT TOOL INTEGRATION:
1. IDE PlantUML plugin validation
2. Build system UML validation integration
3. Documentation generation tool compatibility
4. Version control UML diff validation
5. Continuous integration UML checking
```

## Issue Documentation and Resolution

### **Issue Classification System**

#### **Syntax Issues**
```
SYNTAX ISSUE TEMPLATE:
- Issue Type: Syntax Error
- Severity: [Critical/Major/Minor]
- Location: [Line number or class reference]
- Description: [Specific syntax problem]
- Resolution: [Exact correction needed]
- Example: [Corrected syntax example]
```

**Semantic Issues**
```
SEMANTIC ISSUE TEMPLATE:
- Issue Type: Semantic Problem
- Severity: [Critical/Major/Minor]
- Business Impact: [Effect on business logic representation]
- Description: [Logical inconsistency or incompleteness]
- Resolution: [Required business clarification or design change]
- Architect Consultation: [Yes/No - if business redesign needed]
```

**Integration Issues**
```
INTEGRATION ISSUE TEMPLATE:
- Issue Type: Integration Conflict
- Severity: [Critical/Major/Minor]
- Conflict Area: [Naming/Architecture/Technology/Framework]
- Description: [Specific integration problem]
- Project Impact: [Effect on existing codebase integration]
- Resolution Options: [Alternative approaches or modifications]
```

### **Quality Gate Decision Framework**

#### **Decision Criteria**
```
PROCEED CRITERIA:
- All syntax validation passes completely
- No critical semantic inconsistencies
- Project integration conflicts are minor and resolvable
- Test generation feasibility confirmed
- Business logic representation adequate

ESCALATE CRITERIA:
- Critical syntax errors preventing parsing
- Major semantic inconsistencies affecting business logic
- Significant architectural conflicts with existing project
- Test generation blockers identified
- Essential business functionality missing or inadequate
```

**Documentation Requirements**
```
VALIDATION REPORT TEMPLATE:
1. Executive Summary: [PROCEED/ESCALATE decision with rationale]
2. Syntax Validation Results: [Detailed findings and status]
3. Semantic Analysis Summary: [Business logic assessment]
4. Integration Assessment: [Project compatibility analysis]
5. Test Generation Readiness: [Feasibility and approach confirmation]
6. Issue Summary: [All identified issues with resolution guidance]
7. Next Steps: [Specific actions required before proceeding]
```

## Validation Best Practices

### **Efficiency and Accuracy**
- Perform validation in systematic phases to catch issues early
- Use project knowledge base to inform validation criteria
- Document all findings clearly for reproducibility
- Maintain validation consistency across different UML inputs
- Leverage automated tools where available for accuracy

### **Quality Assurance**
- Double-check critical validation decisions
- Cross-reference validation results with project requirements
- Verify validation completeness against checklist criteria
- Ensure validation documentation supports decision rationale
- Validate validator accuracy through spot checks and reviews