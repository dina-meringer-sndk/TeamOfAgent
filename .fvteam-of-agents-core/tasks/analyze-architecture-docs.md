# Task: analyze-architecture-docs

## Purpose
Analyze architecture documents to extract key insights, dependencies, and strategic validation considerations for feature validation planning.

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

5. **Summary Generation**
   - Create architecture analysis summary
   - Use feature-analysis-tmpl.docx for professional DOCX output
   - Generate both .md and .docx outputs with consistent formatting
   - Include strategic validation implications
   - Save to validation strategy folder

## Inputs
- Feature name or area of interest
- Architecture documents from input folders
- Analysis scope and objectives

## Outputs
- `architecture_analysis_{feature_name}_{date}.md`
- `architecture_analysis_{feature_name}_{date}.docx`
- Key insights and strategic implications
- Dependency mapping
- Risk identification summary

## Dependencies
- Utils: utils/document_processor.py, utils/pdf_utils.py, utils/docx_utils.py
- Templates: templates/feature-analysis-tmpl.yaml, templates/feature-analysis-tmpl.docx
- Data: architecture-patterns.md

## Notes
- Focus on strategic validation implications
- Ensure comprehensive dependency analysis
- Highlight architectural risks and validation challenges