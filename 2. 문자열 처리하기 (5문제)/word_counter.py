'''
문제 2-4 (중/하)
설명: 문장을 입력받아 공백을 제거하고, 단어의 개수를 세는 프로그램을 작성하세요.
출력결과:
문장을 입력하세요:   Python is   great   
공백 제거: Python is great
단어 개수: 3개
'''

word = input("문장을 입력하세요: ")
clean_word = ' '.join(word.strip().split())
print(f"공백 제거: {clean_word}")
count = len(clean_word.split())
print(f"단어 개수: {count}")