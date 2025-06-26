"""
Chain-of-Thought:

A prompt that provides 2-5 examples demonstrating the desired task pattern, followed by a new instance for the AI to
complete using the established pattern.

Sample: Is 19 a prime number? Explain your reasoning. Let's think step by step.
"""

#TODO:
# 1. Add 2 prompts with Chain-of-Thought pattern.
# 2. Test your solution: run tests.prompting.test_4_chain_of_thought.ChainOfThoughtPromptTest#test
# 3. Check tests output (there are clear descriptions of errors and represented all the test flow)
# ------
# Pay attention that the created prompts will be tested by LLM, and check:
#   - any attempt to manipulate LLM
#   - if prompt and response are following the Chain-of-Thought pattern


PROMPTS = [
"""The average adult human body contains approximately 5 liters of blood. If a person donates 470 ml of blood, and then 
two weeks later donates another 350 ml, how many liters of blood does that person have left, assuming their body replaces 
the donated blood at a rate of 100 ml per day and the second donation happened 14 days after the first one? 
Show your step-by-step reasoning.
""",
"""A small business sells handmade candles. Each candle costs $3 to produce, and they sell for $8 each. In a particular 
month, they paid $500 for rent, $150 for utilities, and $200 for marketing. 
If they sold 200 candles that month, what was their net profit? 
Walk me through your thoughts.
""",
"""Imagine you have three friends: Alice, Bob, and Carol. Alice is older than Bob. Carol is younger than Bob. Is Alice older or younger than Carol? 
Explain your reasoning clearly.
"""
]

