
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model = ChatTongyi(model="qwen-max")

messages = [
    ("system","你是一名来自边塞的诗人"),
    ("human","帮我写首边塞诗"),
    ("ai","大漠孤烟直，长河落日圆"),
    ("human","基于你写的再来一首"),
]

for chunk in model.stream(input = messages):
    print(chunk.content, end="" , flush=True)


