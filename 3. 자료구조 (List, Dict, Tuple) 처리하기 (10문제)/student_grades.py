'''
문제 3-3 (중/하)
설명: 학생들의 성적을 딕셔너리로 저장하고 평균 점수를 계산하는 프로그램을 작성하세요.
출력결과:
학생 성적:
김철수: 85점
이영희: 92점
박민수: 78점
최수진: 95점
평균 점수: 87.5점
'''

student_grade = {}

while True:
    student_name = input("학생 이름 : ")
    if student_name == '끝':
        break
    student_score = int(input(f"{student_name}의 점수: "))
    student_grade[student_name] = student_score

print("학생 성적:")
for student_name, student_score in student_grade.items():
    print(f"{student_name}: {student_score}점")

score_mean = sum(student_grade.values()) / len(student_grade)
print(f"평균 점수: {score_mean}점")