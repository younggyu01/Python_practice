'''
문제 3-5 (중/하)
설명: 쇼핑 카트를 딕셔너리로 구현하여 상품을 추가하고 총 가격을 계산하는 프로그램을 작성하세요.
출력결과:
쇼핑 카트:
사과: 2개 (개당 1000원) = 2000원
바나나: 3개 (개당 800원) = 2400원
오렌지: 1개 (개당 1500원) = 1500원
총 가격: 5900원
'''

cart_dict = {
    'apple' : 1000, 
    'banana' : 800, 
    'orange' : 1500
    }

apples = int(input(f"사과 (개당 1000원) : "))
bananas = int(input(f"바나나 (개당 800원) : "))
oranges = int(input(f"오렌지 (개당 1500원) : "))

apples_price = cart_dict['apple'] * apples
bananas_price = cart_dict['banana'] * bananas
oranges_price = cart_dict['orange'] * oranges

total_price = apples_price + bananas_price + oranges_price

print("쇼핑 카트:")
print(f"사과 {apples}개 (개당 1000원) = {apples_price}원")
print(f"바나나: {bananas}개 (개당 800원) = {bananas_price}원")
print(f"오렌지: {oranges}개 (개당 1500원) = {oranges_price}원")
print(f"총 가격: {total_price}원")