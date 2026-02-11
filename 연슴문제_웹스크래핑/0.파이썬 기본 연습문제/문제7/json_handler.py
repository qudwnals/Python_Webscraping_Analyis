import json

filename = "data.json"

# 1. 데이터 정의 (딕셔너리)
user_data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

# 2. JSON 파일 저장
with open(filename, 'w', encoding='utf-8') as f:
    # indent=4: 들여쓰기를 해서 보기 좋게 저장
    # ensure_ascii=False: 한글을 유니코드 코드가 아닌 글자 그대로 저장
    json.dump(user_data, f, ensure_ascii=False, indent=4)

print(f"데이터가 {filename}에 저장되었습니다.\n")

# 3. JSON 파일 읽기
print("JSON에서 읽어온 데이터:")
with open(filename, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    
    for key, value in loaded_data.items():
        print(f"{key}: {value}")