'''
문제 3-7 (중/하)
설명: 단어들이 담긴 리스트에서 가장 긴 단어와 가장 짧은 단어를 찾는 프로그램을 작성하세요.
출력결과:
단어 목록: ['cat', 'elephant', 'dog', 'butterfly', 'ant']
가장 긴 단어: butterfly (9글자)
가장 짧은 단어: cat (3글자)
'''

word_list = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
print(f"단어 목록: {word_list}")

count_word = list(map(len, word_list))

max_word = max(word_list, key=len)
min_word = min(word_list, key=len)

print(f"가장 긴 단어: {max_word} ({max(count_word)}글자)")
print(f"가장 짧은 단어: {min_word} ({min(count_word)}글자)")