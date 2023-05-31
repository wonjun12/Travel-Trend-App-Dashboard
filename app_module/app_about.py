import streamlit as st
import pandas as pd

def run_about_func(df):
    st.image('image/about_main.png')
    st.header('이번 여행 트렌드는 어디일까?')
    st.text('2019년 ~ 2023년 까지의 데이터를 기준으로 가장 많이 검색된 지역과 검색어를 알아보자!')
    st.text('')
    st.text('')
    st.subheader('참고 데이터')
    st.dataframe(df)
    st.write('데이터 다운로드 : https://www.bigdata-culture.kr/bigdata/user/main.do')
    