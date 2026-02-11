import math

def calculate_stats(numbers):
    # 1. 평균
    mean = sum(numbers) / len(numbers)
    
    # 2. 최댓값, 최솟값
    max_val = max(numbers)
    min_val = min(numbers)
    
    # 3. 표준편차 (Standard Deviation)
    # 분산 = (데이터 - 평균)^2의 합 / (데이터 개수 - 1)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    std_dev = math.sqrt(variance)
    
    return mean, max_val, min_val, std_dev

data = [10, 20, 30, 40, 50]
mean, max_v, min_v, std = calculate_stats(data)

print(f"숫자들: {data}")
print(f"평균: {mean}")
print(f"최댓값: {max_v}")
print(f"최솟값: {min_v}")
print(f"표준편차: {std:.2f}")