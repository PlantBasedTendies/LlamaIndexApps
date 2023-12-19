# LlamaIndexApps
LlamaIndexApps is a repo to store experiments conducted with LlamaIndex's integrated RAG framework.
\
## :telescope: **talk2docs_hawking_openai.py**:
\
This script loads a simple text file about Stephen Hawking, located in /hawking_text/, and
allows the end-user to ask questions about the astrophysicist, such as:

* ***What was Stephen Hawking's father's name?***
* ***What illness did Stephen Hawking develop?***
* ***What kind of work helped Stephen Hawking prove the idea of the 'Big Bang'?***

--------

## :flying_saucer: **talk2docs_uapstudy_openai.py**:
\
This script loads a PDF file about UAP, located in /uapstudy_data/, and
allows the end-user to ask questions about NASA's report on UAP, such as:

* ***What is the subject of this report?***
* ***Are UAP of extraterrestrial origin?***
* ***What organizations operate the NEXRAD Doppler radar network?***

--------

:wrench: Requirements include:
* llama-index
* openai
* transformers
* accelerate
* python-dotenv
* os
* pypdf

:gear: To run the python script, you will need to populate **default.env** with your OpenAI API key and rename it to **.env**
