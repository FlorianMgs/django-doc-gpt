import os
from chroma_db import ChromaDB
from django_doc_chatbot import DjangoDocChatBot


def main():
    if not os.path.exists(ChromaDB.CHROMA_DB_DIRECTORY):
        print("Chroma DB does not exist. Creating it...")
        ChromaDB()

    chatbot = DjangoDocChatBot()
    query = input("Ask DjangoDocChatbot > ")
    result = chatbot.answer(query)
    print(result["answer"])
    print(result["sources"])


if __name__ == "__main__":
    main()
