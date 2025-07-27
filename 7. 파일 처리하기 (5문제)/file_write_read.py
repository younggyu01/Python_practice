'''
문제 7-1 (중/하)
설명: 텍스트 파일에 여러 줄의 문자열을 저장하고 읽어오는 프로그램을 작성하세요.
출력결과:
파일에 저장할 내용:
안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다

파일에서 읽어온 내용:
안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다
'''

test_file = "7-1.txt"
with open(test_file, "w", encoding="utf-8") as file:
    t1 = "안녕하세요\n"
    t2 = "파이썬 파일 처리를 연습하고 있습니다\n"
    t3 = "오늘은 좋은 날씨입니다\n"

    print("파일에 저장할 내용:")

    for text in [t1,t2,t3]:
        print(text, end="")
        file.write(text)

test_rd = open("7-1.txt", "r", encoding="utf-8")
print(f"\n파일에서 읽어온 내용: \n{test_rd.read()}")