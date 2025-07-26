# app.py

import streamlit as st
from modules.dart_tool import run_dart_app
from modules.summary_tool import run_summary_app
from modules.csv_analysis_tool import run_csv_analysis_app

st.set_page_config(page_title="회계 분석 툴", layout="wide")
st.title("💼 회계법인 포트폴리오용 분석 앱")

menu = st.sidebar.radio("메뉴 선택", ["📊 DART 조회기", "📄 문서 요약기", "📈 CSV 분석기"])

if menu == "📊 DART 조회기":
    run_dart_app()
elif menu == "📄 문서 요약기":
    run_summary_app()
elif menu == "📈 CSV 분석기":
    run_csv_analysis_app()