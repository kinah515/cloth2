from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as ootd_router

app = FastAPI(
    title="Fashion AI MVP API",
    description="사용자의 OOTD 고민을 입력받아 스타일, 이미지, 링크를 반환하는 서비스 API",
    version="0.1.0"
)

# CORS 설정 (프론트엔드 연동을 위해 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 허용할 도메인만 지정해야 합니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ootd_router, prefix="/api/v1/ootd", tags=["OOTD"])

@app.get("/")
async def root():
    return {"message": "Welcome to Fashion AI MVP API Server. Please visit /docs for API documentation."}
