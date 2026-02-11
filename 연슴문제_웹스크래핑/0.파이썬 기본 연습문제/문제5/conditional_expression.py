# 1. 점수 합격/불합격
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

# 2. 나이 상태
age = 17
status = "성인" if age >= 20 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 3. 최대값 (max 함수 없이 삼항 연산자 중첩 - 예시용)
# 실제로는 max()가 더 pythonic함
a, b = 42, 24
max_val = a if a > b else b
print(f"숫자들의 최대값: {max_val}")

# 4. 리스트 컴프리헨션 내의 조건부 표현식 (필터링이 아님)
# 양수면 그대로, 음수면 0으로 바꾸는 예시
nums = [5, -3, 12, 8, -1, 23]
positives = [n for n in nums if n > 0] # 필터링 (if가 뒤에)
print(f"양수들: {positives}")