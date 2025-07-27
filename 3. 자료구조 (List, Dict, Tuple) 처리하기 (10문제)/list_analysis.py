'''
문제 3-6 (중/하)
설명: 리스트에서 최댓값, 최솟값, 두 번째로 큰 값을 찾는 프로그램을 작성하세요.
출력결과:
숫자 목록: [15, 3, 27, 8, 19, 12, 31]
최댓값: 31
최솟값: 3
두 번째로 큰 값: 27
'''

# 공백으로 구분
math_str = list(map(int, input("정수들을 입력하세요 : ").split()))
math_list = list(math_str)
print(f"숫자 목록: {math_list}")

list_max = max(math_list)
list_min = min(math_list)

print(f"최댓값: {list_max}")
print(f"최솟값: {list_min}")

math_list2 = sorted(math_list)
list_second_max = math_list2[-2]

print(f"두 번째로 큰 값: {list_second_max}")