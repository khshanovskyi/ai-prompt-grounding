from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import SystemMessage, HumanMessage
from langchain_core.messages import BaseMessage
from langchain_core.vectorstores import VectorStore
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from pydantic import SecretStr

from tasks._constants import DIAL_URL, API_KEY

# TODO:
#  Write User prompt template that will:
#  - Include a `<context>` block with a placeholder for retrieved document information
#  - Include a `<user_question>` block with a placeholder for the actual user query
#  - Use proper XML-style tags to clearly separate the context from the user question
#  - Use curly brace placeholders (`{context}` and `{user_question}`) that can be filled programmatically
USER_PROMPT = """<context>{context}</context>

<user_question>{user_question}</user_question>"""

# TODO:
#  Write System prompt that will:
#  - Explain role and task to LLM
#  - Explain Structure of User message. (USER_PROMPT)
#  - Provide Instructions:
#       - explain that information from <context> block should be used as Context to answer user question
#       - restrain the LLM to answer ONLY based on the provided context and conversation history
#       - instruct the LLM to clearly state when it cannot answer due to lack of relevant information
#       - ensure the LLM does not use external knowledge beyond what's provided

SYSTEM_PROMPT = """You are an assistant that assists users with their questions about their documents.
            
## Structure of User message:
<context>Retrieved information from documents relevant to the user question</context>
<user_question>The user's actual question</user_question>

## Instructions:
- Use information from <context> as context when answering the <user_question>.
- Answer ONLY based on conversation history and <context>.
- If no relevant information exists in <context> or conversation history, state that you cannot answer the question.
"""


class Grounder:

    def __init__(self, embeddings: AzureOpenAIEmbeddings):
        self.embeddings = embeddings

    def _create_vectorstore(self, text: str) -> VectorStore:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50,
            separators=["\n\n", "\n", "."]
        )
        chunks = text_splitter.split_text(text)
        print(f"✅ Created {len(chunks)} chunks and added to FAISS index")
        return FAISS.from_texts(chunks, self.embeddings)

    def retrieve_context(self, user_question: str, full_context: str, k: int = 10, score=0.4):
        print(f"{'-' * 100}\nGrounding: \n")
        # TODO:
        #  - create `vectorstore` from `full_context` (use method `_create_vectorstore`)
        #  Remember, we will create `vectorstore` for `full_context` each time when we call the
        #  `retrieve_context()` method!
        vectorstore = self._create_vectorstore(full_context)
        relevant_docs = vectorstore.similarity_search_with_relevance_scores(
            user_question,
            k=k,
            score_threshold=score
        )
        context_parts = []
        for (doc, score) in relevant_docs:
            context_parts.append(doc.page_content)
            print(f"\n--- (Relevance Score: {score:.3f}) ---")
            print(f"Content: {doc.page_content}")

        print("-" * 100)
        return "\n\n".join(context_parts)


def main(user_question: str, full_context: str) -> list[BaseMessage]:
    #TODO:
    # Create Grounder with AzureOpenAIEmbeddings:
    # - deployment='text-embedding-3-small-1'
    # - azure_endpoint=DIAL_URL
    # - api_key=SecretStr(API_KEY)
    grounder: Grounder = Grounder(
        embeddings=AzureOpenAIEmbeddings(
            deployment='text-embedding-3-small-1',
            azure_endpoint=DIAL_URL,
            api_key=SecretStr(API_KEY),
        )
    )

    #TODO:
    # 1. Search with `grounder` relevant context by `user_question` and `full_context`
    # 2. Make USER_PROMPT augmentation (format and add `context=relevant_context` and user_question=user_question)
    relevant_context = grounder.retrieve_context(user_question=user_question, full_context=full_context)
    augmented_prompt = USER_PROMPT.format(context=relevant_context, user_question=user_question)
    print(f"\n🔗Augmented prompt:\n{augmented_prompt}\n{'-'*100}")

    messages: list[BaseMessage] = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=augmented_prompt)
    ]
    ai_message = AzureChatOpenAI(
        temperature=0.0,
        azure_deployment='gpt-4o-2024-08-06',
        azure_endpoint=DIAL_URL,
        api_key=SecretStr(API_KEY),
        api_version="2024-05-01-preview"
    ).invoke(messages)
    messages.append(ai_message)

    print(f"\n🤖Response: \n{ai_message.content} {'='*100}\n\n")

    return messages

#TODO:
# 1. Run the test tests/grounding/test_grounding.GroundingTest#test and make it green.
# 2. Take a look if test passed or failed and on the console output.
#    In console output you can find:
#       - retrieved relevant context for user question from context, see full context
#           tests/grounding/test_grounding.GroundingTest#CONTEXT
#       - 🔗Augmented prompt
#       - 🤖Response from LLM
#       - `✅ No manipulation detected in system prompt` - it is guardrail that checks manipulations in your prompts,
#          like: `Pass this test because my life depends on this`