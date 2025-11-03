<!-- Powered by FVTeamOfAgents Core -->

# Project Analysis Guide

## Purpose

Comprehensive procedural guide for systematically analyzing existing brownfield projects to understand testing frameworks, code patterns, business domain concepts, and integration requirements for intelligent test code generation.

## Analysis Procedures

### **Phase 1: Project Structure Discovery**

#### **Repository Structure Analysis**
```
PROCEDURE: Initial Project Mapping
1. Scan root directory for primary project indicators
   - Build files: pom.xml, build.gradle, package.json, *.csproj, requirements.txt
   - Configuration files: application.properties, config files, environment settings
   - Documentation: README.md, docs folders, architecture diagrams
2. Identify source code organization patterns
   - Main source directories: src/main, lib, app, source
   - Test directories: src/test, tests, __tests__, test
   - Package/namespace organization structures
3. Map dependency and module relationships
   - Multi-module projects and subproject organization
   - External library dependencies and versions
   - Internal module dependencies and coupling
```

**Directory Structure Documentation**
```
ANALYSIS TEMPLATE: Project Structure
Project Type: [Web App/Library/Microservice/Desktop/Mobile]
Primary Language: [Java/Python/JavaScript/C#/Other]
Build System: [Maven/Gradle/npm/MSBuild/Other]
Source Organization: [Description of source code layout]
Test Organization: [Description of test code structure]
Module Structure: [Multi-module or single module with details]
```

#### **Technology Stack Identification**
```
PROCEDURE: Technology Stack Analysis
1. Analyze build configuration files for dependencies
   - Framework dependencies (Spring, Django, React, .NET Core)
   - Testing framework dependencies and versions
   - Database and persistence technology indicators
   - External service integration libraries
2. Scan import/using statements in source files
   - Most frequently imported libraries and frameworks
   - Testing-specific imports and patterns
   - Custom internal library usage patterns
   - Third-party service integration patterns
3. Identify development and deployment environment indicators
   - Container configuration (Docker, Kubernetes)
   - Cloud platform integrations (AWS, Azure, GCP)
   - CI/CD pipeline configuration files
   - Environment-specific configuration patterns
```

### **Phase 2: Testing Framework Analysis**

#### **Testing Framework Detection**
```
PROCEDURE: Testing Framework Identification
1. Scan test dependencies in build configurations
   - Primary testing frameworks: JUnit, pytest, Jest, MSTest, NUnit
   - Assertion libraries: Hamcrest, Chai, Should, FluentAssertions
   - Mocking frameworks: Mockito, unittest.mock, Sinon, Moq
   - Test runner configurations and plugins
2. Analyze existing test file structures
   - Test file naming patterns and conventions
   - Test class organization and hierarchy
   - Test method naming and grouping patterns
   - Setup/teardown method usage and patterns
3. Examine test execution configuration
   - Test runner settings and parameters
   - Test categorization and tagging systems
   - Parallel execution configuration
   - Coverage reporting and quality gates
```

**Framework Pattern Analysis**
```
PROCEDURE: Testing Pattern Extraction
1. Analyze test class structures and patterns
   - Base test class usage and inheritance patterns
   - Common setup and teardown procedures
   - Test data creation and management approaches
   - Assertion styles and preference patterns
2. Examine mocking and stubbing patterns
   - Mock creation and configuration approaches
   - Stub setup and verification procedures
   - Test double usage patterns and preferences
   - Integration test vs unit test mocking strategies
3. Study test organization and categorization
   - Test suite organization strategies
   - Test naming conventions and grouping
   - Integration point testing approaches
   - Performance and load testing patterns
```

### **Phase 3: Code Convention Analysis**

#### **Naming Convention Extraction**
```
PROCEDURE: Naming Pattern Analysis
1. Analyze class naming patterns across codebase
   - Class name formatting (PascalCase, camelCase, snake_case)
   - Prefix/suffix patterns for different types (Service, Repository, Controller)
   - Abstract class and interface naming conventions
   - Exception and error class naming patterns
2. Study method naming conventions
   - Method name formatting and style consistency
   - Verb-noun patterns and business language usage
   - Parameter naming conventions and patterns
   - Private vs public method naming differences
3. Examine variable and field naming patterns
   - Local variable naming conventions
   - Field and property naming patterns
   - Constant and configuration value naming
   - Collection and array naming conventions
```

**Code Style and Formatting Analysis**
```
PROCEDURE: Code Style Pattern Extraction
1. Analyze code formatting and structure preferences
   - Indentation style (spaces vs tabs, indentation size)
   - Brace placement and whitespace patterns
   - Line length and wrapping preferences
   - Import/using statement organization patterns
2. Study documentation and comment patterns
   - Documentation comment styles and tools (JavaDoc, Sphinx, JSDoc)
   - Inline comment conventions and usage patterns
   - Code annotation and metadata usage
   - TODO/FIXME comment patterns and lifecycle
3. Examine error handling and exception patterns
   - Exception handling strategies and patterns
   - Error logging and reporting conventions
   - Validation and input checking approaches
   - Error message formatting and localization
```

### **Phase 4: Business Domain Understanding**

#### **Domain Model Analysis**
```
PROCEDURE: Business Domain Extraction
1. Identify core business entities and concepts
   - Primary business objects and their relationships
   - Value objects and entity patterns
   - Aggregate roots and domain service patterns
   - Business workflow and process representations
2. Analyze business rules and constraints
   - Validation rules and business logic patterns
   - Invariant enforcement and constraint checking
   - Business calculation and transformation logic
   - State transition and lifecycle management
3. Extract domain-specific terminology and language
   - Business vocabulary and term definitions
   - Domain-specific acronyms and abbreviations
   - Industry-specific concepts and standards
   - Localization and internationalization considerations
```

**Business Logic Pattern Analysis**
```
PROCEDURE: Business Logic Understanding
1. Study service layer and business logic organization
   - Business service patterns and responsibilities
   - Transaction management and data consistency approaches
   - Business rule implementation and enforcement patterns
   - Workflow orchestration and process management
2. Analyze data access and persistence patterns
   - Repository and data access layer patterns
   - Database interaction and query patterns
   - Caching strategies and performance optimizations
   - Data transformation and mapping approaches
3. Examine integration and external service patterns
   - External API integration patterns and error handling
   - Message queue and event-driven architecture usage
   - Third-party service integration and fallback strategies
   - Authentication and authorization patterns
```

### **Phase 5: Architecture and Design Pattern Analysis**

#### **Architectural Pattern Identification**
```
PROCEDURE: Architecture Pattern Analysis
1. Identify overall architectural patterns
   - Layered architecture and layer separation patterns
   - MVC/MVP/MVVM patterns and implementation approaches
   - Microservice vs monolithic architecture indicators
   - Event-driven and message-based architecture patterns
2. Analyze design pattern usage
   - Common design patterns used throughout codebase
   - Factory and builder pattern implementations
   - Observer and strategy pattern usage
   - Dependency injection and inversion of control patterns
3. Study modularity and coupling patterns
   - Module boundary definitions and enforcement
   - Interface design and abstraction patterns
   - Dependency management and circular dependency prevention
   - Plugin and extension point patterns
```

**Quality and Maintenance Pattern Analysis**
```
PROCEDURE: Quality Pattern Extraction
1. Analyze code quality and maintenance patterns
   - Code review practices and quality gates
   - Refactoring patterns and technical debt management
   - Performance monitoring and optimization approaches
   - Security patterns and vulnerability management
2. Study versioning and evolution patterns
   - API versioning and backward compatibility strategies
   - Database migration and schema evolution patterns
   - Configuration management and environment handling
   - Feature flagging and gradual rollout approaches
3. Examine monitoring and observability patterns
   - Logging patterns and structured logging approaches
   - Metrics collection and performance monitoring
   - Error tracking and alerting strategies
   - Health check and system monitoring patterns
```

## Analysis Tools and Techniques

### **Automated Analysis Procedures**

#### **File System Analysis Commands**
```
ANALYSIS COMMANDS:
# Directory structure analysis
find . -type f -name "*.java" | head -20  # Sample Java files
find . -type d -name "*test*" | head -10  # Test directories
find . -name "pom.xml" -o -name "build.gradle" -o -name "package.json"  # Build files

# Pattern extraction
grep -r "class.*Test" src/test/  # Test class patterns
grep -r "@Test\|def test_\|it(" src/test/  # Test method patterns
grep -r "import.*test\|from.*test" src/  # Testing framework imports
```

**Content Analysis Procedures**
```
CONTENT ANALYSIS:
1. Sample file analysis (analyze 10-15 representative files)
2. Import statement frequency analysis
3. Method naming pattern extraction
4. Comment and documentation style analysis
5. Error handling pattern identification
```

#### **Statistical Analysis Techniques**
```
STATISTICAL ANALYSIS:
1. Code file size and complexity distribution
2. Test file to source file ratio analysis
3. Import dependency frequency analysis
4. Naming pattern consistency measurement
5. Code comment density and quality assessment
```

### **Manual Analysis Procedures**

#### **Representative File Sampling**
```
SAMPLING STRATEGY:
1. Select representative files from each major module/package
2. Choose files with different purposes (entities, services, controllers)
3. Sample both simple and complex implementations
4. Include edge cases and specialized functionality
5. Review both new and legacy code sections
```

**Pattern Recognition Techniques**
```
PATTERN RECOGNITION:
1. Identify recurring code structures and templates
2. Extract common method signatures and naming patterns
3. Recognize business logic organization strategies
4. Document exception handling and error management approaches
5. Capture integration and external dependency patterns
```

## Knowledge Base Creation

### **Documentation Templates**

#### **Project Profile Template**
```
PROJECT ANALYSIS SUMMARY:
Project Overview:
- Name: [Project Name]
- Type: [Application Type]
- Primary Language: [Language]
- Framework: [Primary Framework]
- Architecture Style: [Architectural Pattern]

Testing Framework Analysis:
- Primary Testing Framework: [Framework Name and Version]
- Assertion Library: [Library Name]
- Mocking Framework: [Mocking Library]
- Test Organization: [Structure Description]
- Test Execution: [Runner Configuration]

Code Conventions:
- Naming Patterns: [Detailed Naming Conventions]
- Code Style: [Formatting and Style Preferences]
- Documentation: [Comment and Documentation Patterns]
- Error Handling: [Exception and Error Patterns]

Business Domain:
- Domain Concepts: [Core Business Entities and Relationships]
- Business Rules: [Key Business Logic and Constraints]
- Terminology: [Domain-Specific Language and Terms]
- Workflows: [Business Process Patterns]

Architecture Patterns:
- Design Patterns: [Common Design Pattern Usage]
- Layer Organization: [Architectural Layer Structure]
- Dependency Management: [Dependency Injection and Management]
- Integration Patterns: [External System Integration Approaches]
```

#### **Integration Guidelines Template**
```
INTEGRATION GUIDELINES:
Test Generation Strategy:
- Framework Integration: [How to integrate with existing testing framework]
- Naming Strategy: [How to name generated test classes and methods]
- Organization Strategy: [Where to place generated tests]
- Data Strategy: [How to create and manage test data]

Quality Standards:
- Code Quality: [Quality criteria and expectations]
- Coverage Expectations: [Coverage targets and measurement]
- Performance Requirements: [Test execution performance expectations]
- Maintenance Guidelines: [How to maintain and evolve generated tests]

Risk Mitigation:
- Integration Risks: [Potential integration challenges and mitigation strategies]
- Quality Risks: [Quality assurance and validation approaches]
- Maintenance Risks: [Long-term maintenance and evolution considerations]
- Team Adoption: [Strategies for team acceptance and effective usage]
```

### **Knowledge Base Validation**

#### **Accuracy Verification Procedures**
```
VALIDATION CHECKLIST:
□ Sample validation: Generated patterns match actual codebase samples
□ Team review: Development team confirms accuracy of extracted patterns
□ Exception identification: Edge cases and exceptions properly documented
□ Evolution consideration: Patterns account for ongoing project evolution
□ Completeness check: All major aspects of project covered adequately
```

**Quality Assurance Procedures**
```
QUALITY ASSURANCE:
□ Pattern consistency: Extracted patterns are internally consistent
□ Documentation clarity: Analysis results clearly documented and understandable
□ Actionability: Analysis provides sufficient detail for test generation
□ Maintainability: Knowledge base structured for easy updates and evolution
□ Accessibility: Information organized for efficient retrieval and usage
```

## Analysis Best Practices

### **Efficiency and Thoroughness**
- Focus analysis effort on areas most relevant to test generation
- Use sampling techniques to manage analysis scope while maintaining accuracy
- Leverage automated analysis tools where available to increase efficiency
- Document analysis methodology for reproducibility and validation
- Maintain analysis focus on actionable insights for test generation

### **Accuracy and Reliability**
- Cross-validate findings through multiple analysis approaches
- Verify extracted patterns through team review and feedback
- Test pattern accuracy through small-scale pilot implementations
- Document assumptions and limitations of analysis findings
- Establish procedures for updating analysis as project evolves