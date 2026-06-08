
from langchain_community.llms.tongyi import Tongyi
# from langchain_tongyi import Tongyi
model = Tongyi(model="qwen-max")

# invoke 调用模型，一次性返回完整结果
# stream 调用模型，逐段流式输出
res = model.stream(input = "你是谁能做什么")

for chunk in res:
    print(chunk, end="" , flush=True)



