# modules/dart_tool.py

import streamlit as st
import requests
import pandas as pd
import zipfile
import xml.etree.ElementTree as ET
import os
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
DART_API_KEY = os.getenv("DART_API_KEY")

def get_corp_code(corp_name):
    url = f"https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key={DART_API_KEY}"
    with requests.get(url, stream=True) as r:
        with open("corp_code.zip", 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
    with zipfile.ZipFile("corp_code.zip", 'r') as zip_ref:
        zip_ref.extract("CORPCODE.xml")
    tree = ET.parse("CORPCODE.xml")
    root = tree.getroot()
    for child in root:
        if child.find("corp_name").text == corp_name:
            return child.find("corp_code").text
    return None

def get_financial_statement(corp_code, year="2023"):
    url = f"https://opendart.fss.or.kr/api/fnlttSinglAcnt.json"
    params = {
        "crtfc_key": DART_API_KEY,
        "corp_code": corp_code,
        "bsns_year": year,
        "reprt_code": "11011",
        "fs_div": "CFS"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] != "013": 
        df = pd.DataFrame(data["list"])
        return df[["sj_nm", "account_nm", "thstrm_amount"]]
    else:
        return None

def run_dart_app():
    st.header("📊 DART 재무제표 조회기")

    corp_name = st.text_input("기업명 입력", value="")
    year = st.selectbox("연도 선택", options=["2023", "2022", "2021"])

    if st.button("조회하기"):
        with st.spinner("고유코드 조회 중..."):
            corp_code = get_corp_code(corp_name)
        if corp_code:
            with st.spinner("재무제표 불러오는 중..."):
                df = get_financial_statement(corp_code, year)
            if df is not None:
                st.success("재무제표 불러오기 완료!")
                st.dataframe(df)
            else:
                st.warning("재무제표 데이터를 찾을 수 없습니다.")
        else:
            st.error("해당 기업명을 찾을 수 없습니다.")
