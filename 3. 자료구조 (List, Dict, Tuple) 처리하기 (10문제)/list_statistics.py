'''
문제 3-1 (하)
설명: 5개의 숫자를 리스트에 저장하고 합계와 평균을 구하는 프로그램을 작성하세요.
출력결과:
숫자들: [10, 20, 30, 40, 50]
합계: 150
평균: 30.0
'''
# 공백으로 구분
numbers = list(map(int,input("입력 : ").split()))
print(f"숫자들: {numbers}")
result_sum = sum(numbers)
result_mean = (result_sum/len(numbers))
print(f"합계: {result_sum}")
print(f"평균: {result_mean}")