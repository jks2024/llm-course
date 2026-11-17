import json
from common import client, MODEL

def get_lesson_duration(lesson: str) -> str:
    sample = {"RAG": 120, "프롬프트": 90}
    return json.dumps({
        "lesson": lesson,
        "minutes": sample.get(lesson),
        "is_demo": True,
    }, ensure_ascii=False)

tools = [{
    "type": "function",
    "function": {
        "name": "get_lesson_duration",
        "description": "수업용 가상 강의 시간(분)을 조회합니다.",
        "parameters": {
            "type": "object",
            "properties": {"lesson": {"type": "string"}},
            "required": ["lesson"],
            "additionalProperties": False,
        },
        "strict": True,
    },
}]
messages = [
    {"role": "system", "content": "가상 강의 시간만 안내합니다. 조회한 값을 근거로 답하세요."},
    {"role": "user", "content": "RAG 강의의 실습 시간은 몇 분인가요?"},
]

for step in range(4):
    response = client.chat.completions.create(
        model=MODEL, messages=messages, tools=tools, tool_choice="auto",
    )
    message = response.choices[0].message
    messages.append(message.model_dump(exclude_none=True))
    if not message.tool_calls:
        print(message.content)
        break
    for call in message.tool_calls:
        try:
            if call.function.name != "get_lesson_duration":
                raise ValueError("허용되지 않은 도구")
            args = json.loads(call.function.arguments)
            if set(args) != {"lesson"} or not isinstance(args["lesson"], str):
                raise ValueError("잘못된 인자")
            result = get_lesson_duration(**args)
        except (ValueError, TypeError):
            result = json.dumps({"error": "도구 이름·인자를 확인하세요."}, ensure_ascii=False)
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": result,
        })
else:
    print("반복 한도로 종료했습니다. 최종 답변이 완성된 것은 아닙니다.")