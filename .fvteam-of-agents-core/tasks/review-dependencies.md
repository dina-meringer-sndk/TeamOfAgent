# Task: review-dependencies

## Purpose
Analyze feature dependencies and integration points to understand validation complexity and strategic validation requirements.

## Steps
1. **Dependency Mapping**
   - Identify feature dependencies (internal/external)
   - Map inter-component relationships
   - Analyze interface dependencies
   - Document system-level dependencies

2. **Integration Point Analysis**
   - Identify critical integration points
   - Assess integration complexity
   - Map data flows and interfaces
   - Analyze integration risks

3. **Impact Assessment**
   - Evaluate dependency impact on validation
   - Assess integration testing requirements
   - Identify coordination needs
   - Map validation sequence dependencies

4. **Strategic Recommendations**
   - Define dependency validation strategy
   - Recommend integration approach
   - Identify critical path dependencies
   - Plan coordination requirements

5. **Documentation Generation**
   - Generate dependency analysis report
   - Create both .md and .docx versions
   - Include dependency maps and matrices
   - Save to validation strategy folder

## Inputs
- Feature architecture documentation
- System integration specifications
- Interface definitions and protocols
- Component dependency information

## Outputs
- `dependency_analysis_{feature_name}_{date}.md`
- `dependency_analysis_{feature_name}_{date}.docx`
- Dependency mapping diagrams
- Integration strategy recommendations
- Coordination requirements summary

## Dependencies
- Templates: templates/feature-analysis-tmpl.yaml
- Utils: utils/strategy_generator.py, utils/docx_utils.py
- Data: architecture-patterns.md

## Notes
- Focus on strategic validation implications
- Ensure comprehensive dependency coverage
- Highlight critical path and coordination needs