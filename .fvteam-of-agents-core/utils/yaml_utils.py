# <!-- Powered by FVTeamOfAgents Core -->
"""
BMAD Factory Agent - YAML Utilities

Utilities for processing YAML templates and generating content with variable substitution.
"""

import yaml
import re
from typing import Dict, Any, List, Optional
from pathlib import Path


class YAMLTemplateProcessor:
    """Process YAML templates with variable substitution and validation."""
    
    def __init__(self):
        self.variables = {}
        self.template_cache = {}
    
    def load_template(self, template_path: str) -> Dict[str, Any]:
        """
        Load a YAML template file.
        
        Args:
            template_path: Path to the YAML template file
            
        Returns:
            Dictionary containing the template structure
        """
        try:
            with open(template_path, 'r', encoding='utf-8') as file:
                template = yaml.safe_load(file)
                self.template_cache[template_path] = template
                return template
        except FileNotFoundError:
            raise FileNotFoundError(f"Template file not found: {template_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in template {template_path}: {e}")
    
    def set_variables(self, variables: Dict[str, Any]):
        """
        Set variables for template substitution.
        
        Args:
            variables: Dictionary of variable names and values
        """
        self.variables.update(variables)
    
    def substitute_variables(self, text: str) -> str:
        """
        Substitute variables in text using {{variable}} pattern.
        
        Args:
            text: Text containing variable placeholders
            
        Returns:
            Text with variables substituted
        """
        def replace_var(match):
            var_name = match.group(1)
            return str(self.variables.get(var_name, f"{{{{{var_name}}}}}"))
        
        return re.sub(r'\{\{(\w+)\}\}', replace_var, text)
    
    def process_template_section(self, section: Dict[str, Any]) -> str:
        """
        Process a template section and generate content.
        
        Args:
            section: Template section configuration
            
        Returns:
            Generated content for the section
        """
        if 'template' in section:
            template_text = section['template']
            return self.substitute_variables(template_text)
        
        return ""
    
    def generate_from_template(self, template_path: str, output_path: str, variables: Dict[str, Any]):
        """
        Generate a file from a template with variable substitution.
        
        Args:
            template_path: Path to the YAML template
            output_path: Path where generated file should be saved
            variables: Variables for substitution
        """
        template = self.load_template(template_path)
        self.set_variables(variables)
        
        output_content = []
        
        # Process template sections
        if 'sections' in template:
            for section in template['sections']:
                content = self.process_template_section(section)
                if content:
                    output_content.append(content)
        
        # Write output file
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(output_content))
    
    def validate_template(self, template_path: str) -> List[str]:
        """
        Validate a YAML template for BMAD compliance.
        
        Args:
            template_path: Path to the template file
            
        Returns:
            List of validation errors (empty if valid)
        """
        errors = []
        
        try:
            template = self.load_template(template_path)
            
            # Check required top-level fields
            required_fields = ['template', 'workflow', 'sections']
            for field in required_fields:
                if field not in template:
                    errors.append(f"Missing required field: {field}")
            
            # Check template metadata
            if 'template' in template:
                template_meta = template['template']
                required_meta = ['id', 'name', 'version', 'output']
                for field in required_meta:
                    if field not in template_meta:
                        errors.append(f"Missing template metadata: {field}")
            
            # Check sections structure
            if 'sections' in template:
                for i, section in enumerate(template['sections']):
                    if 'id' not in section:
                        errors.append(f"Section {i} missing required 'id' field")
                    if 'title' not in section:
                        errors.append(f"Section {i} missing required 'title' field")
        
        except Exception as e:
            errors.append(f"Template validation error: {e}")
        
        return errors


def create_bmad_template(template_id: str, name: str, output_filename: str) -> Dict[str, Any]:
    """
    Create a basic BMAD template structure.
    
    Args:
        template_id: Unique identifier for the template
        name: Display name for the template
        output_filename: Target filename for generated content
        
    Returns:
        Dictionary containing basic BMAD template structure
    """
    return {
        'template': {
            'id': template_id,
            'name': name,
            'version': '1.0',
            'output': {
                'format': 'markdown',
                'filename': output_filename,
                'title': name
            }
        },
        'workflow': {
            'mode': 'interactive',
            'elicitation': 'advanced-elicitation'
        },
        'sections': []
    }


def validate_yaml_syntax(file_path: str) -> Optional[str]:
    """
    Validate YAML syntax in a file.
    
    Args:
        file_path: Path to the YAML file
        
    Returns:
        Error message if invalid, None if valid
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            yaml.safe_load(file)
        return None
    except yaml.YAMLError as e:
        return f"YAML syntax error: {e}"
    except FileNotFoundError:
        return f"File not found: {file_path}"


# Example usage
if __name__ == "__main__":
    processor = YAMLTemplateProcessor()
    
    # Example: Load and process a template
    variables = {
        'agent_name': 'Example Agent',
        'agent_id': 'example_agent',
        'agent_purpose': 'Demonstrate YAML template processing'
    }
    
    try:
        processor.set_variables(variables)
        print("YAML template processor initialized successfully")
    except Exception as e:
        print(f"Error: {e}")