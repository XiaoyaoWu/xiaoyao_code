from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "邻居姓{firstname},生了个{gender}，帮我取个名字，简单回答"
)
model = Tongyi(model = "qwen-max")
# prompt_text = prompt_template.format(firstname = "张", gender = "女儿" )
#
# model = Tongyi(model = "qwen-max")
# res = model.invoke(input = prompt_text)
# print(res)

chain = prompt_template | model
res = chain.invoke(input={"firstname":"张", "gender":"女儿"})
print(res)
