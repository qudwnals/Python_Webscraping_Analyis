# 파일명 정의
filename = "my_text_file.txt"

# 1. 파일에 쓰기 (Write)
content = """안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다"""

print("파일에 저장할 내용:")
print(content)

with open(filename, 'w', encoding='utf-8') as file:
    file.write(content)

print("\n" + "="*20 + "\n")

# 2. 파일에서 읽기 (Read)
print("파일에서 읽어온 내용:")
with open(filename, 'r', encoding='utf-8') as file:
    read_content = file.read()
    print(read_content)