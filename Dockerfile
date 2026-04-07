# 사용할 베이스 이미지 (가볍고 보안이 뛰어난 python:3.11-slim 사용)
FROM python:3.11-slim

# 보안: root 대신 애플리케이션을 실행할 non-root 사용자 생성
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /usr/src/app

# 환경 변수 설정 (파이썬 바이트코드 생성 방지, 로그 버퍼링 비활성화)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 보안 및 용량 최적화: 시스템 패키지 업데이트, 빌드 필수 패키지 설치 후 캐시 삭제
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 파이썬 패키지 설치 (캐시 미사용으로 이미지 용량 절감)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . .

# 소스 코드 파일의 소유권을 새로 생성한 appuser로 변경
RUN chown -R appuser:appuser /usr/src/app

# 이후 명령어는 appuser 권한으로 실행
USER appuser

# 외부로 노출할 포트
EXPOSE 8000

# 컨테이너 실행 명령어
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
