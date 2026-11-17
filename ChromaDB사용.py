# pip install chromadb

import os          # 환경변수에서 OpenAI API 키 가져오기
import chromadb    # 벡터 데이터베이스 생성 및 관리
from chromadb.utils import embedding_functions  # ChromaDB에서 사용할 임베딩 모델 설정
from common import client, MODEL  # 앞에서 작성한 OpenAI 공통 설정 파일

# OpenAI의 임베딩 모델과 ChromaDB를 연결하여 문서를 벡터로 저장하고, 사용자 질문과 의미적으로 유사한 문서를 검색하는 예제
# 임베딩과 코사인 유사도를 실제 벡터 데이터베이스에 적용하는 과정

# OpenAI 임베딩 모델 설정
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ["OPENAI_API_KEY"],
    model_name="text-embedding-3-small"
)

# ChromaDB 클라이언트 생성
chroma_client = chromadb.Client()

# 컬렉션 생성
collection = chroma_client.get_or_create_collection(
    name="demo",
    embedding_function=openai_ef
)

# 저장할 문서 정의 (추가된 부분)
texts = [
    "오늘 날씨가 많이 더워요",
    "기온이 높아서 더위가 심해요",
    "주식 시장이 오늘 크게 반등했습니다"
]

# 문서 저장
collection.upsert(
    documents=texts,
    ids=["doc1", "doc2", "doc3"]  # 각 문서를 구분하기 위한 고유 ID입니다.
)

# 유사한 문서 검색
results = collection.query(
    query_texts=["오늘 날씨 어때?"],
    n_results=2
)

print(results["documents"])
print(results["distances"])