
price = int(input("상품 가격을 입력하세요: "))
discount_rate = int(input("할인율을 입력하세요(%): "))

# 할인 금액 계산 (가격 * 할인율 / 100)
discount_amount = int(price * (discount_rate / 100))


final_price = price - discount_amount

# 결과 출력
print(f"원래 가격: {price}원")
print(f"할인율: {discount_rate}%")
print(f"할인 금액: {discount_amount}원")
print(f"최종 가격: {final_price}원")