# DART 재무제표 분석기

이 프로젝트는 공시된 기업 재무제표를 간단하게 조회하고 확인할 수 있도록 만든 웹 도구입니다.  
Python의 Streamlit이라는 웹 프레임워크를 처음 사용해봤고, DART API를 이용해 데이터를 불러오는 연습을 해봤습니다.


# 주요 기능

- 기업명으로 고유 코드 자동 조회 (DART API 활용)
- 연도 선택 후 재무제표 항목 불러오기
- 표 형식으로 보기 쉽게 출력
- Hugging Face 요약 모델을 이용한 문서 요약 기능 포함
- CSV 재무정보 분석 기능도 간단하게 구현


# 실행 방법

1. 필요한 라이브러리 설치
pip install streamlit pandas requests python-dotenv

2. `modules/` 폴더 안에 `.env` 파일을 생성한 뒤 DART_API_KEY 에 실제 API KEY 입력. DART_API_KEY=본인의_API_KEY 

3. streamlit run app.py