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
- Always perform complete document review before declaring task complete

## Document Review and Completion Protocol
Before declaring this task complete, perform comprehensive review:

### 1. Content Completeness Check:
- [ ] All validation strategy sections completed thoroughly
- [ ] Risk assessment matrix complete with all areas covered
- [ ] Resource requirements documented and justified
- [ ] Success criteria clearly defined and measurable
- [ ] No placeholder text or incomplete sections

### 2. Strategic Quality Review:
- [ ] Strategic focus maintained throughout document
- [ ] Risk-based prioritization applied consistently
- [ ] Architecture-driven approach evident in strategy
- [ ] Coverage strategy comprehensive and justified

### 3. Traceability and Accuracy Review:
- [ ] All requirements traced to validation approaches
- [ ] Risk assessments realistic and well-justified
- [ ] Resource estimates reasonable and documented
- [ ] Technical content accurate for the domain

### 4. Format and Compliance Review:
- [ ] Professional formatting applied consistently
- [ ] Document structure clear with proper organization
- [ ] File naming conventions followed exactly
- [ ] Both .md and .docx outputs generated properly

### 5. Validation Strategy Completeness:
- [ ] All critical validation areas addressed
- [ ] Integration and interface validation covered
- [ ] Edge cases and error conditions included
- [ ] Compliance and regulatory requirements addressed

**Only after ALL review items are verified complete:**
- State: "Validation strategy document review completed successfully"
- Provide completion summary with key deliverables and highlights
- Confirm strategy is ready for implementation and next phases