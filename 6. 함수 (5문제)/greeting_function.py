'''
문제 6-3 (중/하)
설명: 기본값 매개변수를 사용하여 인사말을 생성하는 함수를 작성하세요.
출력결과:
안녕하세요, 김철수님!
Hello, John!
안녕하세요, 이영희님! 좋은 하루 되세요!
'''

def hello(name, hi="안녕하세요", msg=""):
    if hi == "안녕하세요":
        kr_name = f"{name}님!"
    else:
        kr_name = f"{name}!"
    
    if msg:
        print(f"{hi}, {kr_name} {msg}")
    else:
        print(f"{hi}, {kr_name}")

hello("김철수")
hello("John", "Hello")
hello("이영희", msg="좋은 하루 되세요!")