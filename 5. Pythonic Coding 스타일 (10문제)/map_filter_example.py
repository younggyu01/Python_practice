'''
문제 5-7 (중/하)
설명: map과 filter를 사용하여 리스트를 처리하는 프로그램을 작성하세요.
출력결과:
원본 숫자: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
모든 수의 제곱: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
5보다 큰 수들: [6, 7, 8, 9, 10]
5보다 큰 수들의 제곱: [36, 49, 64, 81, 100]
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 숫자: {numbers}")

even = list(map(lambda x : x*x, numbers))
print(f"모든 수의 제곱: {even}")

five_numbers = list(filter(lambda x : x > 5, numbers))
print(f"5보다 큰 수들: {five_numbers}")

five_even = list(map(lambda x : x*x, five_numbers))
print(f"5보다 큰 수들의 제곱: {five_even}")