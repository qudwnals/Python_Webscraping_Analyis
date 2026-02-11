# 1. 튜플 언패킹
point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}")

# 2. 리스트 언패킹
nums = [1, 2, 3]
a, b, c = nums
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# 3. 가변 인수 (*args) 함수
def sum_all(*args):
    return sum(args)

print(f"가변 인수의 합: {sum_all(10, 20, 30)}")

# 4. 키워드 인수 (**kwargs) 함수
def print_info(**kwargs):
    # kwargs는 딕셔너리로 받음
    info_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    print(f"키워드 인수들: {info_str}")

print_info(name="김철수", age=25, city="서울")