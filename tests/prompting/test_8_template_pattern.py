from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_8_template_pattern
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION = """### Template Pattern

**Definition**: A prompt that provides a rigid, predefined structural template with specific sections, labels, and formatting that the AI must follow exactly without deviation.

**Validation Criteria**:

1. **Rigid Structure Provided** ✓
   - Contains a complete, predefined template with exact formatting
   - Uses specific structural elements (headers, tags, brackets, etc.)
   - Template is fully laid out, not just described

2. **Exact Format Specification** ✓
   - Uses precise formatting: markdown headers, XML tags, JSON structure, etc.
   - Includes specific labels, sections, and organizational elements
   - Shows exact syntax and structure to be maintained

3. **Placeholder System** ✓
   - Contains clear placeholders showing where content should go
   - Uses consistent placeholder format: [brackets], "descriptions", etc.
   - Indicates exactly what type of content belongs in each section

4. **Complete Template Framework** ✓
   - Provides the entire structural framework, not partial examples
   - Template is comprehensive enough to complete the full task
   - Shows all required sections and their relationships

**Valid Template Indicators**:
- Complete structural templates in specific formats (Markdown, XML, JSON, etc.)
- Consistent use of placeholders: [description], [value], etc.
- Exact formatting with headers, tags, indentation, or syntax
- Rigid organizational structure that must be maintained
- Clear section labels and hierarchical organization

**Invalid Patterns**:
- Flexible guidelines without rigid structure
- Partial examples rather than complete templates
- Descriptive instructions without actual template format
- Templates that allow significant structural variation
- Missing placeholder system or unclear content placement

**Note**: The template must be so specific that the AI has little choice in how to structure the response. The format should be rigid enough that all responses following the template would have identical structural organization.
"""

class TemplatePromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_8_template_pattern.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.TEMPLATE_PATTERN

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION
