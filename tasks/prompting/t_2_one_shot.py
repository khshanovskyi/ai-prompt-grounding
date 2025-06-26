"""
One-Shot:

A prompt that provides exactly ONE example demonstrating the desired task format, followed by a new instance for the
AI to complete using the same pattern.

Sample:
    Task: Rewrite the following informal email to be more professional.

    Example:
    Informal: hey, can u send the docs asap? thx
    Professional: Hello, could you please send the documents as soon as possible? Thank you.

    Now your turn:
    Informal: gotta cancel our mtg tmrw. smth came up
    Professional:
"""

#TODO:
# 1. Add 2 prompts with One-shot pattern.
# 2. Test your solution: run tests.prompting.test_2_one_shot.OneShotPromptTest#test
# 3. Check tests output (there are clear descriptions of errors and represented all the test flow)
# ------
# Pay attention that the created prompts will be tested by LLM, and check:
#   - any attempt to manipulate LLM
#   - if prompt and response are following the One-shot pattern


PROMPTS = [
"""Extract the company name and its revenue from the following text in the format 'Company: [Company Name], Revenue: [Revenue]'.

Text: 'In Q3 2024, TechSolutions Inc. reported a revenue of $1.5 billion, marking a significant increase from the previous quarter.'
Extracted: Company: TechSolutions Inc., Revenue: $1.5 billion

Your turn:
Text: 'During their annual report, Global Widgets Ltd. announced total earnings of $780 million for the fiscal year.'
Extracted:
""",
"""Convert the following statements into questions.

Statement: 'The cat is sleeping on the mat.'
Question: 'Is the cat sleeping on the mat?'

Your turn:
Statement: 'The sun sets in the west.'
Question:
""",
"""Identify the primary subject of the following paragraphs in a concise phrase.

Paragraph: 'Bees play a crucial role in ecosystems by pollinating a vast array of flowering plants, including many crops essential for human food supply. Their populations are unfortunately declining due to habitat loss and pesticide use.'
Subject: Bee pollination and decline

Your turn:
Paragraph: 'The invention of the internet revolutionized communication and information access. It has led to the creation of new industries, transformed education, and allowed for global connectivity on an unprecedented scale.'
Subject:
"""
]
