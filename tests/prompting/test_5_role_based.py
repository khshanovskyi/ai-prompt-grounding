from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_5_role_based
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION = """### Role-Based

**Definition**: A prompt that assigns the AI a specific role.

**Validation Criteria**:

1. **Clear Role Assignment** ✓
   - Explicitly defines what role the AI should assume
   - Uses phrases like "You are a [role]," "Act as," or "**Role**:"
   - Specifies professional identity, expertise level, or character type

2. **Contextual Background** ✓
   - Provides relevant context or scenario for the role
   - Sets the situation, environment, or circumstances
   - May include organizational context, client details, or situational parameters

3. **Structured Instructions** ✓
   - Breaks down requirements into organized components
   - Uses clear labels or sections (Task, Guidelines, Format, etc.)
   - Provides systematic approach rather than single instruction

4. **Multiple Directive Components** ✓
   - Contains at least 3 of: Role, Context, Task, Guidelines/Rules, Format, Input
   - Each component serves a distinct purpose in shaping the response
   - Instructions are comprehensive and leave little ambiguity

**Valid Role-Based Indicators**:
- Explicit role definitions with professional or character identity
- Structured format with labeled sections (**Role**, **Context**, **Task**, etc.)
- Comprehensive guidelines covering approach, tone, and requirements
- Clear formatting or output structure expectations
- Specific context or scenario setting

**Invalid Patterns**:
- Simple task instructions without role assignment
- Vague or minimal role description
- Unstructured instructions without clear components
- Missing essential elements (no clear role, context, or guidelines)
- Single-sentence instructions without systematic breakdown

**Validation Decision**:
- **VALID**: Contains clear role assignment with structured, multi-component instructions including context and guidelines
- **INVALID**: Lacks clear role definition, structured format, or comprehensive instruction components

**Note**: The pattern should create a comprehensive framework that guides both what the AI should do and how it should approach the task within the assigned role.
"""

class RoleBasedPromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_5_role_based.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.ROLE_BASED

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION
