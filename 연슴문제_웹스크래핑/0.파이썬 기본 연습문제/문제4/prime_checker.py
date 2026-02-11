num = int(input("숫자를 입력하세요: "))

is_prime = True  # 소수라고 가정하고 시작 (Flag 변수)

if num < 2:
    is_prime = False  # 1보다 작은 수는 소수가 아님
else:
    # 2부터 자기 자신보다 1 작은 수까지 반복
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # 나누어 떨어지면 소수가 아님
            break  # 더 이상 검사할 필요 없음

# 결과 출력
if is_prime:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")