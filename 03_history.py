from common import client, MODEL

messages = [
    {"role": "system", "content": "강의 조교입니다. 간단히 답하세요."},
    {"role": "user", "content": "임베딩을 설명해줘"},
]
first = client.chat.completions.create(model=MODEL, messages=messages)
messages.append({"role": "assistant", "content": first.choices[0].message.content or ""})
messages.append({"role": "user", "content": "방금 설명을 한 문장으로 줄여줘"})
second = client.chat.completions.create(model=MODEL, messages=messages)
print(second.choices[0].message.content)