filename = "words.txt"
text_data = "파이썬 프로그래밍 언어 파이썬 배우기 쉬운 강력한 언어 프로그래밍 파이썬"

# 1. 파일 생성
with open(filename, 'w', encoding='utf-8') as f:
    f.write(text_data)

# 2. 파일 읽기 및 빈도 계산
word_counts = {}

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()
    words = content.split()  # 공백 기준으로 단어 분리
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# 3. 결과 출력
print("단어 빈도 분석 결과:")
# 빈도수가 높은 순서대로 정렬 (내림차순)
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count}번")