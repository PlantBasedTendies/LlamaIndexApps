# LlamaIndexApps
LlamaIndexApps is a repo to store experiments conducted with LlamaIndex's integrated RAG framework.

--------
## :telescope: **streamlit_hawking_openai.py**
This script builds upon talk2docs_hawking_openai.py by adding a Streamlit UI which enables the end-user to
ask questions about Stephen Hawking with natural language answers produced via LlamaIndex. Screenshot:
![Screenshot of Streamlit Integration](https://github.com/PlantBasedTendies/LlamaIndexApps/assets/86295293/9e9099e1-fb30-40e9-8420-d3ab1ebb3e23)


--------
## :telescope: **talk2docs_hawking_openai.py**
This script loads a text file containing information about Stephen Hawking's life, located in /hawking_text/, and
allows the end-user to ask questions about the astrophysicist.

--------

## :flying_saucer: **talk2docs_uapstudy_openai.py**
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
* streamlit

:gear: To run the python script, you will need to populate **default.env** with your OpenAI API key and rename it to **.env**
