# modules/csv_analysis_tool.py
import streamlit as st
import pandas as pd

def run_csv_analysis_app():
    st.subheader("📈 CSV 재무제표 분석기")
    uploaded_file = st.file_uploader("📂 CSV 업로드 (예: sample_financials.csv)", type="csv")

    comments = []

    def get_number(val):
        try:
            return float(str(val).replace(",", ""))
        except:
            return None

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        for _, row in df.iterrows():
            name = row['account_nm']
            now = get_number(row['thstrm_amount'])
            prev = get_number(row.get('frmtrm_amount', None))

            if name == "부채비율" and now and now > 200:
                comments.append("부채비율이 200%를 초과하여 재무 위험 가능성이 있습니다.")
            if name == "유동비율" and now and now < 100:
                comments.append("유동비율이 100% 미만으로 유동성에 주의가 필요합니다.")
            if name == "당기순이익":
                if now is not None and now < 0:
                    comments.append("당기순손실이 발생했습니다.")
                if prev is not None and prev > 0 and now < 0:
                    comments.append("전기 대비 적자 전환이 발생했습니다.")

        st.subheader("📝 분석 결과")
        if comments:
            for c in comments:
                st.write("- " + c)
        else:
            st.info("특이사항이 발견되지 않았습니다.")
    else:
        st.info("CSV 파일을 업로드해주세요.")