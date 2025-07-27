'''
문제 4-1 (하)
설명: 점수를 입력받아 학점을 출력하는 프로그램을 작성하세요. (90이상:A, 80이상:B, 70이상:C, 60이상:D, 미만:F)
출력결과:
점수를 입력하세요: 85
점수 85점의 학점은 B입니다.
'''

grade = int(input("점수를 입력하세요: "))

if grade >= 90:
    print(f"점수 {grade}의 학점은 A입니다.")
elif 90 > grade >= 80:
    print(f"점수 {grade}의 학점은 B입니다.")
elif 80 > grade >= 70:
    print(f"점수 {grade}의 학점은 C입니다.")
elif 70 > grade >= 60:
    print(f"점수 {grade}의 학점은 D입니다.")
else:
    print(f"점수 {grade}의 학점은 F입니다.")