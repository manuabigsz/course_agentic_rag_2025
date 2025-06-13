import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import (HumanMessage, SystemMessage)
from IPython.display import Markdown, display

hf_key = os.getenv('HF_TOKEN')


repo_id = "microsoft/Phi-4" 
#repo_id2 = "google/gemma-3-27b-it"
llm = HuggingFaceEndpoint(repo_id=repo_id,
                          task = "generated_text",
                          )

chat_model = ChatHuggingFace(llm=llm)

ai_message = chat_model.invoke("what is the capital of france?")

display(Markdown(ai_message.content))