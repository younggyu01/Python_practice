'''
문제 3-9 (중/하)
설명: 두 개의 리스트를 병합하고 공통 요소를 찾는 프로그램을 작성하세요.
출력결과:
리스트1: [1, 2, 3, 4, 5]
리스트2: [4, 5, 6, 7, 8]
병합된 리스트: [1, 2, 3, 4, 5, 6, 7, 8]
공통 요소: [4, 5]
'''

first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7, 8]

print(f"리스트1: {first_list}")
print(f"리스트2: {second_list}")

merge_list = list(set(first_list + second_list))
print(f"병합된 리스트: {merge_list}")

dup_list = [x for x in first_list if x in second_list]
print(f"공통 요소: {dup_list}")