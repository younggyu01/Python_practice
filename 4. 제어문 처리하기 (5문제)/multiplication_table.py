'''
문제 4-3 (중/하)
설명: 구구단을 출력하는 프로그램을 작성하세요. 사용자가 입력한 단만 출력하세요.
출력결과:
몇 단을 출력할까요? 7
7단 구구단:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
'''

gu = int(input("몇 단을 출력할까요? "))

print(f"{gu}단 구구단:")

for i in range(1,10):
    print(f"{gu} x {i} = {gu*i}")