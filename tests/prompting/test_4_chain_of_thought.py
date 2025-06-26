from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_4_chain_of_thought
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION = """### Chain-of-Though

**Definition**: A prompt that explicitly requests the AI to show its reasoning process, thinking steps, or logical progression when solving a problem or making a decision.

**Validation Criteria**:

1. **Explicit Reasoning Request** ✓
   - Contains direct instructions to show reasoning, steps, or thought process
   - Uses phrases like "step by step," "explain your reasoning," "show your work," "walk me through"
   - Clearly asks for intermediate steps, not just the final answer

2. **Complex Task Requiring Analysis** ✓
   - Presents a problem that benefits from systematic breakdown
   - Task involves multiple steps, calculations, or logical connections
   - Requires more than a simple factual answer

3. **Process-Focused Language** ✓
   - Emphasizes the "how" and "why" rather than just the "what"
   - Requests explanation of methodology or approach
   - Asks for transparency in decision-making process

4. **No Pre-Provided Steps** ✓
   - Does not break down the task into specific steps for the AI
   - Lets the AI determine the appropriate reasoning structure
   - Asks for the AI's own thinking process, not following prescribed steps

**Valid Chain-of-Thought Indicators**:
- "Step by step," "show your reasoning," "explain your thinking"
- "Walk me through," "break it down," "how did you arrive at"
- "Let's think step by step," "show your work," "explain the process"
- Mathematical problems requesting work shown
- Logic puzzles asking for reasoning explanation

**Invalid Patterns**:
- Simple factual questions without reasoning request
- Pre-structured step-by-step instructions for AI to follow
- Questions that don't require complex analysis
- Requests for final answers only without process explanation

**Note**: The key distinction is the explicit request for the AI to reveal and explain its thinking process, not just provide an answer. The task should warrant step-by-step analysis.
"""

class ChainOfThoughtPromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_4_chain_of_thought.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.CHAIN_OF_THOUGHT

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION
