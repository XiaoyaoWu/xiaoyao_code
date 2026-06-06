from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen3.7-max",  # 您可以按需更换为其它深度思考模型
    messages= [
        {"role": "system", "content": "你是python专家，说废话的那种"},
        {"role": "assistant", "content": "我是话多的python专家"},
        {"role": "user", "content": "用python输出1-10"}
    ],
    extra_body={"enable_thinking": True},
    stream=True  # 开启了流式输出的功能
)
for chunk in completion:
    if not chunk.choices:
        continue
    print(
        chunk.choices[0].delta.content,
        end="",  # 每一段之间以空格分隔
        flush=True  # 立刻刷新缓冲区
    )