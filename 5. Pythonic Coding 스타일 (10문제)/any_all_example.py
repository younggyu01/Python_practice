'''
문제 5-6 (중/하)
설명: any와 all 함수를 사용하여 조건을 검사하는 프로그램을 작성하세요.
출력결과:
숫자 리스트: [2, 4, 6, 8, 10]
모든 수가 짝수인가? True
하나라도 10보다 큰 수가 있는가? False

숫자 리스트2: [1, 3, 5, 7, 12]
모든 수가 짝수인가? False
하나라도 10보다 큰 수가 있는가? True
'''

num_list1 = [2, 4, 6, 8, 10]
num_list2 = [1, 3, 5, 7, 12]

def any_all(n_list):
    if all(num % 2 == 0 for num in n_list):
        print("모든 수가 짝수인가? True")
    else:
        print("모든 수가 짝수인가? False")

    if any(10 < num for num in n_list):
        print("하나라도 10보다 큰 수가 있는가? True")
    else:
        print("하나라도 10보다 큰 수가 있는가? False")

print(f"숫자 리스트 : {num_list1}")
any_all(num_list1)

print(f"숫자 리스트 : {num_list2}")
any_all(num_list2)