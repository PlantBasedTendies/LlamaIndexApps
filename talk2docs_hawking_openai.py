
'''
Overview:

    A LLamaIndex implementation for interacting with text documents via LLM queries

    In this early stage python script we leverage OpenAI, LlamaIndex, and a text
    file containing a history of Stephen Hawking to ask questions about one of
    the world's greatest astrophysicists. Several questions are pre-populated.
    An OpenAI key is necessary for this iteration of the script.

    Date: 10/24/2023

    Examples:
    Q: What illness did Stephen Hawking develop?
    A: Stephen Hawking developed motor neurone disease.

    Q: What was Stephen Hawking's father's name?
    A: Frank

    Q: What kind of work helped Stephen Hawking prove the idea of the 'Big Bang'?
    A: Stephen Hawking's work on black holes helped prove the idea of the 'Big Bang'.

'''
from dotenv import load_dotenv
import os
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader
# from IPython.display import Markdown, display # Add later for notebook implementation

documents = SimpleDirectoryReader("hawking_data").load_data() # text file resides in /hawking_data/
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# response = query_engine.query("What illness did Stephen Hawking develop?")
# response = query_engine.query("What was Stephen Hawking's father's name?")
response = query_engine.query("What kind of work helped Stephen Hawking prove the idea of the 'Big Bang'?")

print(response)