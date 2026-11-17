import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(".env에 OPENAI_API_KEY를 설정하세요.")

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
client = OpenAI(timeout=30.0, max_retries=2)