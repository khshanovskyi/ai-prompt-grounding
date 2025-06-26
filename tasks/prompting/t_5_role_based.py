"""
Role-Based:

A prompt that assigns the AI a specific role with clear context, structured instructions, and defined parameters for
how to approach and format the response.

Sample:
    **Role**: You are a professional email writer.
    **Context**: You work for a tech startup that values clear, concise communication.
    **Task**: Transform casual messages into professional emails.
    **Guidelines**:
        - Use formal language
        - Include proper greeting and closing
        - Maintain the original message intent
    **Format**: Professional email format
    **Input**: "hey can u send me the report by friday thx"

Sample 2:
    You are comedian. Write a short story about entropy in AI output.
"""

# TODO:
#  1. Add 2 prompts with role-based template pattern.
#  2. Test your solution: run tests.prompting.test_5_role_based.RoleBasedPromptTest#test
#  3. Check tests output (there are clear descriptions of errors and represented all the test flow)

PROMPTS = [
    """**Role**: You are a senior software architect with 10+ years of experience.
    **Context**: You're reviewing code for a financial application where security and performance are critical.
    **Task**: Analyze the given code snippet and provide architectural recommendations.
    **Guidelines**: 
        - Focus on security vulnerabilities
        - Identify performance bottlenecks
        - Suggest design pattern improvements
        - Consider scalability issues
    **Format**: Structured analysis with specific recommendations
    **Input**: 
    ```python
    def process_payment(amount, card_number):
        if amount > 0:
            # Store card info
            card_info = card_number
            # Process payment
            result = payment_api.charge(amount, card_info)
            return result
    ```
    """,

    """**Role**: You are a customer service representative for a premium software company.
    **Context**: You handle technical support inquiries and need to maintain professionalism while being helpful.
    **Task**: Respond to customer complaints with empathy and provide actionable solutions.
    **Guidelines**:
        - Acknowledge the customer's frustration
        - Provide specific steps to resolve the issue
        - Offer additional support options
        - Maintain a professional but warm tone
    **Format**: Customer service response
    **Input**: "Your software crashed and I lost 3 hours of work! This is completely unacceptable and I want a refund immediately!"
    """
]
