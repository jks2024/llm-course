from common import client, MODEL

stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "RAG의 동작을 네 단계로 설명해줘"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices:
        text = chunk.choices[0].delta.content
        if text:
            print(text, end="", flush=True)
print()