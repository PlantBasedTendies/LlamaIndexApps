# LlamaIndex Experimentation
LlamaIndex Experimentation is a repo to store experiments conducted with LlamaIndex's integrated RAG framework.

The **talk2docs_hawking_openai.py** script loads a simple text file about Stephen Hawking, located in /hawking_text/, and
allows the end-user to ask questions about the astrophysicist, such as:

* *What was Stephen Hawking's father's name?* \
* *What illness did Stephen Hawking develop?* \
* *What kind of work helped Stephen Hawking prove the idea of the 'Big Bang'?*

Requirements include:
* llama-index
* openai
* transformers
* accelerate
* python-dotenv
* os

To run the python script, you will need to populate **default.env** with your OpenAI API key and rename it to **.env**
