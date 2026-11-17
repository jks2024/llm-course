import tiktoken
from common import MODEL

try:
    enc = tiktoken.encoding_for_model(MODEL)
except KeyError:
    # 설치된 tiktoken이 모르는 모델명이면 GPT-4o·4.1 계열 인코딩으로 대체
    enc = tiktoken.get_encoding("o200k_base")
for text in ["Hello, how are you?", "안녕하세요, 어떻게 지내세요?"]:
    ids = enc.encode(text)
    print(text, "토큰 수:", len(ids), "토큰 ID:", ids)