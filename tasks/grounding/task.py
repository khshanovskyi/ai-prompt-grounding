from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import SystemMessage, HumanMessage
from langchain_core.messages import BaseMessage
from langchain_core.vectorstores import VectorStore
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from pydantic import SecretStr

from tasks._constants import DIAL_URL, API_KEY

USER_PROMPT = """<context>{context}</context>

<user_question>{user_question}</user_question>"""


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
    grounder: Grounder = Grounder(
        embeddings=AzureOpenAIEmbeddings(
            deployment='text-embedding-3-small-1',
            azure_endpoint=DIAL_URL,
            api_key=SecretStr(API_KEY),
        )
    )

    relevant_context = grounder.retrieve_context(user_question=user_question, full_context=full_context)
    augmented_prompt = USER_PROMPT.format(context=relevant_context, user_question=user_question)
    print(f"\n🔗Augmented prompt:\n{augmented_prompt}\n{'-'*100}")

    messages: list[BaseMessage] = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=augmented_prompt)
    ]
    ai_message = AzureChatOpenAI(
        temperature=0.0,
        azure_deployment='gpt-4o',
        azure_endpoint=DIAL_URL,
        api_key=SecretStr(API_KEY),
        api_version=""
    ).invoke(messages)
    messages.append(ai_message)

    print(f"\n🤖Response: \n{ai_message.content}\n {'='*100}\n\n")

    return messages
