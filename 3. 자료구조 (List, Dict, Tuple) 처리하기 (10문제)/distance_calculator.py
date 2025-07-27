'''
문제 3-4 (중/하)
설명: 좌표를 튜플로 저장하고 두 점 사이의 거리를 계산하는 프로그램을 작성하세요.
출력결과:
점1: (0, 0)
점2: (3, 4)
두 점 사이의 거리: 5.0
'''

import math

# x,y 형태로 입력
point1 = eval(input("점1: "))
point2 = eval(input("점2: "))

x1, y1 = point1
x2, y2 = point2

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'두 점 사이의 거리: {dist}')