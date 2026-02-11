numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

def check_conditions(nums, name):
    print(f"\n{name}: {nums}")
    # 모든 수가 짝수인지 확인 (generator expression 사용)
    is_all_even = all(n % 2 == 0 for n in nums)
    print(f"모든 수가 짝수인가? {is_all_even}")
    
    # 하나라도 10보다 큰 수가 있는지 확인
    has_gt_10 = any(n > 10 for n in nums)
    print(f"하나라도 10보다 큰 수가 있는가? {has_gt_10}")

check_conditions(numbers1, "숫자 리스트")
check_conditions(numbers2, "숫자 리스트2")