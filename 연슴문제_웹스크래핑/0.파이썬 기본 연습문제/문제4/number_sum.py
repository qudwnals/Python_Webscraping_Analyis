total = 0

while True:
    # 숫자 입력받기
    num = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))
    
    # 0이면 반복문 종료
    if num == 0:
        break
    
    # 입력된 숫자를 합계에 더하기
    total += num

# 결과 출력
print(f"입력된 숫자들의 합: {total}")