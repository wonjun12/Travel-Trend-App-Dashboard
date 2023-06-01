import streamlit as st
import pandas as pd

from datetime import date
import joblib
import plotly.express as px

def run_ml_func():
    st.header('검색 트렌드 예측')
    data = joblib.load('model/travel.pkl')

    select_list = ['선택','국내여행 예측', '해외여행 예측']
    selected_key = st.selectbox('예측하고 싶으신 종류를 선택하세요!', select_list)

    if selected_key != select_list[0]:
        df = pd.DataFrame(columns=['지역', '검색량'])
        travel_data = data[selected_key]
        start_date = st.date_input('시작일', min_value=date(2023,5,28), max_value=date(2026, 5, 27))
        start_date = pd.to_datetime(start_date)
        end_date = st.date_input('마지막일', min_value=date(2023,5,28), max_value=date(2026, 5, 27))
        end_date = pd.to_datetime(end_date)

        if start_date <= end_date:
            if st.button('검색 순위 예측 하기'):
                for region, shrch in travel_data.items():
                    yhat = int(shrch.loc[(shrch['ds'] >= start_date) & (shrch['ds'] <= end_date), 'yhat'].sum())
                    if yhat > 0:
                        df.loc[len(df.index)] = [region, yhat]
                
                df = df.sort_values('검색량', ascending=False)
                with st.expander('데이터 프레임 결과 보기'):
                    st.dataframe(df)
                
                #default_view = st.slider('최대 순위 결과 설정', min_value=2, max_value=df.shape[0], value=10)

                fig_bar = px.bar(
                    df,
                    y = '검색량',
                    x = '지역',
                    text_auto='.2s',
                    title='검색 트랜드 순위 예측'
                )
                st.plotly_chart(fig_bar)

                fig_pie = px.pie(df,values='검색량',names=df['지역'])
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig_pie)

                
                    
        else :
            st.error('시작일이 마지막일 보다 높을 수 없습니다!')
    