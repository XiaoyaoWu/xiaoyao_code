from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen3.7-max",  # 您可以按需更换为其它深度思考模型
    messages= [
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有3只宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有2只宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共多少宠物？"}
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