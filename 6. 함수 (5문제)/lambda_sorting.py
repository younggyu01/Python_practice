'''
문제 6-5 (중/하)
설명: 람다 함수를 사용하여 리스트를 다양한 방식으로 정렬하는 프로그램을 작성하세요.
출력결과:
학생 정보: [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]
이름순 정렬: [('김철수', 85), ('박민수', 78), ('이영희', 92), ('최수진', 95)]
점수순 정렬: [('박민수', 78), ('김철수', 85), ('이영희', 92), ('최수진', 95)]
점수 내림차순: [('최수진', 95), ('이영희', 92), ('김철수', 85), ('박민수', 78)]
'''

student_info = [
    ('김철수', 85), 
    ('이영희', 92), 
    ('박민수', 78), 
    ('최수진', 95)
]
print(f"학생 정보: {student_info}")

sort_name = sorted(student_info, key = lambda x : x[0])
print(f"이름순 정렬: {sort_name}")

sort_score = sorted(student_info, key = lambda x : x[1])
print(f"점수순 정렬: {sort_score}")

sort_score_down = sorted(student_info, key = lambda x : -x[1])
print(f"점수 내림차순: {sort_score_down}")