import base64
from pathlib import Path
from common import client, MODEL

image = base64.b64encode(Path("./image.png").read_bytes()).decode("ascii")
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "이 도식의 요소를 설명하세요. 보이지 않는 내용은 추측하지 마세요."},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image}"}},
    ]}],
)
print(response.choices[0].message.content)