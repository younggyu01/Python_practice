'''
문제 8-3 (중/하)
설명: os와 sys 모듈을 사용하여 시스템 정보를 출력하고 파일 경로를 다루는 프로그램을 작성하세요.
출력결과:
현재 작업 디렉토리: /Users/username/python_practice
Python 버전: 3.9.7 (default, Oct 13 2021, 06:44:56)
운영체제: posix
환경 변수 PATH 일부: /usr/local/bin:/usr/bin:/bin
파일 경로 정보:
- 디렉토리: /Users/username/documents
- 파일명: report.txt
- 확장자: .txt
파일 존재 여부: False
'''
import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")
print(f"환경 변수 PATH 일부: {os.environ.get('PATH')[:50]}")

file_path = r"C:\Users\82103\Documents\report.txt"
print("파일 경로 정보:")
print(f"- 디렉토리: {os.path.dirname(file_path)}")
print(f"- 파일명: {os.path.basename(file_path)}")
print(f"- 확장자: {os.path.splitext(file_path)[1]}")
print(f"파일 존재 여부: {os.path.exists(file_path)}")