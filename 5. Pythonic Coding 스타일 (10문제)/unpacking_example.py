'''
문제 5-8 (중/하)
설명: 언패킹과 *args, **kwargs를 사용하는 예제를 작성하세요.
출력결과:
좌표: x=10, y=20
리스트 언패킹: a=1, b=2, c=3
가변 인수의 합: 60
키워드 인수들: name=김철수, age=25, city=서울
'''

def func(*args):
    x,y = args
    print(f"좌표: x={x}, y={y}")

func(10,20)


list1 = [1,2,3]
a,b,c = list1
print(f"리스트 언패킹: a={a}, b={b}, c={c}")


def sum_ar(*args):
    print(f"가변 인수의 합: {sum(args)}")

sum_ar(10,20,30)

def info(**kwargs):
    keward = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    print(f"키워드 인수들: {keward}")

info(name="김철수", age=25, city="서울")