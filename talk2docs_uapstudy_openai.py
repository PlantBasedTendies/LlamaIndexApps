
'''
Overview:

    A LLamaIndex implementation for interacting with PDF documents via LLM queries

    In this early stage python script we leverage OpenAI, LlamaIndex, and a PDF
    file containing a study of UAP to ask questions about this otherwordly topic.
    Several questions are pre-populated. An OpenAI key is necessary for this
    version of the script.

    Date: 10/26/2023

    Examples:

    Q: What is the subject of this report?
    A: The subject of this report is "UNIDENTIFIED ANOMALOUS PHENOMENA."

    Q: Are UAP of extraterrestrial origin?
    A: To date, there is no conclusive evidence suggesting that UAPs have
       an extraterrestrial origin. The scientific literature does not provide
       any definitive conclusions about the provenance of these anomalous
       sightings. While it is possible to hypothesize about the existence of
       faraway extraterrestrial civilizations and their detectable technologies,
       the search for extraterrestrial life is considered the hypothesis of last
       resort, only to be considered after ruling out all other possibilities.
       The focus should be on collecting data and conducting rigorous scientific
       investigations to understand UAPs.
    
    Q: What organizations operate the NEXRAD Doppler radar network?
    A: The NEXRAD Doppler radar network is jointly operated by the FAA
       (Federal Aviation Administration), U.S. Air Force, and National
       Weather Service.




'''
from dotenv import load_dotenv
import os
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader
# from IPython.display import Markdown, display # Add later for notebook implementation

documents = SimpleDirectoryReader("uapstudy_data").load_data() # PDF file resides in /uapstudy_data/
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# response = query_engine.query("What is the subject of this report?")
response = query_engine.query("Are UAP of extraterrestrial origin?")
# response = query_engine.query("What organizations operate the NEXRAD Doppler radar network?")

print(response)