from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_7_constraint_pattern
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION = """### Constraint Pattern

**Definition**: A prompt that sets explicit, specific limitations and boundaries that restrict how the AI can respond, including constraints on length, format, content, style, audience, or scope.

**Validation Criteria**:

1. **Explicit Limitations Defined** ✓
   - Contains clear, specific constraints that limit the response
   - Uses quantifiable restrictions (word count, sentence limits, specific numbers)
   - Establishes firm boundaries that must be followed

2. **Multiple Constraint Types** ✓
   - Includes at least 2-3 different types of constraints
   - May combine: length, format, content, style, audience, scope, structure
   - Creates a framework that significantly shapes the response

3. **Measurable/Verifiable Constraints** ✓
   - Constraints can be objectively verified (exact word count, specific format)
   - Uses precise language: "exactly," "maximum," "must include," "no more than"
   - Avoids vague limitations that are subjective

4. **Restrictive Impact** ✓
   - Constraints meaningfully limit how the task can be completed
   - Forces the AI to work within defined parameters
   - Creates challenge in balancing multiple restrictions simultaneously

**Valid Constraint Indicators**:
- Specific numerical limits (word count, sentence count, bullet points)
- Format requirements (bullet points, specific structure, sections)
- Content restrictions (no technical details, must include specific elements)
- Style limitations (tone, audience-specific language)
- Scope boundaries (focus only on X, exclude Y completely)

**Invalid Patterns**:
- Vague suggestions without specific limits
- Single constraint that doesn't significantly restrict response
- Flexible guidelines rather than firm boundaries
- Constraints that are subjective or unmeasurable
- General advice without explicit limitations

**Note**: Constraints should create a challenging framework that forces the AI to balance multiple specific requirements while completing the task. The limitations should be objective and verifiable.
"""

class ConstraintPromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_7_constraint_pattern.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.CONSTRAINT_PATTERN

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION
