'''
문제 2-2 (중/하)
설명: 문자열을 입력받아 대문자로 변환, 소문자로 변환, 길이 출력하는 프로그램을 작성하세요.
출력결과:
문자열을 입력하세요: Hello World
대문자: HELLO WORLD
소문자: hello world
문자열 길이: 11
'''

str1 = input("문자열을 입력하세요: ")
print(f"대문자: {str1.upper()}")
print(f"소문자: {str1.lower()}")
print(f"문자열 길이: {len(str1)}")