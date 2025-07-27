'''
문제 5-10 (중/하)
설명: 삼항 연산자와 조건부 표현식을 사용하는 예제를 작성하세요.
출력결과:
점수: 85, 결과: 합격
나이: 17, 상태: 미성년자
숫자들의 최대값: 42
양수들: [5, 12, 8, 23]
'''

score = int(input("점수를 입력하세요: "))
score_result = "합격" if score >= 80 else "불합격"

age = int(input("나이를 입력하세요: "))
age_result = "성인" if age >= 20 else "미성년자"

print(f"점수: {score}, 결과: {score_result}")
print(f"나이: {age}, 상태: {age_result}")

num_list = [5, 12, 8, 23, 42, -1, -12, -4, -34, -29]
max_num = max(num_list)
print(f"숫자들의 최대값: {max_num}")

plus_num = [num for num in num_list if num > 0 and num != max_num]
print(f"양수들: {plus_num}")