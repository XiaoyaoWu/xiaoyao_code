from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一名边塞诗人"),
        MessagesPlaceholder("history"),
        ("human","再来一首"),
    ]
)
messages_data = [
    ("human","来一首边塞诗"),
    ("ai","大漠孤烟直，长河落日圆"),
    ("human","来一首边塞诗"),
    ("ai","黄沙百战穿金甲，不破楼兰终不还")
]

model = ChatTongyi(model= "qwen3-max")

chain = chat_prompt_template | model

# resp = chain.invoke({"history":messages_data})
# print(resp.content)

resp = chain.stream({"history":messages_data})
for chunk in resp:
    print(chunk.content,end="",flush=True)




