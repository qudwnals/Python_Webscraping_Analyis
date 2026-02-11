numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. 모든 수의 제곱 (map)
# map(함수, 리스트) -> 결과를 리스트로 변환
squared = list(map(lambda x: x**2, numbers))

# 2. 5보다 큰 수들 (filter)
# filter(함수, 리스트) -> 조건이 참인 것만 남김
filtered = list(filter(lambda x: x > 5, numbers))

# 3. 5보다 큰 수들의 제곱 (filter 후 map)
filtered_squared = list(map(lambda x: x**2, filter(lambda x: x > 5, numbers)))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared}")
print(f"5보다 큰 수들: {filtered}")
print(f"5보다 큰 수들의 제곱: {filtered_squared}")