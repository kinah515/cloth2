from pydantic import BaseModel, Field

class OOTDRequest(BaseModel):
    query: str = Field(..., description="사용자의 OOTD 고민 (예: '내일 바다 가는데 뭐 입지?')", json_schema_extra={"example": "내일 바다 가는데 뭐 입지?"})

class OOTDResponse(BaseModel):
    recommendation_text: str = Field(..., description="상황에 맞는 추천 스타일 텍스트")
    pinterest_image_url: str = Field(..., description="핀터레스트 모델 사진 이미지 URL")
    pinterest_deep_link: str = Field(..., description="해당 핀터레스트 딥링크")
