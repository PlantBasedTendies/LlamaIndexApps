
'''
Overview:

    In this local Streamlit app we leverage OpenAI, LlamaIndex, and a text
    file containing a history of Stephen Hawking to ask questions about one of
    the world's greatest astrophysicists.

    **Note: An OpenAI key is necessary for this version of the script.**

    Date: 1/05/2024

'''
from dotenv import load_dotenv
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os
import streamlit as st

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app layout
st.title("Stephen Hawking Q&A :telescope: ")

intro = '''**Examples:**  
        :pill: :orange[What illness did Stephen Hawking develop?]  
        :bald_man: :green[What was Stephen Hawking's father's name?]  
        :boom: :blue[What kind of work helped Stephen Hawking prove the idea of the 'Big Bang'?]
        '''
st.markdown(intro)

user_input = st.text_input("Ask a question about Stephen Hawking:")

# LlamaIndex integrated RAG
# text file resides in /hawking_data/
documents = SimpleDirectoryReader("hawking_data").load_data() 

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

# Check for input and produce output
if user_input:
    response = query_engine.query(user_input)
    response_string = str(response)

    # Display the output
    st.write(response_string)