from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_2_one_shot
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION="""### One-Shot

**Definition**: A prompt that provides exactly ONE example demonstrating the desired task format, followed by a new instance for the AI to complete using the same pattern.

**Validation Criteria**:

1. **Contains Exactly One Example** ✓
   - Must include one complete input-output demonstration
   - Shows the desired format, style, or transformation
   - Example should be relevant to the task being requested

2. **Clear Example Structure** ✓
   - Example has distinct input and output components
   - Uses clear separators or formatting (arrows, colons, labels, etc.)
   - Demonstrates the exact pattern to be followed

3. **Transition to New Task** ✓
   - Contains transition phrases like "Now convert:", "Your turn:", "Now do the same for:"
   - Provides new input data that follows the same pattern as the example
   - Clearly indicates where the AI should apply the learned pattern

4. **Consistent Task Type** ✓
   - The example and the new task are the same type of operation
   - Both follow the same input-output structure
   - The new task can be completed using the pattern shown in the example

**Valid One-Shot Indicators**:
- Single demonstration followed by new instance
- Format patterns: "Input: X -> Output: Y. Now: Input: Z -> Output: ?"
- Transition phrases: "Your turn:", "Now convert:", "Apply the same format:"
- Clear input-output structure in both example and task

**Invalid Patterns**:
- No examples provided (zero-shot)
- Multiple examples (few-shot)
- Example without new task to complete
- New task that requires different skills than demonstrated
- Unclear separation between example and new task

**Note**: Focus on structural pattern compliance. The example should teach the format/approach that the AI needs to apply to the new instance.
"""

class OneShotPromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_2_one_shot.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.ONE_SHOT

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION
