# Django Doc GPT
This is a local GPT-powered chatbot that uses Django documentation. Ask him anything related to Django!  
This uses Lanchain alongside with ChromaDB to store the embeddings.  
Embeddings are created using `text-embedding-ada-002` OpenAI model.

## Setup
- Clone the repo, create your venv, install the dependencies:  
```
git clone https://github.com/FlorianMgs/django-doc-gpt.git 
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Create a `.env` file, define your OpenAI API key:  
```
OPENAI_API_KEY=<your openai api key>
```
- Launch the script  
```
python main.py
```