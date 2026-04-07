document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("ootd-form");
    const input = document.getElementById("query-input");
    const loading = document.getElementById("loading");
    const resultContainer = document.getElementById("result-container");
    const resultImage = document.getElementById("result-image");
    const resultPinterestLink = document.getElementById("result-pinterest-link");
    const resultText = document.getElementById("result-text");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const query = input.value.trim();
        if(!query) return;

        // UI 상태 초기화: 결과창 숨기고 로딩 표시
        resultContainer.classList.add("hidden");
        loading.classList.remove("hidden");

        try {
            // 현재 구동중인 서버의 주소 기준으로 API 요청
            const response = await fetch('/api/v1/ootd/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query: query })
            });

            if(!response.ok) {
                throw new Error('API request failed');
            }

            const data = await response.json();
            
            // 데이터 바인딩
            resultImage.src = data.pinterest_image_url;
            // 핀터레스트 앱 스키마나 웹 링크 처리
            resultPinterestLink.href = data.pinterest_deep_link;
            resultText.textContent = data.recommendation_text;

            // 이미지가 로드된 후 화면에 부드럽게 표시하기 위해 load 이벤트 대기 (옵션)
            resultImage.onload = () => {
                loading.classList.add("hidden");
                resultContainer.classList.remove("hidden");
                
                // 검색 후 스크롤을 결과창으로 살짝 부드럽게 이동
                resultContainer.scrollIntoView({ behavior: 'smooth', block: 'end' });
            };

            // 만약 이미지 로드 실패 시 강제로 보여주기
            resultImage.onerror = () => {
                resultImage.src = "https://via.placeholder.com/600x800?text=No+Mock+Image+Found";
                loading.classList.add("hidden");
                resultContainer.classList.remove("hidden");
            };

        } catch (error) {
            console.error("추천 데이터를 가져오는 중 오류가 발생했습니다:", error);
            alert("서버 연결에 실패했습니다. API가 켜져 있는지 확인해주세요.");
            loading.classList.add("hidden");
        }
    });
});
