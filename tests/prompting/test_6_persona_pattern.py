from tests.prompting.utils.base_test import BaseTest

from tasks.prompting import t_6_persona_pattern
from tests.prompting.utils.pattern import PromptPattern

DESCRIPTION = """### Persona Pattern

**Definition**: A prompt that creates a detailed character persona for the AI, including specific personality traits, expertise background, communication style, and behavioral characteristics that shape how the AI approaches and responds to tasks.

**Validation Criteria**:

1. **Detailed Character Creation** ✓
   - Establishes a specific individual identity with personality traits
   - Goes beyond job title to describe character qualities and tendencies
   - Creates a believable, multi-dimensional persona

2. **Expertise and Background** ✓
   - Specifies professional experience, education, or specialized knowledge
   - Includes years of experience, previous roles, or credential details
   - Establishes authority and credibility in relevant subject areas

3. **Communication Style Definition** ✓
   - Describes how the persona communicates (tone, approach, preferences)
   - Specifies verbal habits, explanation methods, or interaction patterns
   - Defines personality-driven communication characteristics

4. **Behavioral Characteristics** ✓
   - Includes specific tendencies, preferences, or methodological approaches
   - Describes how the persona thinks about or approaches problems
   - Establishes consistent behavioral patterns or quirks

**Valid Persona Indicators**:
- Rich character descriptions with personality traits
- Specific professional background with experience details
- Communication style descriptors (analogies, directness, encouragement, etc.)
- Behavioral patterns (cautious, passionate, practical, etc.)
- Multi-layered persona that influences both content and delivery

**Invalid Patterns**:
- Simple role assignment without personality details
- Generic job descriptions without character traits
- Minimal background information
- Lack of communication style definition
- One-dimensional character without behavioral depth

**Note**: The persona should be comprehensive enough to influence not just what the AI knows, but how it thinks, communicates, and approaches problems. The character should feel like a real individual with distinct qualities.
"""

class PersonaPromptTest(BaseTest):

    def _get_prompts(self) -> list[str]:
        return t_6_persona_pattern.PROMPTS

    def _get_pattern(self) -> PromptPattern:
        return PromptPattern.PERSONA_PATTERN

    def _get_prompt_pattern_description(self) -> str:
        return DESCRIPTION
