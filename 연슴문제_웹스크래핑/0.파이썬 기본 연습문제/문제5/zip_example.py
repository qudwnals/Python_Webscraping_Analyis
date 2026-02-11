students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

print("학생과 점수 매칭:")
# Pythonic 방식 (추천)
for student, score in zip(students, scores):
    print(f"{student}: {score}점")

# 두 리스트를 딕셔너리로 변환
score_dict = dict(zip(students, scores))
print(f"점수별 학생 딕셔너리: {score_dict}")