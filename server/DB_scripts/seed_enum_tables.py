"""
데이터가 데이터베이스에 들어가기 전에 필요한 enum 테이블을 채워주는 스크립트입니다.
"""
import pymysql
from dotenv import load_dotenv
import os
import sys

load_dotenv()

env_variables = {
    "DB_NAME": os.getenv("DATABASE_NAME"),
    "DB_HOST": os.getenv("DATABASE_HOST"),
    "DB_USER": os.getenv("DATABASE_USER"),
    "DB_PASSWORD": os.getenv("DATABASE_PASSWORD"),
}

# Check all required env variables are set.
for key, val in env_variables.items():
    if env_variables[key] is None or env_variables[key] == "None":
        print("Not all required variables are set. Please double check.")
        sys.exit()
    else:
        print(f"{key} variable loaded.")

# db 접속
conn = pymysql.connect(
    host=env_variables["DB_HOST"],
    user=env_variables["DB_USER"],
    password=env_variables["DB_PASSWORD"],
    db=env_variables["DB_NAME"],
    charset="utf8",
)
curs = conn.cursor()

# contentTypes
sql = """insert into content_types (name) values (%s)"""
types = ["Movie", "TV Show"]
for i in range(2):
    curs.execute(sql, (types[i]))

sql = """insert into content_levels (level) values (%s)"""
for i in range(1, 6):
    curs.execute(sql, i)

# db 저장
conn.commit()
# db 접속 해제
conn.close()

print("Seeding Enum Done.")
