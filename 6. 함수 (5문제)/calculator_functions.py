'''
문제 6-1 (하)
설명: 두 수를 받아서 사칙연산을 수행하는 함수들을 작성하는 프로그램을 만드세요.
출력결과:
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
'''

def calcurator(num1,num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} + {num2} = {num1 - num2}")
    print(f"{num1} + {num2} = {num1 * num2}")
    print(f"{num1} + {num2} = {num1 / num2}")

calcurator(10,5)