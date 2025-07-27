'''
문제 7-3 (중/하)
설명: 텍스트 파일의 단어 빈도를 계산하는 프로그램을 작성하세요.
출력결과:
단어 빈도 분석 결과:
파이썬: 3번
프로그래밍: 2번  
언어: 2번
배우기: 1번
쉬운: 1번
강력한: 1번
'''
from collections import Counter

word_list = ["파이썬", "파이썬", "파이썬", "프로그래밍", "프로그래밍", "언어", "언어", "배우기", "쉬운", "강력한"]

save_file = '7-3.txt'
with open(save_file, "w", encoding="utf-8") as file:
    file.write(' '.join(word_list))

with open("7-3.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

count_word = Counter(words)

print("단어 빈도 분석 결과:")
for word,count in count_word.items():
    print(f"{word}: {count}번")