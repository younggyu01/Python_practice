'''
문제 2-5 (중/하)
설명: 문자열을 입력받아 특정 문자가 몇 번 나타나는지 세는 프로그램을 작성하세요.
출력결과:
문자열을 입력하세요: programming
찾을 문자를 입력하세요: m
문자 'm'이 2번 나타납니다.
'''

word = input("문자열을 입력하세요: ")
find_word = input("찾을 문자를 입력하세요: ")
counter = word.count(find_word)
print(f"문자 '{find_word}'이 {counter}번 나타납니다.")