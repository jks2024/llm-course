from common import client, MODEL

normal = "철수가 사과 5개를 3000원에 사고, 그중 2개를 친구에게 줬다. 남은 사과는 개당 얼마짜리인가?"
cot = normal + " 정답과 확인 가능한 계산식만 간단히 제시해줘."

for name, prompt in [("기본", normal), ("CoT", cot)]:
    res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    print(f"[{name}]", res.choices[0].message.content, "\n")