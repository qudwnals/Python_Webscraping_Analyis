# 과일 리스트 정의
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print(f"과일 목록: {fruits}")

# 찾을 과일 입력받기
search_fruit = input("찾을 과일을 입력하세요: ")

# 검색 및 결과 출력
if search_fruit in fruits:
    print(f"'{search_fruit}'가 목록에 있습니다!")
else:
    print(f"'{search_fruit}'는 목록에 없습니다.")