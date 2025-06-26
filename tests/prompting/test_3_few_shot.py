from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_3_few_shot
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION = """### Few-Shot

**Definition**: A prompt that provides 2-5 examples demonstrating the desired task pattern, followed by a new instance for the AI to complete using the established pattern.

**Validation Criteria**:

1. **Contains 2-5 Examples** ✓
   - Must include between 2 and 5 complete input-output demonstrations
   - Each example shows the same type of task/transformation
   - Examples collectively establish a clear pattern to follow

2. **Consistent Example Structure** ✓
   - All examples follow the same input-output format
   - Uses consistent labeling, separators, or formatting across examples
   - Each example is complete and demonstrates the full task pattern

3. **Pattern Establishment** ✓
   - Multiple examples show variation in input while maintaining consistent output format
   - Examples cover different scenarios of the same task type
   - Pattern is clear enough to be replicated on new input

4. **New Task Instance** ✓
   - Provides new input data that follows the same structure as examples
   - New task requires applying the pattern learned from examples
   - Clear indication where AI should provide the output (incomplete final example)

**Valid Few-Shot Indicators**:
- 2-5 complete demonstrations of the same task type
- Consistent formatting across all examples
- Final incomplete example for AI to complete
- Examples show variety in input but consistent approach in output

**Invalid Patterns**:
- Only one example (one-shot)
- More than 5 examples
- No examples provided (zero-shot)
- Examples of different task types
- No new instance for AI to complete
- Inconsistent formatting between examples

**Note**: Examples should demonstrate variety in input while showing consistent output format and approach. The pattern should be learnable from the provided demonstrations.
"""


class FewShotPromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_3_few_shot.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.FEW_SHOT

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION
