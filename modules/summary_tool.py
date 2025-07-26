# modules/summary_tool.py

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("digit82/kobart-summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("digit82/kobart-summarization")
    return tokenizer, model

def run_summary_app():
    st.subheader("📄 문서 요약기 (KoBART 기반)")
    st.markdown("텍스트를 붙여넣거나 파일을 업로드하면 3줄 요약을 생성합니다.")

    uploaded_file = st.file_uploader("📂 텍스트 파일 업로드 (.txt)", type="txt")
    manual_text = st.text_area("또는 직접 문서 입력:", height=300)

    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
    else:
        text = manual_text

    if st.button("요약하기"):
        if not text.strip():
            st.warning("문서를 입력하거나 업로드해주세요.")
            return

        tokenizer, model = load_model()
        inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=128, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        st.success("✅ 요약 결과:")
        st.write(summary)