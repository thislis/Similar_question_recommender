import os

from dotenv import load_dotenv

# dotenv를 로드해요.
# .env파일에는 우리가 설정한 데이터베이스 주소가 있어요.
# TODO : 원래는 .env를 .gitignore에 추가하고 .env.template을 놓아요.
load_dotenv()


class Config:
    DATABASE_URI = os.getenv("DATABASE_URI")

config = Config()