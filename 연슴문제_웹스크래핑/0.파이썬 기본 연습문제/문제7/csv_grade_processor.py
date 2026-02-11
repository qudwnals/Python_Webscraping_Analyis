import csv

filename = "grades.csv"

# 1. CSV 파일 생성 (데이터 저장)
data = [
    ['이름', '점수'],  # 헤더
    ['김철수', 85],
    ['이영희', 92],
    ['박민수', 78],
    ['최수진', 95]
]

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"학생 성적이 {filename}에 저장되었습니다.\n")

# 2. CSV 파일 읽기 및 분석
print("성적 분석 결과:")
total_score = 0
count = 0

with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # 첫 번째 줄(헤더: 이름, 점수) 건너뛰기
    
    for row in reader:
        name = row[0]
        score = int(row[1])  # 문자열로 읽히므로 정수로 변환
        print(f"{name}: {score}점")
        
        total_score += score
        count += 1

# 평균 계산
average = total_score / count
print(f"전체 평균: {average:.1f}점")