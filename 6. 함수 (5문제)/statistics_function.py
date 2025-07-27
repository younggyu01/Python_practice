'''
문제 6-4 (중/하)
설명: 리스트의 통계 정보(평균, 최댓값, 최솟값, 표준편차)를 반환하는 함수를 작성하세요.
출력결과:
숫자들: [10, 20, 30, 40, 50]
평균: 30.0
최댓값: 50
최솟값: 10
표준편차: 15.81
'''
import numpy as np

num_list = [10, 20, 30, 40, 50]

def stat(num):
    print(f"숫자들: {num}")
    print(f"평균: {np.mean(num)}")
    print(f"최댓값: {max(num)}")
    print(f"최솟값: {min(num)}")
    print(f"표준편차: {np.std(num):.2f}")

stat(num_list)