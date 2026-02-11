# 점수 입력받기
score = int(input("점수를 입력하세요: "))

# 학점 판별 로직
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# 결과 출력
print(f"점수 {score}점의 학점은 {grade}입니다.")