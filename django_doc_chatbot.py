from dotenv import load_dotenv

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI


load_dotenv()


class DjangoDocChatBot:
    CHROMA_DB_DIRECTORY = "chroma_db/ask_django_docs"

    def answer(self, query):
        embeddings = OpenAIEmbeddings()
        db = Chroma(
            collection_name="ask_django_docs",
            persist_directory=self.CHROMA_DB_DIRECTORY,
            embedding_function=embeddings,
        )

        chat = ChatOpenAI(temperature=0)

        chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=chat,
            chain_type="stuff",
            retriever=db.as_retriever(),
        )

        result = chain({"question": query}, return_only_outputs=True)
        return result
