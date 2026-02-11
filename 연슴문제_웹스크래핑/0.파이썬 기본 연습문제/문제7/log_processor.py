filename = "app.log"

# 1. 로그 파일 생성
log_content = """2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다
2025-07-20 10:00:00 - INFO - 서버 시작
2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패
2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음
2025-07-20 12:00:00 - WARNING - 디스크 공간 부족
2025-07-20 13:00:00 - INFO - 사용자 로그인"""

with open(filename, 'w', encoding='utf-8') as f:
    f.write(log_content)

print("로그 파일이 생성되었습니다.\n")

# 2. 로그 필터링 함수
def print_logs_by_level(target_level, lines):
    print(f"{target_level} 레벨 로그들:")
    for line in lines:
        if target_level in line:
            print(line.strip()) # 줄바꿈 문자 제거 후 출력
    print() # 줄바꿈

# 3. 파일 읽기 및 출력
with open(filename, 'r', encoding='utf-8') as f:
    log_lines = f.readlines()
    
    # ERROR 레벨 출력
    print_logs_by_level("ERROR", log_lines)
    
    # WARNING 레벨 출력
    print_logs_by_level("WARNING", log_lines)