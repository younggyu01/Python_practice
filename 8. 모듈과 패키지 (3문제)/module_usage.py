'''
문제 8-2 (중/하)
설명: datetime과 random 모듈을 사용하여 임의의 날짜와 숫자를 생성하는 프로그램을 작성하세요.
출력결과:
현재 날짜와 시간: 2025-07-20 14:30:25
포맷된 날짜: 2025년 07월 20일 일요일
임의의 숫자: 7
임의의 실수: 3.14
임의의 리스트 요소: 바나나
섞인 리스트: ['포도', '사과', '오렌지', '바나나', '딸기']
'''
import datetime as dt
import random as rd

today_now = dt.datetime.now()
print(f"현재 날짜와 시간: {today_now.strftime('%Y-%m-%d %H:%M:%S')}")

weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
weekday_name = weekdays[today_now.weekday()]
print(f"포맷된 날짜: {today_now.strftime('%Y년 %m월 %d일')} {weekday_name}")

print(f"임의의 숫자: {rd.randint(0,100)}")

print(f"임의의 실수: {round(rd.uniform(1, 100), 2)}")

fruits = ['사과', '딸기', '바나나', '오렌지', '포도']
print(f"임의의 리스트 요소: {rd.choice(fruits)}")

rd.shuffle(fruits)
print(f"섞인 리스트: {fruits}")