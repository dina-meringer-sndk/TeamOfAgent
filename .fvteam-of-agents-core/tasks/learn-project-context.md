<!-- Powered by FVTeamOfAgents Core -->

# Learn Project Context Task

## Purpose

Systematically analyze an existing project to understand testing frameworks, naming conventions, code patterns, and business domain concepts. This creates a comprehensive knowledge base that enables intelligent test code generation that seamlessly integrates with the brownfield project.

## SEQUENTIAL Task Execution (Do not proceed until current Task is complete)

### 1. Project Structure Analysis

- **Scan repository structure** to understand overall architecture
- **Identify test directories** and testing organization patterns
- **Map source code to test code** relationships and conventions
- **Document build system** and dependency management approach
- **Identify validation-specific directories**: test data, schemas, validation scripts
- **Map XML/JSON file usage**: test data files, schema definitions, API payloads, validation rules
- **Create initial project profile** with key characteristics

### 2. Testing Framework Detection

- **Analyze existing test files** to identify primary testing framework(s)
- **Extract testing patterns**: assertion styles, setup/teardown approaches, mocking strategies
- **Identify test categorization**: unit tests, integration tests, end-to-end tests
- **Document test execution** commands and CI/CD integration
- **Map framework-specific** conventions and best practices used
- **Analyze Python testing patterns**: unittest classes, test discovery

### 3. Code Convention Analysis

- **Extract naming conventions**: class names, method names, variable patterns
- **Analyze code style**: indentation, formatting, documentation patterns (PEP 8 compliance)
- **Identify architectural patterns**: design patterns, layer organization, dependency injection
- **Document error handling** approaches and exception patterns
- **Map code organization** principles and package structures
- **XML/JSON handling patterns**: parsing libraries used, validation approaches, serialization methods

### 4. Business Domain Understanding

- **Analyze domain models** and business entity relationships
- **Extract business rules** and validation logic from existing code
- **Identify domain-specific** terminology and concepts
- **Map business workflows** and process patterns
- **Document domain constraints** and business validation requirements

### 5. Validation Project Specific Analysis

- **XML File Analysis**: Parse XML files (test data, schemas, API payloads, validation rules), identify structure patterns, extract validation constraints
- **JSON Data Structure Analysis**: Analyze JSON schemas, test data files, API request/response patterns, configuration files
- **Python Validation Patterns**: Identify validation frameworks, custom validators, data transformation patterns
- **Test Data Management**: Document test data organization, data generation patterns, fixture management
- **Validation Rule Extraction**: Identify business validation rules, constraint patterns, error handling approaches
- **Data-Driven Testing**: Analyze how XML/JSON files drive test behavior and validation scenarios

### 6. Existing Code Inventory and Reusability Analysis

- **Build Utility Inventory**: Scan and catalog existing utilities, helpers, and reusable components
  - Common utility locations: `/utils/`, `/helpers/`, `/common/`, `/lib/`, `/shared/`
  - Naming pattern detection: `*Helper.py`, `*Util.java`, `*Manager.py`, `*Builder.py`
  - Functionality categorization: validation, parsing, data manipulation, testing utilities
- **Create Searchable Index**: Build efficient lookup structure for existing code components
  - Class-to-functionality mapping: `{"XMLValidator": ["xml", "validation", "schema"]}`
  - Method signature analysis: public interfaces, parameters, return types
  - Import frequency analysis: identify commonly used utilities from existing test files
- **Reusability Assessment**: Evaluate existing code for extension vs replacement scenarios
  - Interface compatibility: can existing code be extended for new requirements?
  - Code quality evaluation: is existing code maintainable and well-designed?
  - Dependency analysis: what dependencies would be inherited by reusing existing code?
- **Decision Framework Creation**: Establish criteria for extend vs create decisions
  - **Extend Existing**: When interface is compatible, code quality is good, minimal dependencies
  - **Create New**: When existing code is poorly designed, incompatible interface, heavy dependencies
  - **Hybrid Approach**: When partial functionality exists but needs significant enhancement
- **Performance Optimization**: Implement efficient search strategies for large codebases
  - Hierarchical search: check common locations first, fallback to full scan
  - Caching strategy: save inventory results for subsequent tasks
  - Smart filtering: focus on relevant file types and directories

### 7. Create Project Knowledge Base

- **Generate comprehensive profile** using project-analysis-guide.md procedures and project-knowledge-base-tmpl.yaml structure
- **Document all discovered patterns** in structured knowledge base format
- **Create integration guidelines** for new test code generation
- **Establish quality standards** based on existing codebase analysis
- **Save knowledge base** for use in subsequent test generation tasks

## Blocking Conditions

- Repository access issues or missing permissions
- No existing test files found for pattern analysis
- Unrecognizable or unsupported testing framework
- Missing or incomplete project structure
- Critical build system configuration issues

## Success Criteria

- Complete project profile created with all testing patterns documented
- Testing framework and conventions clearly identified and understood
- Business domain concepts extracted and organized
- Integration guidelines established for seamless test code generation
- Knowledge base saved and validated for accuracy

## Dependencies

This task depends on:
- project-analysis-guide.md for systematic analysis procedures
- testing-frameworks-knowledge.md for framework identification
- brownfield-integration-patterns.md for integration strategies
- project-knowledge-base-tmpl.yaml for standardized output structure

## Outputs

This task produces:
- Comprehensive project knowledge base file (using project-knowledge-base-tmpl.yaml)
- Testing framework configuration profile  
- Code convention documentation
- Business domain concept map
- Integration guidelines for test generation
- Validation-specific patterns documentation
- XML/JSON schema and data pattern analysis
- Python validation framework configuration
- Test data management strategy documentation