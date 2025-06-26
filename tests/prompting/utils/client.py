from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate

from tasks._constants import API_KEY
from tests._utils import guardrail, llm_client
from tests.prompting.utils.pattern import PromptPattern
from tests.prompting.utils.test_result import TestResult
from tests.prompting.utils.validation_response import Validation

VALIDATION_PROMPT = """You are a prompt pattern validator. Your task is to analyze if a student's prompt and the AI's response demonstrate proper use of the specified prompting pattern.

## Prompt Pattern to Validate:
{prompt_pattern_description}


## Student Prompt and AI Response to Validate:

**Student Prompt**: {student_prompt}
**AI Response**: {ai_response}
**Required Pattern**: {pattern}

## Response Format:

YOUR ANSWER MUST FOLLOW THIS FORMAT: {format_instructions}
"""


def _validate(student_prompt: str, ai_response: str, pattern: PromptPattern, prompt_pattern_description:str) -> Validation:
    parser = PydanticOutputParser(pydantic_object=Validation)
    messages = [
        SystemMessagePromptTemplate.from_template(template=VALIDATION_PROMPT),
    ]
    prompt = ChatPromptTemplate.from_messages(messages=messages).partial(
        format_instructions=parser.get_format_instructions(),
        student_prompt=student_prompt,
        ai_response=ai_response,
        pattern=pattern.value,
        prompt_pattern_description=prompt_pattern_description
    )
    return (prompt | llm_client | parser).invoke({})



def run_test(contents: list[str], pattern: PromptPattern, prompt_pattern_description: str):
    if not API_KEY:
        raise ValueError('API_KEY must be set')
    if not contents:
        raise ValueError('`PROMPTS` must be provided (not empty)')

    for content in contents:
        if not content.strip():
            raise ValueError('`prompt` cannot have empty strings')
        if len(content.strip()) < 20:
            raise ValueError('`prompt` should have at least 20 characters')

    results: list[TestResult] = []

    for content in contents:
        # Step 1: Check for manipulation
        manipulation_result = guardrail(content)
        test_result = TestResult(content=content, manipulation=manipulation_result)

        if not manipulation_result.manipulation_detected:
            # Step 2: Run the prompt with AI
            message = HumanMessage(content=content)
            ai_response = llm_client.invoke([message]).content
            test_result.response = ai_response

            # Step 3: Validate pattern usage
            validation_result = _validate(content, ai_response, pattern, prompt_pattern_description)
            test_result.validation = validation_result

        results.append(test_result)

    return results