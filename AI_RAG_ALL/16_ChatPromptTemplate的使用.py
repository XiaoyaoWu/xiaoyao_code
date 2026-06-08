
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一名边塞诗人"),
        MessagesPlaceholder("history"),
        ("human","再来一首"),
    ]
)

history_data = [
    ("human","写一首诗"),
    ("ai","床前明月光，疑似地上霜"),
    ("human","写一首诗"),
    ("ai","我本将心向明月，奈何明月照沟渠"),
]

prompt_text = chat_prompt_template.invoke({"history":history_data}).to_string()

print(prompt_text)

model = ChatTongyi(model= "qwen3-max")
resp = model.invoke(input=prompt_text)
print(resp.content)
