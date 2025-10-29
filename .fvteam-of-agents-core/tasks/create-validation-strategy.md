# Task: create-validation-strategy

## Purpose
Guide the user through creating a comprehensive validation strategy for a specific feature, focusing on strategic architecture and high-level validation approach.

## Steps
1. **Feature Identification**
   - Gather feature name and basic description
   - Identify feature domain (ASIC, FW, System)
   - Understand feature scope and boundaries

2. **Architecture Analysis**
   - Review relevant architecture documents from input folders
   - Identify key architectural components
   - Map feature dependencies and integration points
   - Analyze critical paths and interfaces

3. **Strategic Coverage Planning**
   - Define high-level coverage objectives
   - Identify strategic validation approaches
   - Prioritize validation areas based on risk
   - Define success criteria

4. **Risk Assessment**
   - Identify strategic risks and failure modes
   - Assess impact and likelihood
   - Define mitigation strategies
   - Prioritize risk areas

5. **Resource Strategy**
   - Identify required skills and expertise
   - Define tool and environment requirements
   - Estimate effort and timeline considerations
   - Plan resource allocation strategy

6. **Documentation Generation**
   - Generate validation strategy document using templates
   - Use validation-strategy-tmpl.docx for professional DOCX output
   - Use validation-strategy-tmpl.yaml for structured data
   - Create both .md and .docx versions with consistent content
   - Include feature name in document naming
   - Save to validation strategy output folder

## Inputs
- Feature name and description
- Architecture documents from relevant input folders
- User requirements and constraints

## Outputs
- `validation_strategy_{feature_name}_{date}.md`
- `validation_strategy_{feature_name}_{date}.docx`
- Strategic validation approach document
- Risk assessment matrix
- Resource requirements summary

## Dependencies
- Templates: templates/validation-strategy-tmpl.yaml, templates/validation-strategy-tmpl.docx
- Utils: utils/document_processor.py, utils/docx_utils.py
- Data: validation-strategy-kb.md

## Notes
- Maintain strategic focus throughout - avoid tactical implementation details
- Use architecture-driven approach for strategy development
- Ensure risk-based prioritization in all recommendations