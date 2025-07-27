'''
문제 5-1 (중/하)
설명: 문자열을 단어별로 분리했다가 다시 합치는 코드를 split과 join을 사용하여 작성하세요.
출력결과:
원본 문자열: Python is awesome programming language
분리된 단어들: ['Python', 'is', 'awesome', 'programming', 'language']
하이픈으로 연결: Python-is-awesome-programming-language
대문자로 변환 후 공백으로 연결: PYTHON IS AWESOME PROGRAMMING LANGUAGE
'''

word = input("원본 문자열: ")

split_word = word.split(" ")
print(f"분리된 단어들 : {split_word}")

hypen_word = "-".join(split_word)
print(f"하이픈으로 연결: {hypen_word}")

print((hypen_word.upper()).replace("-"," "))
