# Task: analyze-architecture-docs

## Purpose
Analyze architecture documents to extract key insights, dependencies, and architectural information ONLY. This task produces architecture analysis documentation without creating validation strategies.

**IMPORTANT**: This task creates ONLY architecture analysis reports - no validation strategy documents.

## Steps
1. **Document Discovery**
   - Scan input folders (ASIC architecture, FW architecture, System architecture)
   - Identify relevant documents for the specified feature
   - Categorize documents by type and relevance

2. **Document Processing**
   - Use utils for reading .docx, .pdf, and .md files
   - Extract key architectural information
   - Identify system interfaces and dependencies
   - Map feature integration points

3. **Architecture Analysis**
   - Analyze system architecture relevant to feature
   - Identify critical paths and data flows
   - Map inter-component dependencies
   - Assess architectural complexity and risks

4. **Strategic Insights Extraction**
   - Identify validation-critical architectural elements
   - Highlight potential risk areas
   - Extract interface and integration requirements
   - Document architectural constraints
   - **NOTE**: Analysis only - no validation strategy creation

5. **Architecture Analysis Report Generation**
   - Create comprehensive architecture analysis report
   - Use feature-analysis-tmpl.docx for professional DOCX output
   - Generate both .md and .docx outputs with consistent formatting
   - Include architectural insights and implications
   - **CRITICAL**: Save ONLY architecture analysis - NO validation strategy documents
   - Save to specified output folder with proper naming conventions

## Inputs
- Feature name or area of interest
- Architecture documents from input folders
- Analysis scope and objectives

## Outputs
- `architecture_analysis_{feature_name}_{date}.md`
- `architecture_analysis_{feature_name}_{date}.docx`
- Architectural insights and technical analysis
- Dependency mapping and interface documentation
- Risk identification and complexity assessment
- **IMPORTANT**: NO validation strategy documents produced by this task

## Dependencies
- Utils: utils/document_processor.py, utils/pdf_utils.py, utils/docx_utils.py
- Templates: templates/feature-analysis-tmpl.yaml, templates/feature-analysis-tmpl.docx
- Data: architecture-patterns.md

## Notes
- Focus on comprehensive architecture analysis and documentation
- Ensure complete dependency analysis and interface mapping
- Highlight architectural risks and complexity factors
- **CRITICAL**: This task produces ONLY architecture analysis - use separate commands for validation strategy creation
- Always perform complete document review before declaring task complete

## Document Review and Completion Protocol
Before declaring this task complete, perform comprehensive review:

### 1. Content Completeness Check:
- [ ] All architecture components analyzed and documented
- [ ] All interfaces and dependencies identified and mapped
- [ ] Risk areas and complexity factors highlighted
- [ ] All sections of analysis report completed
- [ ] No placeholder text or incomplete sections

### 2. Technical Accuracy Review:
- [ ] Technical content accurate for the architectural domain
- [ ] Dependency mappings correct and complete
- [ ] Interface descriptions technically sound
- [ ] Risk assessments realistic and justified

### 3. Format and Quality Review:
- [ ] Professional formatting applied consistently
- [ ] Document structure clear with proper headings
- [ ] Tables and diagrams properly formatted
- [ ] File naming conventions followed exactly

### 4. Task Compliance Review:
- [ ] Task instructions followed exactly as specified
- [ ] ONLY architecture analysis produced (no validation strategy)
- [ ] All required outputs generated (.md and .docx)
- [ ] Files saved to correct output location

**Only after ALL review items are verified complete:**
- State: "Architecture analysis document review completed successfully"
- Provide completion summary with key deliverables
- Confirm task finished and ready for next steps