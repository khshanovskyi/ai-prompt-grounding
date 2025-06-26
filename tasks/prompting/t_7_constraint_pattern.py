"""
Constraint Pattern:

A prompt that sets explicit, specific limitations and boundaries that restrict how the AI can respond, including
constraints on length, format, content, style, audience, or scope.

Sample:
    Write a product description for a smartphone.
    Constraints:
        - Exactly 50 words
        - Include 3 key features
        - Use active voice only
        - Target audience: tech-savvy millennials
        - Avoid technical jargon
"""

#TODO:
# 1. Add 2 prompts with constraint pattern.
# 2. Test your solution: run tests.prompting.test_7_constraint_pattern.ConstraintPromptTest#test
# 3. Check test output for validation

PROMPTS = [
    """Create a business proposal for a new mobile app. 
    Constraints:
    - Maximum 200 words total
    - Must include: problem statement, solution, target market, revenue model
    - Use bullet points for key information
    - No technical details about implementation
    - Focus on business value only
    - Include at least one statistic or market data point
    - End with a clear call to action""",

    """Write a code review comment for a junior developer's pull request.
    Constraints:
    - Maximum 3 sentences
    - Must be constructive and encouraging
    - Include exactly 1 specific improvement suggestion
    - Include exactly 1 positive observation
    - Use professional but friendly tone
    - No code examples in the feedback
    - End with a question to promote learning
    Code being reviewed: A function that processes user input but doesn't validate the input format."""
]