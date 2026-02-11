# 3의 배수를 저장할 빈 리스트 생성
multiples = []

# 1부터 100까지 반복
for i in range(1, 101):
    if i % 3 == 0:  # 3으로 나누어 떨어지면
        multiples.append(i)

# 합계와 개수 계산
total_sum = sum(multiples)
count = len(multiples)

# 결과 출력
print(f"1부터 100까지 3의 배수: {multiples}")
print(f"3의 배수의 합: {total_sum}")
print(f"3의 배수의 개수: {count}개")