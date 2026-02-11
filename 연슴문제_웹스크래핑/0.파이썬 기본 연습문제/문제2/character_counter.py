
text = input("문자열을 입력하세요: ")
target_char = input("찾을 문자를 입력하세요: ")

# 해당 문자의 개수 세기
count = text.count(target_char)

# 결과 출력
print(f"문자 '{target_char}'이 {count}번 나타납니다.")