# 기존 방식 (비추천 코드 생략 - 문제 설명에 포함됨)

text = "Python is awesome programming language"

# Pythonic 방식 (추천)
# 1. 공백을 기준으로 분리
words = text.split()

# 2. 하이픈으로 연결
hyphenated = "-".join(words)

# 3. 대문자로 변환 후 공백으로 연결
# (리스트 컴프리헨션 없이 map이나 upper() 사용 가능하지만,
# 가장 직관적인 방법은 join 전에 리스트 요소를 처리하는 것입니다.)
upper_joined = " ".join([word.upper() for word in words])

print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {hyphenated}")
print(f"대문자로 변환 후 공백으로 연결: {upper_joined}")