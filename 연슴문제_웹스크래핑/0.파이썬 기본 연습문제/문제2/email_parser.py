
email = input("이메일 주소를 입력하세요: ")

# @ 기준으로 분리 (리스트로 반환됨)
# 예: ['user', 'example.com']
parts = email.split('@')


print(f"사용자명: {parts[0]}")
print(f"도메인: {parts[1]}")