import datetime

name = "김철수"
age = 25
pi = 3.14159
price = 1234
percentage = 0.855
today = datetime.date(2025, 7, 20)

print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")           # 소수점 둘째 자리
print(f"가격: {price:,}원")          # 천 단위 콤마
print(f"퍼센트: {percentage:.2%}")   # 백분율 변환
print(f"날짜: {today:%Y년 %m월 %d일}") # 날짜 포맷