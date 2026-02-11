import datetime
import random

# 1. 날짜와 시간 처리
now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 요일 구하기 (0:월, 1:화 ... 6:일)
days = ['월', '화', '수', '목', '금', '토', '일']
day_str = days[now.weekday()]
print(f"포맷된 날짜: {now.strftime('%Y년 %m월 %d일')} {day_str}요일")

# 2. 랜덤 처리
# 1부터 10 사이의 임의의 정수
rand_int = random.randint(1, 10)
print(f"임의의 숫자: {rand_int}")

# 임의의 실수 (소수점 둘째 자리까지)
rand_float = random.uniform(1, 10)
print(f"임의의 실수: {rand_float:.2f}")

# 리스트 요소 선택 및 섞기
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
print(f"임의의 리스트 요소: {random.choice(fruits)}")

random.shuffle(fruits)  # 리스트 순서 섞기 (원본 변경됨)
print(f"섞인 리스트: {fruits}")