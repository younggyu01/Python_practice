'''
문제 7-2 (중/하)
설명: CSV 형태의 학생 성적 데이터를 파일에 저장하고 읽어서 평균을 계산하는 프로그램을 작성하세요.
출력결과:
학생 성적이 grades.csv에 저장되었습니다.

성적 분석 결과:
김철수: 85점
이영희: 92점  
박민수: 78점
최수진: 95점
전체 평균: 87.5점
'''
import pandas as pd

student = ["김철수", "이영희", "박민수", "최수진"]
score = [85, 92, 78, 95]

df = pd.DataFrame(student, columns= ["학생"])
df['성적'] = score

df.to_csv("grades.csv", index=False)
print(f"학생 성적이 grades.csv에 저장되었습니다.\n")

data = pd.read_csv("grades.csv")

print(f"성적 분석 결과:")

for i in range(len(data)):
    print(f"{data['학생'][i]}: {data['성적'][i]}점")

print(f"전체 평균: {data['성적'].mean()}")