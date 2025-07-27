'''
문제 7-5 (중/하)
설명: 로그 파일을 생성하고 특정 레벨의 로그만 필터링하여 출력하는 프로그램을 작성하세요.
출력결과:
로그 파일이 생성되었습니다.

ERROR 레벨 로그들:
2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패
2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음

WARNING 레벨 로그들:  
2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다
2025-07-20 12:00:00 - WARNING - 디스크 공간 부족
'''

import logging

log_file = "log.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("시스템이 정상 작동 중입니다.")
logging.warning("메모리 사용량이 높습니다.")
logging.error("데이터베이스 연결 실패.")
logging.warning("디스크 공간 부족.")
logging.error("파일을 찾을 수 없음.")

print("로그 파일이 생성되었습니다.\n")

with open(log_file, "r", encoding="cp949") as f:
    logs = f.readlines()

print("ERROR 레벨 로그들:")
for log in logs:
    if "ERROR" in log:
        print(log.strip())

print("\nWARNING 레벨 로그들:")
for log in logs:
    if "WARNING" in log:
        print(log.strip())