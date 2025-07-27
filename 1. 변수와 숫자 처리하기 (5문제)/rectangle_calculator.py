'''
문제 1-4 (중/하)
설명: 직사각형의 가로와 세로 길이를 입력받아 넓이와 둘레를 계산하는 프로그램을 작성하세요.
출력결과:
가로 길이를 입력하세요: 8
세로 길이를 입력하세요: 5
직사각형의 넓이: 40
직사각형의 둘레: 26
'''

width = float(input("가로 길이를 입력하세요: "))
height = float(input("세로 길이를 입력하세요: "))
area = width*height
cir = 2 * (width+height)
print(f"직사각형의 넓이: {area}")
print(f"직사각형의 둘레: {cir}")