# 출력할 단 입력받기
dan = int(input("몇 단을 출력할까요? "))

print(f"{dan}단 구구단:")

# 1부터 9까지 반복
for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")