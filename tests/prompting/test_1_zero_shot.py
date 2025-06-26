from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_1_zero_shot
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION="""### Zero-Shot

**Definition**: A prompt that gives direct instructions to complete a task without providing any examples, demonstrations, or sample outputs.

**Validation Criteria**:

1. **Contains Direct Task Instruction** ✓
   - Has a clear, actionable command or question
   - Uses imperative verbs (classify, translate, identify, solve, etc.) or direct questions

2. **No Examples or Demonstrations** ✓
   - Must NOT contain input-output pairs showing how to complete the task
   - Must NOT include phrases like "For example:", "Like this:", "Here's how:", or "Sample:"
   - Must NOT show sample responses or expected answer formats beyond basic constraints

3. **No Step-by-Step Guidance** ✓
   - Does not break down the task into multiple steps
   - Does not provide a methodology or process to follow

4. **Self-Contained Task** ✓
   - All necessary information to complete the task is within the prompt
   - Does not reference external examples or previous interactions

**Valid Zero-Shot Indicators**:
- Direct commands: "Classify...", "Translate...", "Identify...", "Determine..."
- Simple format constraints: "Answer 'Yes' or 'No'", "in one word", "as a percentage"
- Content to be processed is provided directly in the prompt

**Invalid Patterns**:
- Any demonstration of expected input-output format
- Multiple examples showing the pattern
- Step-by-step instructions on how to approach the task
- References to previous examples or conversations

**Note**: Focus on prompt structure, not AI response quality. A malformed sentence (like missing quotes) doesn't invalidate the zero-shot pattern if the structure is correct.
"""

class ZeroShotPromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_1_zero_shot.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.ZERO_SHOT

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION