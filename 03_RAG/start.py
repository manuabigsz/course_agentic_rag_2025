import os
from openai import OpenAI
from IPython.display import Markdown, display


api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key
)

model = "GPT-5-mini"

system_prompt = "You are Kendrick Lamar"
system_prompt2 = "You are Taylor Swift"

user_prompt = "write a diss song about Drake with 2 verses and a chorus"

# response = client.chat.completions.create(
#     model=model,
#     messages=[
#         {"role": "system", "content": system_prompt2},
#         {"role": "user", "content": user_prompt}
#     ]
# )

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt2},
        {"role": "user", "content": user_prompt}
    ]
)


display(Markdown(response.choices[0].message.content))