# 학생 정보 (이름, 점수) 튜플 리스트
students = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

print(f"학생 정보: {students}")

# 1. 이름순 정렬 (튜플의 0번째 요소 기준)
sorted_by_name = sorted(students, key=lambda x: x[0])
print(f"이름순 정렬: {sorted_by_name}")

# 2. 점수순 정렬 (튜플의 1번째 요소 기준)
sorted_by_score = sorted(students, key=lambda x: x[1])
print(f"점수순 정렬: {sorted_by_score}")

# 3. 점수 내림차순 정렬 (reverse=True 추가)
sorted_by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"점수 내림차순: {sorted_by_score_desc}")