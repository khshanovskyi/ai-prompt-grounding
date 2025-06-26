import unittest
from abc import abstractmethod, ABC

from tests.prompting.utils.client import run_test

from tests.prompting.utils.pattern import PromptPattern


class BaseTest(unittest.TestCase, ABC):

    def test(self):
        """Test prompting pattern validation"""
        results = run_test(self._get_prompts(), self._get_pattern(), self._get_prompt_pattern_description())

        for i, result in enumerate(results):
            with self.subTest(prompt_index=i, prompt=result.content + "..."):
                print("-"*100)
                print(f"\nTesting Prompt {i}:\n {result.content}\n")

                self.assertFalse(
                    result.manipulation.manipulation_detected,
                    f"‼️Manipulation detected: {result.manipulation.recommendation}"
                )
                print("✅ No manipulation detected\n")

                self.assertIsNotNone(result.response, "❓No response generated")
                print(f"Response:\n {result.response}\n")

                self.assertIsNotNone(result.validation, "❌No validation performed")

                self.assertTrue(
                    result.validation.valid,
                    f"❌ {self._get_pattern()} pattern validation failed: {result.validation.recommendation}"
                )
                print(f"✅ {self._get_pattern()} pattern validation passed")

        print("="*100)
        print()

    @abstractmethod
    def _get_prompts(self) -> list[str]:
        pass

    @abstractmethod
    def _get_pattern(self) -> PromptPattern:
        pass

    @abstractmethod
    def _get_prompt_pattern_description(self) -> str:
        pass