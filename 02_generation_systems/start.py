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

human_message = "Explain time to me"
system_message = "You are a 4th grande science teatcher"

messages = [
    SystemMessage(content = system_message),
    HumanMessage(content=human_message)
]

print(f"messages: {messages}")

ai_message = chat_model.invoke(messages)
display(Markdown(ai_message))

#text generation with parameters

llm = HuggingFaceEndpoint(
    repo_id = repo_id,
    task = "generated_text",
    temperature=1.2,
    max_new_tokens=512,
    cache = False)
chat_model2=ChatHuggingFace(llm=llm)


ai_message = chat_model2.invoke(messages)
display(Markdown(ai_message))