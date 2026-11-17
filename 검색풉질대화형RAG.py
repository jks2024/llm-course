# 검색 품질을 높이고, 후속 질문을 처리하고, 개선 효과를 숫자로 확인하는 방법을 다룸

# indexing.py — 문서가 바뀔 때만 실행
# pip install langchain-community langchain-text-splitters langchain-openai langchain-chroma pypdf python-dotenv
import hashlib
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

docs = PyPDFDirectoryLoader("./docs").load()          # docs 폴더의 모든 PDF
splits = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)

def make_id(doc):
    key = f"{doc.metadata['source']}|{doc.metadata.get('page')}|{doc.page_content}"
    return hashlib.md5(key.encode()).hexdigest()

unique = {make_id(d): d for d in splits}             # 동일 청크 중복 제거

vectorstore = Chroma(
    collection_name="lecture",
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory="./chroma_db",                 # 디스크에 저장
)
vectorstore.add_documents(list(unique.values()), ids=list(unique.keys()))  # 같은 ID는 덮어씀
print(f"{len(unique)}개 청크 저장 완료")