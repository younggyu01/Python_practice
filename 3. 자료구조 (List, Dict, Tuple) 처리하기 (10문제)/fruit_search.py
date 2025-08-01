'''
문제 3-2 (중/하)
설명: 과일 이름들이 담긴 리스트에서 특정 과일을 검색하는 프로그램을 작성하세요.
출력결과:
과일 목록: ['사과', '바나나', '오렌지', '포도', '딸기']
찾을 과일을 입력하세요: 바나나
'바나나'가 목록에 있습니다!
'''

# 공백으로 구분
fruits = list(input("입력 : ").split())
print(f"과일 목록: {fruits}")

find_fruit = input(f"찾을 과일을 입력하세요: ")

if find_fruit in fruits:
    print(f"{find_fruit}가 목록에 있습니다!")
else:
    print(f"{find_fruit}가 목록에 없습니다...")