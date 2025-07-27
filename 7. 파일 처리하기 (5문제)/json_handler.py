'''
문제 7-4 (중/하)
설명: JSON 형태의 데이터를 파일에 저장하고 읽어오는 프로그램을 작성하세요.
출력결과:
데이터가 data.json에 저장되었습니다.

JSON에서 읽어온 데이터:
이름: 김철수
나이: 25
직업: 개발자
취미: ['독서', '영화감상', '코딩']
주소: 서울시 강남구
'''
import json

dic1 = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ['독서', '영화감상', '코딩'],
    "주소": "서울시 강남구"
}

with open('data.json', 'w') as f:
    json.dump(dic1, f, indent=4, ensure_ascii=False)

print("데이터가 data.json에 저장되었습니다.\n")

with open('data.json', 'r') as f:
    info = json.load(f)

print("JSON에서 읽어온 데이터:")
print(f"이름: {info['이름']}")
print(f"나이: {info['나이']}")
print(f"직업: {info['직업']}")
print(f"취미: {info['취미']}")
print(f"주소: {info['주소']}")