from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen3.7-max",  # 您可以按需更换为其它深度思考模型
    messages= [
        {"role": "user", "content": "你是谁"}
    ],
    extra_body={"enable_thinking": True},
    stream=True
)
for chunk in completion:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="", flush=True)