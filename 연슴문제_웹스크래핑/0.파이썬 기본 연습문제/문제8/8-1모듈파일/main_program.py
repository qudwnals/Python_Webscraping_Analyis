# main_program.py
import math_operations as mo  # 모듈을 불러오면서 'mo'라는 별명 붙이기

# 1. 원의 넓이
radius = 5
print(f"원의 넓이: {mo.circle_area(radius):.2f}")

# 2. 직사각형 넓이
print(f"직사각형 넓이: {mo.rectangle_area(10, 5)}")

# 3. 팩토리얼
print(f"팩토리얼 5! = {mo.factorial(5)}")

# 4. 최대공약수
print(f"최대공약수(48, 18) = {mo.gcd(48, 18)}")