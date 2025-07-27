'''
문제 8-1 (중/하)
설명: 수학 연산을 위한 모듈을 만들고 이를 사용하는 메인 프로그램을 작성하세요.
'''

pi = 3.14159

def circle(r):
    return f"{pi*r**2:.2f}"

def area(x,y):
    return x*y

def pact(n):
    if n == 0 or n == 1:
        return 1
    return n * pact(n-1)

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)