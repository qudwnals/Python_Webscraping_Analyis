
sentence = input("문장을 입력하세요: ")

# 공백을 기준으로 단어 분리 (연속된 공백도 자동 처리됨)
words = sentence.split()

cleaned_sentence = ' '.join(words)

# 결과 출력
print(f"공백 제거: {cleaned_sentence}")
print(f"단어 개수: {len(words)}개")