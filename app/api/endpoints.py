from fastapi import APIRouter
from app.models.schemas import OOTDRequest, OOTDResponse

router = APIRouter()

@router.post("/recommend", response_model=OOTDResponse, summary="OOTD 추천 받기")
async def get_ootd_recommendation(request: OOTDRequest):
    """
    사용자의 상황(텍스트)을 입력받아 상황에 맞는 추천 OOTD 스타일 텍스트, 참조 이미지 URL, 링크를 반환합니다.
    (현재 MVP 버전에서는 Mock 데이터를 반환합니다)
    """
    query = request.query
    
    if "바다" in query or "휴가" in query:
        recommendation_text = "바다와 잘 어울리는 화이트 리넨 셔츠에 시원한 네이비 반바지를 매치해보세요. 포인트로 라탄햇을 더하면 완벽한 휴양지 룩이 완성됩니다!"
        pinterest_image_url = "https://i.pinimg.com/736x/52/7c/18/527c18a0f88639f98c15d4ded59108d3.jpg"  # 임시 Mock URL
        pinterest_deep_link = "https://pin.it/93SaraDyk"
    elif "데이트" in query or "소개팅" in query:
        recommendation_text = "깔끔한 인상을 주는 베이지 슬랙스와 파스텔 톤 셔츠를 추천합니다. 단정하면서도 따뜻한 느낌을 줄 수 있어요."
        pinterest_image_url = "https://i.pinimg.com/736x/mock_date_outfit.jpg" # 임시 Mock URL
        pinterest_deep_link = "pinterest://search/pins/?q=mens%20date%20outfit"
    else:
        recommendation_text = "오늘은 편안하면서도 스타일리시한 미니멀 캐주얼 룩 어떨까요? 오버핏 티셔츠와 와이드 데님 팬츠 조합에 스니커즈를 추천드려요."
        pinterest_image_url = "https://i.pinimg.com/736x/mock_casual_outfit.jpg" # 임시 Mock URL
        pinterest_deep_link = "pinterest://search/pins/?q=mens%20casual%20outfit"

    return OOTDResponse(
        recommendation_text=recommendation_text,
        pinterest_image_url=pinterest_image_url,
        pinterest_deep_link=pinterest_deep_link
    )
