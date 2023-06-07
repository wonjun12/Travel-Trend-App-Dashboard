import streamlit as st
import pandas as pd

def run_about_func(df):
    st.image('image/about_main.png')
    st.header('이전 여행 트렌드는 어디일까?')
    st.text('2019년 ~ 2023년 까지의 데이터를 기준으로 가장 많이 검색된 지역과 검색어를 알아보자!')
    st.text('이전 데이터를 통해서 미래의 검색 트렌드에 대해 예측해보자!')
    st.text('')
    st.subheader('사용 데이터')
    st.dataframe(df)
    st.write('해외 데이터 다운로드 : https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=2ed02b20-1e55-11eb-a4e6-a9a03a61580b')
    st.write('국내 데이터 다운로드 : https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=25c89d50-1e55-11eb-a4e6-a9a03a61580b')
    