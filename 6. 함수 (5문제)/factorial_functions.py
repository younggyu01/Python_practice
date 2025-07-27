'''
문제 6-2 (중/하)
설명: 팩토리얼을 계산하는 재귀함수와 반복문을 사용한 함수를 각각 작성하세요.
출력결과:
5! (재귀) = 120
5! (반복) = 120
7! (재귀) = 5040
7! (반복) = 5040
'''

def pact(n):
    if n == 0 or n == 1:
        return 1
    return n * pact(n-1)

def is_pact(n):
    plus_num = 1
    for i in range(1,n+1):
        plus_num *= i
    return plus_num

print(f"5! (재귀) = {pact(5)}")
print(f"5! (반복) = {is_pact(5)}")
print(f"7! (재귀) = {pact(7)}")
print(f"7! (반복) = {is_pact(7)}")  