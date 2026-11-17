from openai import OpenAI
from dotenv import load_dotenv
import numpy as np
# OpenAI의 임베딩 모델을 사용하여 여러 문장을 숫자 벡터로 변환하는 예제
# 텍스트 임베딩은 문장의 의미와 특징을 숫자 벡터로 표현하는 기술. 의미가 비슷한 문장은 벡터 공간에서도 비슷한 위치에 나타나는 경향

load_dotenv()
client = OpenAI() # OPENAI_API_KEY 환경변수 자동 사용

def get_embedding(text):
    res = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(res.data[0].embedding)

texts = [
    "오늘 날씨가 많이 더워요",
    "기온이 높아서 더위가 심해요",
    "주식 시장이 오늘 크게 반등했습니다"
]

embeddings = [get_embedding(t) for t in texts]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("문장1 vs 문장2:", cosine_similarity(embeddings[0], embeddings[1]))
print("문장1 vs 문장3:", cosine_similarity(embeddings[0], embeddings[2]))