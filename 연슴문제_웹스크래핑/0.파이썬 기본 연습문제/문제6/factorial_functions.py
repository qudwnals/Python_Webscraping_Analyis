# 1. 재귀함수를 이용한 팩토리얼
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# 2. 반복문을 이용한 팩토리얼
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 결과 출력
print(f"5! (재귀) = {factorial_recursive(5)}")
print(f"5! (반복) = {factorial_iterative(5)}")
print(f"7! (재귀) = {factorial_recursive(7)}")
print(f"7! (반복) = {factorial_iterative(7)}")