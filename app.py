import streamlit as st
from deep_translator import GoogleTranslator

# 페이지 기본 설정
st.set_page_config(page_title="다국어 번역기", page_icon="🌐", layout="wide")

st.title("🌐 한국어 다국어 번역기")
st.markdown("한국어를 입력하면 **영어, 중국어(간체), 일본어**로 동시 번역됩니다.")

# 사용자 입력 받기
text_to_translate = st.text_area("번역할 한국어 문장을 입력하세요:", height=150)

if st.button("번역하기", type="primary"):
    if text_to_translate.strip():
        with st.spinner("번역 중... 잠시만 기다려주세요."):
            try:
                # 번역기 초기화 및 번역 수행
                en_text = GoogleTranslator(source='ko', target='en').translate(text_to_translate)
                zh_text = GoogleTranslator(source='ko', target='zh-CN').translate(text_to_translate)
                ja_text = GoogleTranslator(source='ko', target='ja').translate(text_to_translate)
                
                st.success("번역이 완료되었습니다!")
                
                # 결과를 3개의 열(Column)로 나누어 깔끔하게 표시
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.subheader("🇺🇸 영어")
                    st.info(en_text)
                    
                with col2:
                    st.subheader("🇨🇳 중국어(간체)")
                    st.info(zh_text)
                    
                with col3:
                    st.subheader("🇯🇵 일본어")
                    st.info(ja_text)
                    
            except Exception as e:
                st.error(f"번역 중 오류가 발생했습니다. 다시 시도해주세요.\n에러 내용: {e}")
    else:
        st.warning("번역할 텍스트를 먼저 입력해주세요.")
