# Task: assess-risks

## Purpose
Perform strategic risk assessment for feature validation, identifying and prioritizing validation risks with mitigation strategies.

## Steps
1. **Risk Identification**
   - Analyze feature architecture for risk areas
   - Identify technical and schedule risks
   - Map interface and integration risks
   - Assess complexity and dependency risks

2. **Risk Analysis**
   - Evaluate risk probability and impact
   - Categorize risks by type and severity
   - Assess risk interdependencies
   - Map risks to feature areas

3. **Risk Prioritization**
   - Create risk priority matrix
   - Rank risks by strategic importance
   - Identify critical path risks
   - Highlight showstopper scenarios

4. **Mitigation Strategy**
   - Define risk mitigation approaches
   - Plan early detection strategies
   - Establish contingency plans
   - Define risk monitoring approach

5. **Risk Documentation**
   - Generate risk assessment report
   - Use risk-assessment-tmpl.docx for professional DOCX output
   - Create both .md and .docx versions with consistent content
   - Include risk matrices and mitigation plans
   - Save to validation strategy folder

## Inputs
- Feature specification and architecture
- Architecture analysis results
- Historical risk data and lessons learned
- Project constraints and timelines

## Outputs
- `risk_assessment_{feature_name}_{date}.md`
- `risk_assessment_{feature_name}_{date}.docx`
- Risk priority matrix
- Mitigation strategy recommendations
- Risk monitoring plan

## Dependencies
- Templates: templates/risk-assessment-tmpl.yaml, templates/risk-assessment-tmpl.docx
- Utils: utils/strategy_generator.py, utils/docx_utils.py
- Data: risk-frameworks.md

## Notes
- Focus on strategic risks, not tactical issues
- Ensure comprehensive coverage of risk areas
- Link risks to business impact and strategic objectives