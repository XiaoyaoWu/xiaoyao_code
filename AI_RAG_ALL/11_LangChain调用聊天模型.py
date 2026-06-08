
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model = ChatTongyi(model="qwen-max")

messages = [
    SystemMessage(content="你是一名来自边塞的诗人"),
    HumanMessage(content="帮我写首边塞诗"),
    AIMessage(content="大漠孤烟直，长河落日圆"),
    HumanMessage(content="基于你写的再来一首")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content, end="" ,flush=True)


