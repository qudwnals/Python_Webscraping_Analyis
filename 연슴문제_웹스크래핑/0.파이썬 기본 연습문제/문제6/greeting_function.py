# 기본값 매개변수 설정 (greeting 기본값: "안녕하세요")
def greet(name, greeting="안녕하세요", suffix=""):
    # 이름 뒤에 '님'을 붙일지 여부는 인사말에 따라 조금 다르게 처리 (출력 예시 맞춤)
    if "Hello" in greeting:
        print(f"{greeting}, {name}!")
    else:
        # suffix가 있으면 뒤에 붙임
        end_msg = f" {suffix}" if suffix else ""
        print(f"{greeting}, {name}님!{end_msg}")

# 1. 기본값 사용 (김철수)
greet("김철수")

# 2. 매개변수 지정 (John, Hello)
greet("John", greeting="Hello")

# 3. 추가 메시지 포함 (이영희)
greet("이영희", suffix="좋은 하루 되세요!")