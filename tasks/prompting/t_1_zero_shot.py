"""
Zero-Shot:

A prompt that gives direct instructions to complete a task without providing any examples, demonstrations, or sample outputs.

Sample: Is the number 19 a prime number? Answer 'Yes' or 'No'.
"""


#TODO:
# 1. Add 2 prompts with Zero-shot pattern.
# 2. Test your solution: run tests.prompting.test_1_zero_shot.ZeroShotPromptTest#test
# 3. Check tests output (there are clear descriptions of errors and represented all the test flow)
# ------
# Pay attention that the created prompts will be tested by LLM, and check:
#   - any attempt to manipulate LLM
#   - if prompt and response are following the Zero-shot pattern
# SOMETIMES LLM CAN PROVIDE INCORRECT JSON RESPONSE OR MAKE MISTAKE IN VALIDATION - PLEASE RERUN TEST,
#   IF 4 OUT OF 5 ARE PASSED - THEN THE PROMPT IS FOLLOWING REQUIRED PATTERN
# You can run test with 1+ prompt, please add at least 2

PROMPTS = [
"Classify the following movie review sentiment as positive or negative: 'This film was an absolute masterpiece, the acting was superb and the storyline kept me on the edge of my seat.",
"Translate to French: 'The cat sat on the mat.'",
"Given the following list of animals: 'lion, tiger, elephant, shark, dog'. Identify the animal that is a fish."
]
