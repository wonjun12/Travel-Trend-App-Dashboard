
import streamlit as st

import plotly.express as px
import pandas as pd

from datetime import timedelta
def date_range(start, end ,df):
    dates = pd.date_range(start, end, freq='D')
    #print(df[0])
    #print(set(dates) & set(df))
    #dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    #print(df)
    
    # for date in df:
    #     print(date)
    
    return dates

def run_travel_func(df,start_date, end_date):
    st.info(f'검색 일자 : {start_date.date()} ~ {end_date.date()}')

    df_sarch = df.loc[(df['SCCNT_DE'] <= end_date) & (df['SCCNT_DE'] >= start_date), ]

    if df_sarch.index.shape[0] != 0:
        st.subheader('기본 검색 순위 확인하기')
        date_range(start_date, end_date, df_sarch['SCCNT_DE'].unique())
        
        with st.expander('없는 데이터 날짜'):
            st.text('날짜')

        sharch_list = ['전체 검색 순위', 'PC 검색 순위', '모바일 검색 순위']
        select_sharch = st.selectbox('보고 싶은 기준을 선택하세요!', sharch_list)
        sharch_dic = {
            sharch_list[0] : 'SCCNT_SM_VALUE',
            sharch_list[1] : 'PC_SCCNT_VALUE',
            sharch_list[2] : 'MOBILE_SCCNT_VALUE',
        }
        # 날짜 범위 지정
        
        # 검색어 많은 순서대로 정렬
        group_sccnt = df_sarch.groupby('AREA_NM')[sharch_dic[select_sharch]].sum().sort_values(ascending=False).iloc[:10, ]
        # 기본적인 검색량 보이기 그래프
        fig = px.pie(group_sccnt,values=sharch_dic[select_sharch],names=group_sccnt.keys(), title=select_sharch)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)

        st.subheader('여행지 검색어 확인하기')
        selected_resions = st.multiselect('보고 싶은 나라를 선택하세요!', group_sccnt.keys())

        for resion in selected_resions:
            resion_loc = df_sarch.loc[df_sarch['AREA_NM'] == resion, ['SRCHWRD_NM']].value_counts()
            fig = px.pie(resion_loc,values=resion_loc.values,names=resion_loc.keys().get_level_values(0), title=f"{resion}의 검색")
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig)

        
        

    else:
        st.subheader('해당 날짜에 데이터가 없습니다!')
        st.error('다른 날짜를 선택해서 확인 해주세요!')
    
