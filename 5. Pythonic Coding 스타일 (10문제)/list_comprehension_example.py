'''
문제 5-2 (중/하)
설명: 리스트에서 짝수만 추출하여 제곱하는 코드를 리스트 컴프리헨션으로 작성하세요.
출력결과:
원본 리스트: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
짝수들: [2, 4, 6, 8, 10]
짝수의 제곱: [4, 16, 36, 64, 100]
'''

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 리스트: {num_list}")

second_list = [num for num in num_list if num % 2 == 0]
print(f"짝수들: {second_list}")

second_square = [num*num for num in num_list if num % 2 == 0]
print(f"짝수의 제곱: {second_square}")