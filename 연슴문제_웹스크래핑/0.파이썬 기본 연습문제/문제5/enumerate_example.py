fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print("과일 목록:")

# Pythonic 방식 (추천)
# start=0 은 생략 가능
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")