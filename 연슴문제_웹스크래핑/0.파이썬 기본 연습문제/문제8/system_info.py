import os
import sys

# 1. 현재 작업 디렉토리 (CWD)
print(f"현재 작업 디렉토리: {os.getcwd()}")

# 2. Python 버전 정보
# 버전 정보가 길어서 줄바꿈 없이 출력하기 위해 replace 사용
print(f"Python 버전: {sys.version.split()[0]}") 

# 3. 운영체제 (nt: 윈도우, posix: 맥/리눅스)
print(f"운영체제: {os.name}")

# 4. 환경 변수 PATH (너무 길어서 앞부분 50자만 출력)
path_env = os.environ.get('PATH', 'PATH 없음')
print(f"환경 변수 PATH 일부: {path_env[:50]}...")

# 5. 파일 경로 정보 다루기
sample_path = "/Users/username/documents/report.txt"
# 윈도우라면: "C:\\Users\\username\\documents\\report.txt"

directory, filename_with_ext = os.path.split(sample_path)
filename, extension = os.path.splitext(filename_with_ext)

print("파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename_with_ext}")
print(f"- 확장자: {extension}")

# 6. 파일 존재 여부 확인
print(f"파일 존재 여부: {os.path.exists(sample_path)}")