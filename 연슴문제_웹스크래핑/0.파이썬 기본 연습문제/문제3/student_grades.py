# 학생 성적 딕셔너리 정의
scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최수진': 95
}

print("학생 성적:")
# 딕셔너리 순회하며 출력
for name, score in scores.items():
    print(f"{name}: {score}점")

# 평균 점수 계산
average_score = sum(scores.values()) / len(scores)

print(f"평균 점수: {average_score:.1f}점")