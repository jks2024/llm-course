from common import client, MODEL

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "입문자를 돕는 강사입니다. 한국어로 간단히 설명하세요."},
        {"role": "user", "content": "RAG가 필요한 이유를 두 문장으로 설명해줘"},
    ],
)
print(response.choices[0].message.content)
print("종료 사유:", response.choices[0].finish_reason)
if response.usage:
    print("입력:", response.usage.prompt_tokens)
    print("출력:", response.usage.completion_tokens)
    print("전체:", response.usage.total_tokens)