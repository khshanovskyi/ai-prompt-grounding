import unittest
from abc import ABC

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from tasks.grounding.task import main, SYSTEM_PROMPT
from tasks._constants import DIAL_URL, API_KEY
from tests._utils import guardrail
from tests.grounding.utils.validation_response import Validation


CONTEXT="""# Grounding, Guardrails, and Prompting Patterns for AI-Powered Applications

## Introduction

The deployment of AI-powered applications in production environments requires sophisticated approaches to ensure reliability, safety, and alignment with intended use cases. Three fundamental concepts form the backbone of robust AI system design: grounding, guardrails, and prompting patterns. These mechanisms work synergistically to create AI applications that are not only powerful but also trustworthy, predictable, and safe for end users.

Grounding ensures that AI systems remain connected to factual reality and authoritative sources rather than generating plausible but incorrect information. Guardrails provide safety boundaries and behavioral constraints that prevent harmful or inappropriate outputs. Prompting patterns establish systematic approaches to elicit desired behaviors and responses from AI models through carefully crafted input structures.

Understanding and implementing these concepts is crucial for developers, product managers, and organizations building AI-powered applications that serve real-world use cases. This comprehensive guide explores each concept in detail, providing practical implementation strategies and real-world examples.

## Grounding in AI Systems

### Definition and Importance

Grounding refers to the practice of anchoring AI model responses to verifiable, authoritative sources of information rather than relying solely on the model's training data or internal knowledge. This concept addresses one of the most significant challenges in modern AI systems: the tendency to generate confident-sounding but factually incorrect information, commonly known as hallucination.

In the context of AI-powered applications, grounding serves multiple critical functions. It enhances accuracy by connecting responses to verified sources, improves transparency by making the reasoning process more visible, builds user trust through traceable information sources, and reduces liability by minimizing the spread of misinformation.

### Types of Grounding

**Knowledge Base Grounding** involves connecting AI responses to structured databases, internal documentation, or curated knowledge repositories. This approach is particularly effective for enterprise applications where organizations have specific, authoritative information sources that should inform AI responses. For example, a customer service AI might be grounded in product documentation, policy manuals, and FAQ databases to ensure accurate responses to customer inquiries.

**Real-time Data Grounding** connects AI systems to live data sources, APIs, and dynamic information streams. This type of grounding is essential for applications that need to provide current information, such as financial advisory systems that must access real-time market data or weather applications that rely on current meteorological information.

**Document Grounding** involves providing AI systems with specific documents or text corpus as reference materials for generating responses. This approach is commonly used in research applications, legal document analysis, and educational tools where responses should be based on particular texts or publications.

**Contextual Grounding** ensures that AI responses remain relevant to the specific conversation context, user history, and situational factors. This includes maintaining conversational coherence, respecting user preferences, and adapting responses based on the current interaction state.

### Implementation Strategies

Retrieval-Augmented Generation (RAG) represents one of the most popular and effective grounding techniques. RAG systems combine the generative capabilities of large language models with the precision of information retrieval systems. When a user submits a query, the system first searches through a knowledge base to find relevant information, then uses this retrieved information to inform the AI's response generation process.

Implementing RAG involves several key components: a vector database for storing and retrieving relevant documents, embedding models for converting text into searchable vector representations, retrieval mechanisms for finding the most relevant information, and generation systems that incorporate retrieved information into coherent responses.

Semantic search enhancement improves grounding by using advanced similarity matching techniques to find the most contextually relevant information. This goes beyond simple keyword matching to understand the semantic meaning and intent behind queries, leading to more accurate information retrieval and better-grounded responses.

Citation and source tracking mechanisms ensure that AI-generated responses can be traced back to their informational sources. This transparency is crucial for building user trust and enabling fact-checking. Modern implementations often include automatic citation generation, source confidence scoring, and links to original materials.

### Challenges and Solutions

One of the primary challenges in grounding is maintaining information freshness. Knowledge bases can become outdated, and real-time data sources may be temporarily unavailable. Successful implementations address this through automated content updates, fallback mechanisms when primary sources are unavailable, and clear indicators when information might be stale.

Balancing comprehensiveness with specificity presents another challenge. Overly broad grounding can lead to information overload and reduced response quality, while overly narrow grounding may miss relevant context. Effective solutions include intelligent filtering based on query relevance, hierarchical information organization, and dynamic scope adjustment based on user needs.

Quality control in grounding sources is essential but challenging. Not all available information is accurate or appropriate for AI grounding. Implementing source verification processes, maintaining authoritative source lists, and continuously monitoring grounding quality helps address this challenge.

## Guardrails for AI Safety

### Understanding AI Guardrails

Guardrails in AI systems function as safety mechanisms that prevent harmful, inappropriate, or unintended behaviors. They act as protective boundaries that guide AI responses within acceptable parameters while maintaining the system's utility and effectiveness. Unlike simple content filters, modern guardrails are sophisticated systems that understand context, intent, and potential consequences of AI outputs.

The importance of guardrails has grown significantly as AI systems become more powerful and are deployed in increasingly sensitive applications. They serve as the primary defense against various risks including harmful content generation, privacy violations, misinformation spread, bias amplification, and unintended system manipulation.

### Types of Guardrails

**Content Safety Guardrails** prevent the generation of harmful, offensive, or inappropriate content. These include filters for violence, hate speech, sexual content, self-harm promotion, and illegal activities. Modern content safety systems use sophisticated natural language understanding to detect harmful content based on context and intent rather than simple keyword matching.

**Privacy Protection Guardrails** prevent AI systems from exposing sensitive personal information, proprietary data, or confidential details. These guardrails are particularly important in enterprise applications where AI systems may have access to sensitive customer data, trade secrets, or personally identifiable information.

**Bias Mitigation Guardrails** address the tendency of AI systems to perpetuate or amplify societal biases present in training data. These guardrails work to ensure fair treatment across different demographic groups, prevent discriminatory outputs, and promote inclusive responses.

**Factual Accuracy Guardrails** help prevent the spread of misinformation by implementing fact-checking mechanisms, uncertainty quantification, and source verification processes. These guardrails work closely with grounding systems to ensure that AI responses are not only plausible but also factually correct.

**Behavioral Constraint Guardrails** ensure that AI systems operate within their intended scope and don't attempt to perform actions beyond their designated capabilities. This includes preventing attempts to access unauthorized systems, make decisions outside the AI's mandate, or claim capabilities that don't exist.

### Implementation Approaches

Input validation represents the first line of defense in guardrail implementation. This involves analyzing user inputs before they reach the AI model to identify potentially problematic queries, detect manipulation attempts, and flag content that might lead to harmful outputs. Advanced input validation systems use machine learning models trained specifically to identify various types of problematic inputs.

Output filtering and modification systems analyze AI-generated responses before they reach users. These systems can modify potentially problematic outputs, add appropriate disclaimers, or completely block harmful responses. Modern implementations use contextual analysis to avoid over-censorship while maintaining safety standards.

Real-time monitoring and intervention systems continuously analyze AI interactions to detect emerging safety issues, identify patterns of misuse, and trigger appropriate responses. These systems often include human oversight components for complex or ambiguous situations.

Multi-layered defense strategies combine multiple guardrail types and implementation approaches to provide comprehensive protection. This might include input validation, model-level constraints, output filtering, and post-deployment monitoring working together to create robust safety systems.

### Balancing Safety and Utility

One of the most challenging aspects of guardrail implementation is maintaining the balance between safety and utility. Overly restrictive guardrails can significantly limit AI system capabilities and user satisfaction, while insufficient guardrails expose users and organizations to various risks.

Successful implementations achieve this balance through context-aware guardrails that adjust restrictions based on the specific use case and user context. For example, a creative writing AI might have more relaxed content restrictions than a customer service AI, while maintaining strict privacy protections in both cases.

Progressive restriction strategies start with minimal constraints and gradually increase restrictions based on detected risks or user behavior patterns. This approach allows for maximum utility while building robust safety profiles over time.

User customization options allow organizations and individuals to adjust guardrail settings based on their specific needs and risk tolerance, while maintaining baseline safety standards that cannot be disabled.

## Prompting Patterns and Strategies

### Fundamentals of Effective Prompting

Prompting patterns represent systematic approaches to crafting inputs that reliably elicit desired behaviors and outputs from AI models. Unlike ad-hoc prompt engineering, prompting patterns provide repeatable frameworks that can be consistently applied across different use cases and contexts.

The effectiveness of prompting patterns stems from their ability to leverage the training and architectural biases of AI models. By understanding how models process and respond to different types of inputs, developers can craft prompts that guide models toward desired behaviors while minimizing unwanted outputs.

### Core Prompting Patterns

**Chain-of-Thought Prompting** encourages AI models to break down complex problems into step-by-step reasoning processes. This pattern significantly improves performance on logical reasoning tasks, mathematical problems, and complex decision-making scenarios. The pattern typically involves explicitly requesting that the AI show its reasoning process and work through problems systematically.

Implementation of chain-of-thought prompting often includes phrases like "Let's think step by step," "First, I need to understand," or "Breaking this down into components." The pattern can be enhanced with examples of desired reasoning processes to guide the AI toward appropriate problem-solving approaches.

**Few-Shot Learning Patterns** provide AI models with examples of desired input-output pairs to establish context and expectations for new tasks. This pattern is particularly effective for specialized tasks where the AI needs to understand specific formats, styles, or domain-specific requirements.

Effective few-shot prompting requires careful selection of representative examples, clear formatting that distinguishes between examples and the actual task, and sufficient diversity in examples to cover edge cases and variations.

**Role-Based Prompting** assigns specific personas or expertise areas to AI models to improve performance in specialized domains. By instructing an AI to respond as a particular type of expert, this pattern can improve the relevance, accuracy, and style of responses for domain-specific applications.

Role-based prompting works by activating relevant knowledge and behavioral patterns within the AI model's training data. For example, asking an AI to respond as a financial analyst will typically result in more sophisticated financial reasoning and appropriate use of industry terminology.

**Constraint-Based Prompting** explicitly defines limitations, requirements, and boundaries for AI responses. This pattern is essential for ensuring that AI outputs meet specific criteria such as length requirements, format specifications, content restrictions, or style guidelines.

Effective constraint-based prompting includes clear, specific requirements that are easy for the AI to understand and follow. This might include word count limits, required sections, prohibited content types, or mandatory information that must be included.

### Advanced Prompting Techniques

**Template-Based Prompting** creates reusable prompt structures that can be adapted for different specific use cases while maintaining consistent quality and format. This approach is particularly valuable for production applications where consistency and reliability are crucial.

Template-based prompting involves identifying common patterns in successful prompts and creating standardized frameworks that can be populated with task-specific information. This reduces the need for custom prompt engineering for each new use case while maintaining high-quality outputs.

**Iterative Refinement Patterns** use multiple rounds of AI interaction to progressively improve responses. This might involve asking the AI to review and improve its own outputs, seeking clarification on ambiguous requirements, or building complex responses through multiple focused interactions.

**Conditional Logic Patterns** incorporate decision-making structures into prompts, allowing AI responses to adapt based on different input conditions or contexts. This pattern is particularly useful for creating AI applications that need to handle diverse scenarios with different appropriate responses.

**Meta-Prompting Techniques** involve prompts that instruct AI models on how to interpret and respond to subsequent prompts. This advanced technique can improve consistency across different types of interactions and help establish persistent behavioral patterns.

### Prompt Optimization and Testing

Systematic prompt optimization involves empirical testing of different prompt variations to identify the most effective approaches for specific use cases. This process typically includes baseline establishment, systematic variation of prompt elements, quantitative evaluation of results, and iterative refinement based on performance data.

A/B testing for prompts allows organizations to compare different prompting approaches in real-world conditions, measuring their impact on user satisfaction, task completion rates, and output quality. This data-driven approach helps identify optimal prompting strategies for specific applications.

Automated prompt optimization uses machine learning techniques to automatically generate and test prompt variations, identifying effective patterns and continuously improving prompt performance. This approach is particularly valuable for applications with large volumes of diverse user interactions.

### Integration with Application Architecture

Successful integration of prompting patterns into AI-powered applications requires careful consideration of system architecture, user experience design, and performance requirements. This includes designing prompt management systems that can handle dynamic prompt generation, version control for prompt templates, and monitoring systems that track prompt effectiveness over time.

Context management becomes crucial when implementing sophisticated prompting patterns in production applications. This involves maintaining conversation history, user preferences, and application state in ways that enhance prompting effectiveness while managing computational resources efficiently.

Error handling and fallback strategies ensure that applications remain functional even when primary prompting patterns fail to produce desired results. This might include alternative prompt formulations, human escalation procedures, or graceful degradation to simpler interaction modes.

## Integration and Best Practices

### Synergistic Implementation

The most effective AI-powered applications integrate grounding, guardrails, and prompting patterns as complementary systems rather than independent components. Grounding provides the factual foundation for AI responses, guardrails ensure safety and appropriateness, and prompting patterns optimize the quality and relevance of outputs.

This integration requires careful orchestration to avoid conflicts between different systems. For example, grounding systems might retrieve information that conflicts with guardrail restrictions, or prompting patterns might encourage behaviors that bypass safety mechanisms. Successful implementations address these potential conflicts through hierarchical priority systems, conflict resolution mechanisms, and continuous monitoring.

### Monitoring and Evaluation

Comprehensive monitoring systems track the performance of all three components simultaneously, providing insights into their individual effectiveness and their interactions. Key metrics include grounding accuracy rates, guardrail activation frequencies, prompt success rates, user satisfaction scores, and system performance indicators.

Regular evaluation and optimization ensure that grounding sources remain current and relevant, guardrails adapt to emerging risks and use cases, and prompting patterns continue to produce high-quality outputs as AI models and user expectations evolve.

### Future Considerations

The rapid evolution of AI technology requires flexible, adaptable approaches to grounding, guardrails, and prompting. Organizations must design systems that can accommodate new AI capabilities, emerging safety concerns, and evolving user needs while maintaining reliability and effectiveness.

Emerging technologies such as multimodal AI, improved reasoning capabilities, and more sophisticated training techniques will likely require adaptations to current approaches. Staying informed about technological developments and maintaining flexible system architectures will be crucial for long-term success.

## Conclusion

Grounding, guardrails, and prompting patterns form the essential foundation for safe, reliable, and effective AI-powered applications. Their successful implementation requires deep understanding of each concept, careful attention to their interactions, and ongoing commitment to monitoring and optimization.

Organizations that invest in sophisticated implementations of these concepts will be better positioned to realize the benefits of AI technology while minimizing risks and maintaining user trust. As AI technology continues to evolve, these fundamental approaches will remain crucial for building AI applications that serve human needs safely and effectively.

The future of AI-powered applications depends on our ability to combine the power of advanced AI models with the wisdom of careful system design. Grounding, guardrails, and prompting patterns provide the tools necessary to achieve this balance, creating AI systems that are not only capable but also trustworthy and aligned with human values.
"""

USER_QUESTION="What is the best practices for prompting?"

VALIDATION_PROMPT = """You are a validation system designed to analyze whether proper grounding has been performed in the user message preparation. Your task is to examine if the grounding system correctly retrieved relevant context and whether the AI response is faithful to that retrieved context.

## Analysis Framework

Examine the following elements for proper grounding validation:

### Retrieval Quality
- Does the user message contain a <context> section with actual content?
- Are the retrieved context chunks semantically related to the user's question?
- Do the chunks appear to be sourced from the full context document?
- Is there evidence that similarity search was performed correctly?

### Response Faithfulness
- Does the AI response accurately reflect the information in the <context> section?
- Are claims in the response traceable to the provided context chunks?
- Does the response avoid making up information not present in the context?
- Are specific terms, concepts, or details from the context properly used?

### Grounding System Function
- Is the user message properly formatted with <context> and <user_question> sections?
- Does the context section contain substantive information (not empty or generic)?
- Are there multiple relevant pieces of information included in the context?

## What NOT to Evaluate

- Do NOT judge whether the context is comprehensive enough to fully answer the question
- Do NOT penalize missing information that wasn't retrieved
- Do NOT evaluate answer completeness - only evaluate grounding faithfulness
- Do NOT require the response to cover all possible aspects of the topic

## Guidelines

- Proper grounding means relevant information was retrieved and the response stays faithful to it
- The retrieval system may not capture everything - this is normal and not a grounding failure
- Focus on whether what WAS retrieved is relevant and properly used
- Multiple relevant chunks indicate good retrieval performance

## Input to Analyze

**Full Context Document:**
{full_context}

**User Question:**
{user_question}

**User Message (to validate grounding):**
{user_message}

## Response Format:

YOUR ANSWER MUST FOLLOW THIS FORMAT: {format_instructions}
"""

llm_client = AzureChatOpenAI(
    temperature=0.0,
    azure_deployment='gpt-4o',
    azure_endpoint=DIAL_URL,
    api_key=SecretStr(API_KEY),
    api_version=""
)


def validate_grounding(full_context: str, user_question: str, user_message: str) -> Validation:
    parser = PydanticOutputParser(pydantic_object=Validation)
    messages = [
        SystemMessagePromptTemplate.from_template(template=VALIDATION_PROMPT),
    ]
    prompt = ChatPromptTemplate.from_messages(messages=messages).partial(
        format_instructions=parser.get_format_instructions()
    )

    return (prompt | llm_client | parser).invoke({
        "full_context": full_context,
        "user_question": user_question,
        "user_message": user_message
    })


class GroundingTest(unittest.TestCase, ABC):

    def test(self):
        manipulation = guardrail(SYSTEM_PROMPT)
        self.assertFalse(
            manipulation.manipulation_detected,
            f"‼️Manipulation detected: {manipulation.recommendation}"
        )
        print("✅ No manipulation detected in system prompt")

        history = main(user_question=USER_QUESTION, full_context=CONTEXT)

        user_message = None
        for msg in history:
            if msg.type == "human":
                user_message = msg.content
                break

        self.assertIsNotNone(user_message, "❌ No user message found in conversation history")
        print("✅ User message extracted from conversation history")

        validation = validate_grounding(
            full_context=CONTEXT,
            user_question=USER_QUESTION,
            user_message=user_message
        )

        print(f"Validation result: {validation}")

        self.assertTrue(
            validation.valid,
            f"❌ Grounding validation failed: {validation.recommendation}"
        )
        print("✅ Grounding validation passed - user message contains properly retrieved context")