# math_operations.py

def circle_area(radius):
    """원의 넓이 계산 (반지름 * 반지름 * 3.14159)"""
    return radius * radius * 3.14159

def rectangle_area(width, height):
    """직사각형 넓이 계산"""
    return width * height

def factorial(n):
    """팩토리얼 계산"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
    """최대공약수 계산 (유클리드 호제법)"""
    while b > 0:
        a, b = b, a % b
    return a