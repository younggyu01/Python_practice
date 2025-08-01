'''
문제 5-5 (중/하)
설명: 딕셔너리 컴프리헨션을 사용하여 숫자와 그 제곱값의 딕셔너리를 만드는 프로그램을 작성하세요.
출력결과:
1부터 5까지의 제곱 딕셔너리: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
짝수만의 제곱 딕셔너리: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
'''

comp_dic = {key:key*key for key in range(1, 6)}
print(f"1부터 5까지의 제곱 딕셔너리: {comp_dic}")

even_dic = {key:key*key for key in range(2, 11, 2)}
print(f"짝수만의 제곱 딕셔너리: {even_dic}")