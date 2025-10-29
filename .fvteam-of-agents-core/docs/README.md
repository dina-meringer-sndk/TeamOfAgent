# Validation Strategist Documentation

## Overview
The Validation Strategist agent 🎯 is designed to help you develop high-level validation strategies, analyze architecture documents, and define strategic validation approaches for ASIC, Firmware, and System features.

## Folder Structure

The agent uses a function-based folder structure that is intuitive and easy to navigate:

```
validation_strategist/
├── agent/              # Agent configuration and prompts
│   └── validation_strategist.prompt.md
├── workflows/          # Task workflows and processes
│   ├── analyze-architecture-docs.md
│   ├── assess-risks.md
│   ├── create-validation-strategy.md
│   ├── define-coverage-strategy.md
│   └── review-dependencies.md
├── templates/          # Output templates
│   ├── validation-strategy-tmpl.yaml
│   ├── validation-strategy-tmpl.docx
│   ├── feature-analysis-tmpl.yaml
│   ├── feature-analysis-tmpl.docx
│   ├── risk-assessment-tmpl.yaml
│   └── risk-assessment-tmpl.docx
├── checklists/         # Quality validation checklists
│   ├── architecture-review-checklist.md
│   └── validation-strategy-checklist.md
├── knowledge_base/     # Reference data and patterns
│   ├── validation-strategy-kb.md
│   ├── architecture-patterns.md
│   └── risk-frameworks.md
├── tools/              # Utility scripts and processors
│   ├── document_processor.py
│   ├── docx_utils.py
│   ├── pdf_utils.py
│   └── strategy_generator.py
├── input_files/        # Architecture documents
│   ├── ASIC architecture/
│   ├── FW architecture/
│   └── System architecture/
├── validation strategy/ # Generated validation strategies
├── output/             # Other generated outputs
└── docs/               # Documentation and help
    └── README.md (this file)
```

## Available Commands

When you activate the Validation Strategist agent, you have access to these commands:

1. **\*help** - Show command list
2. **\*create-validation-strategy** - Generate new validation strategy for a feature
3. **\*analyze-architecture** - Review architecture document and extract key insights
4. **\*define-coverage-strategy** - Define strategic coverage approach for feature
5. **\*assess-risks** - Perform strategic risk assessment for feature
6. **\*review-dependencies** - Analyze feature dependencies and integration points
7. **\*doc-out** - Output current strategy document
8. **\*exit** - End session

## How to Use

### 1. Activate the Agent
Load the agent prompt file:
```
agent/validation_strategist.prompt.md
```

### 2. Create a Validation Strategy
Use command **2** (*create-validation-strategy) to:
- Identify feature details (name, domain, scope)
- Analyze relevant architecture documents
- Define strategic coverage planning
- Perform risk assessment
- Plan resource strategy
- Generate professional documentation

### 3. Architecture Analysis
Use command **3** (*analyze-architecture) to:
- Review architecture documents from input_files/
- Extract key architectural components
- Identify critical interfaces and dependencies
- Generate analysis reports

### 4. Risk Assessment
Use command **5** (*assess-risks) to:
- Identify strategic risks and failure modes
- Assess probability and impact
- Define mitigation strategies
- Prioritize risk areas

## Input and Output

### Input Sources
- **Architecture Documents**: Place in `input_files/` subfolders by domain (ASIC, FW, System)
- **User Requirements**: Provided through interactive sessions

### Output Generation
- **Validation Strategies**: Saved to `validation strategy/` folder
- **Analysis Reports**: Generated in both .md and .docx formats
- **Professional Documents**: Using DOCX templates for formal presentation

### File Naming Convention
- Validation strategies: `validation_strategy_{feature_name}_{date}.{ext}`
- Risk assessments: `risk_assessment_{feature_name}_{date}.{ext}`
- Architecture analysis: `architecture_analysis_{feature_name}_{date}.{ext}`

## Key Features

### Strategic Focus
- High-level validation approach (not tactical implementation)
- Architecture-driven strategy development
- Risk-based prioritization and coverage planning

### Professional Output
- Both Markdown and Word document generation
- Professional DOCX templates
- Feature-specific naming conventions

### Document Processing
- Automated .docx and .pdf handling
- Template-based output generation
- Professional formatting and structure

### Knowledge Integration
- Comprehensive knowledge base of validation patterns
- Architecture analysis frameworks
- Risk assessment methodologies

## Best Practices

1. **Start with Architecture**: Always begin with architecture document analysis
2. **Focus on Strategy**: Maintain high-level strategic perspective
3. **Risk-Based Approach**: Prioritize based on risk assessment
4. **Professional Documentation**: Use provided templates for formal outputs
5. **Feature-Specific**: Tailor strategies to specific feature requirements

## Support and Troubleshooting

### Common Issues
- **Missing Architecture Documents**: Ensure documents are in correct input_files/ subfolders
- **Template Errors**: Verify template files are present in templates/ folder
- **Tool Dependencies**: Check that Python libraries are installed for document processing

### Getting Help
- Review workflow files in `workflows/` for detailed process steps
- Check knowledge base in `knowledge_base/` for patterns and examples
- Use `*doc-out` command to review generated documents

## Continuous Improvement

The agent structure supports easy extension:
- Add new workflows to `workflows/` folder
- Create new templates in `templates/` folder
- Extend knowledge base in `knowledge_base/` folder
- Add new utilities to `tools/` folder

For questions or enhancements, refer to the validation_strategist_revision_summary.md document.