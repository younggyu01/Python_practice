'''
문제 8-1 (중/하)
설명: 수학 연산을 위한 모듈을 만들고 이를 사용하는 메인 프로그램을 작성하세요.
출력결과:
원의 넓이: 78.54
직사각형 넓이: 50
팩토리얼 5! = 120
최대공약수(48, 18) = 6
'''
import math_operations

print(f"원의 넓이: {math_operations.circle(5)}")
print(f"직사각형의 넓이: {math_operations.area(5,10)}")
print(f"팩토리얼 5! = {math_operations.pact(5)}")
print(f"최대공약수(48, 18) = {math_operations.gcd(48,18)}")