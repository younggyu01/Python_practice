'''
문제 4-2 (중/하)
설명: 1부터 100까지의 숫자 중에서 3의 배수의 합을 구하는 프로그램을 작성하세요.
출력결과:
1부터 100까지 3의 배수: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
3의 배수의 합: 1683
3의 배수의 개수: 33개
'''
number_list = []

for i in range(1,101):
    number_list.append(i)

three_list = [num for num in number_list if num % 3 == 0]
print(f"1부터 100까지 3의 배수: {three_list}")

print(f"3의 배수의 합: {sum(three_list)}")
print(f"3의 배수의 개수: {len(three_list)}개")