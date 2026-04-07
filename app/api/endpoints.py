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
        pinterest_image_url = "https://i.pinimg.com/736x/c6/bd/42/c6bd425c7f0fa89f8fda74e73f2ec948.jpg" # 임시 Mock URL
        pinterest_deep_link = "https://kr.pinterest.com/pin/21603273207766637/"

    elif "출근" in query or "오피스" in query:
        recommendation_text = "격식과 편안함을 동시에 잡은 비즈니스 캐주얼은 어떨까요? 셔츠 위에 가벼운 네이비 블레이저를 걸치고 슬림핏 슬랙스를 매치해 전문적인 느낌을 연출해보세요."
        pinterest_image_url = "https://i.pinimg.com/736x/55/d1/95/55d1958be6f3e90af649f0e0fd3b6976.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/3307399721232346/"

    elif "결혼식" in query or "하객" in query:
        recommendation_text = "주인공보다 튀지 않으면서도 세련된 하객 룩이 핵심입니다. 차분한 그레이 톤의 셋업 수트나, 깔끔한 니트에 슬랙스를 조합해 정중한 무드를 완성하세요."
        pinterest_image_url = "https://i.pinimg.com/1200x/ed/db/7f/eddb7f8e6e105d069d2696bd0deb804b.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/5207355815770315/"

    elif "운동" in query or "짐웨어" in query:
        recommendation_text = "기능성과 스타일을 모두 챙긴 고프코어 룩을 추천합니다. 흡습속건 티셔츠에 조거 팬츠를 매치하고, 가벼운 바람막이로 스포티한 감성을 더해보세요."
        pinterest_image_url = "https://i.pinimg.com/736x/83/a7/a0/83a7a0b248952729f6ec2b98768aafc7.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/6896205672846308/"

    elif "캠핑" in query or "아웃도어" in query:
        recommendation_text = "활동성이 중요한 캠핑에는 레이어드가 정답입니다. 넉넉한 포켓이 달린 카고 팬츠에 후드티를 입고, 보온을 위한 베스트(조끼)를 더해 실용적인 워크웨어 룩을 연출하세요."
        pinterest_image_url = "https://i.pinimg.com/736x/camping_look_mock.jpg"
        pinterest_deep_link = "https://pin.it/camping_link"

    elif "카페" in query or "성수" in query:
        recommendation_text = "요즘 트렌드인 '꾸안꾸(꾸민 듯 안 꾸민 듯)' 스타일이 딱입니다. 빈티지한 그래픽 티셔츠에 생지 데님을 매치하고, 볼캡으로 힙한 포인트를 살려보세요."
        pinterest_image_url = "https://i.pinimg.com/736x/41/2b/06/412b065e1488cf0c08613c854aeee971.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/100908847899029541/"

    elif "비" in query or "장마" in query:
        recommendation_text = "비 오는 날에는 젖어도 금방 마르는 소재가 최고죠. 나일론 팬츠에 짧은 기장의 레인코트를 매치하고, 기능성 샌들이나 레인부츠로 발을 보호하세요."
        pinterest_image_url = "https://i.pinimg.com/736x/41/76/b5/4176b5feabc0f47b21a26ba85c5d525c.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/10485011627315659/"

    elif "면접" in query or "인터뷰" in query:
        recommendation_text = "신뢰감을 주는 화이트 셔츠와 다크 차콜 컬러의 수트를 추천합니다. 타이는 너무 화려하지 않은 사선 패턴이나 솔리드 컬러로 진중함을 표현해보세요."
        pinterest_image_url = "https://i.pinimg.com/736x/40/a7/93/40a793d07736c533191c93c2a4d72583.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/1548181186348024/"

    elif "축제" in query or "페스티벌" in query:
        recommendation_text = "자유로운 에너지가 느껴지는 락시크 룩은 어떨까요? 레더 자켓이나 체크 셔츠를 허리에 두르고, 선글라스를 더해 강렬한 존재감을 드러내보세요."
        pinterest_image_url = "https://i.pinimg.com/1200x/2e/88/0b/2e880bdce7a5308d0a7471b13ca7c687.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/33565959718570377/"

    elif "전시회" in query or "미술관" in query:
        recommendation_text = "지적인 분위기의 모노톤 코디를 추천합니다. 검정색 터틀넥에 롱 코트를 걸치고 안경을 매치해 차분하면서도 감각적인 룩을 완성하세요."
        pinterest_image_url = "https://i.pinimg.com/736x/b4/52/b1/b452b1ba78bdf6e3d13699fd4eee8f28.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/960603795534694801/"

    elif "한강" in query or "산책" in query:
        recommendation_text = "편안함이 1순위인 스트릿 캐주얼 룩입니다. 화이트 스웨트 셔츠에 미니스커트를 매치하고, 니삭스와 스니커즈로 포인트를 주면 경쾌한 무드가 살아납니다. 여기에 볼캡 하나만 툭 써주면 산책길 인생샷 준비 끝!"
        pinterest_image_url = "https://i.pinimg.com/1200x/44/44/19/444419ec7eba32e9181621123180d006.jpg"
        pinterest_deep_link = "https://kr.pinterest.com/pin/339669996907948231/"
    else:
        recommendation_text = "오늘은 편안하면서도 스타일리시한 미니멀 캐주얼 룩 어떨까요? 오버핏 티셔츠와 와이드 데님 팬츠 조합에 스니커즈를 추천드려요."
        pinterest_image_url = "https://i.pinimg.com/736x/1d/95/1a/1d951affe259f37ad09500f7b64c0a40.jpg" # 임시 Mock URL
        pinterest_deep_link = "https://kr.pinterest.com/pin/4362930883870022/"

    return OOTDResponse(
        recommendation_text=recommendation_text,
        pinterest_image_url=pinterest_image_url,
        pinterest_deep_link=pinterest_deep_link
    )
