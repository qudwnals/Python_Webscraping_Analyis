# 쇼핑 카트 딕셔너리 (상품명: [수량, 단가])
cart = {
    '사과': [2, 1000],
    '바나나': [3, 800],
    '오렌지': [1, 1500]
}

print("쇼핑 카트:")
total_price = 0

for item, info in cart.items():
    count = info[0]
    price = info[1]
    item_total = count * price
    
    # 총 가격 누적
    total_price += item_total
    
    print(f"{item}: {count}개 (개당 {price}원) = {item_total}원")

print(f"총 가격: {total_price}원")