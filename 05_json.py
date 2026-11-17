import json
from common import client, MODEL

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "반드시 JSON 객체를 반환하세요."},
        {"role": "user", "content": 'RAG를 설명하고 concept, summary 키를 가진 JSON으로 답하세요.'},
    ],
    response_format={"type": "json_object"},
    temperature=0.2,
    max_completion_tokens=300,
)
choice = response.choices[0]
if choice.finish_reason != "stop":
    raise RuntimeError(f"응답이 정상 완료되지 않았습니다: {choice.finish_reason}")
data = json.loads(choice.message.content or "{}")
if not {"concept", "summary"} <= data.keys():
    raise ValueError("필수 키가 없습니다.")
print(data)