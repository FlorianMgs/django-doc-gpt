from dotenv import load_dotenv

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from django_doc_scraper import DjangoDocScraper


load_dotenv()


class ChromaDB:
    CHROMA_DB_DIRECTORY = "chroma_db/ask_django_docs"

    def __init__(self) -> None:
        self.urls = DjangoDocScraper().urls()
        self.load()

    def load(self):
        loader = WebBaseLoader(self.urls)
        documents = loader.load()

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        splitted_documents = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()

        db = Chroma.from_documents(
            splitted_documents,
            embedding=embeddings,
            collection_name="ask_django_docs",
            persist_directory=self.CHROMA_DB_DIRECTORY,
        )
        db.persist()
