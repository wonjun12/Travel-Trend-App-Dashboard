import streamlit as st
import pandas as pd
from datetime import date

import numpy as np
def run_upload_csv():
    st.header('현재 없는 데이터를 추가하실수 있습니다.')
    data1, data2 = st.tabs(['해외여행 데이터', '국내여행 데이터'])
    with data1:
        st.write('해외 데이터 : https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=2ed02b20-1e55-11eb-a4e6-a9a03a61580b')
    with data2:
        st.write('국내 데이터 : https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=25c89d50-1e55-11eb-a4e6-a9a03a61580b')
    
    st.text('\n')
    st.subheader('데이터 추가하기')
    upload_data = st.file_uploader('추가할 데이터를 넣으세요!', type=['csv'], accept_multiple_files=True)
    if len(upload_data) != 0:
        df = pd.DataFrame()
        travel_df = pd.read_csv('travel_data/travel_data.csv')
        for i in range(len(upload_data)):
            st.subheader(f'{i+1}번째 원본 데이터 확인')
            df_read = pd.read_csv(upload_data[i])
            st.dataframe(df_read)
            
            try:
                df_read.drop(['SEQ_NO', 'UPPER_CTGRY_NM'], axis=1, inplace=True)
                if df_read['LWPRT_CTGRY_NM'].unique() == '해외여행':
                    df_read.drop(['CNTT_NM'], axis=1, inplace=True)
                    df_read.rename(columns={'COUNTRY_NM' : 'AREA_NM'}, inplace=True)
                
                df_read['SCCNT_DE'] = df_read['SCCNT_DE'].map(lambda x : date(x//10000, x%10000//100, x%100))

                st.success(f'{i+1}번째 가공된 데이터 확인')
                st.dataframe(df_read)
 
                if str(df_read['SCCNT_DE'][0]) in travel_df.loc[travel_df['LWPRT_CTGRY_NM'] == df_read['LWPRT_CTGRY_NM'][0], 'SCCNT_DE'].unique():
                    st.error('해당 날짜 데이터가 이미 존재합니다!')
                else :
                    if len(df.index) != 0 and df_read['SCCNT_DE'][0] in df.loc[df['LWPRT_CTGRY_NM'] == df_read['LWPRT_CTGRY_NM'][0], 'SCCNT_DE'].unique():
                        st.error('해당 날짜 데이터가 이미 존재합니다!')
                    else:
                        df = pd.concat([df, df_read.iloc[:10, ]], ignore_index=True)
                        st.info('추가할 수 있는 데이터입니다!')        
            except:
                st.error('정상적인 데이터가 아닙니다! 링크된 데이터를 넣어주세요!')

        if st.button('데이터 추가 하기'):
            save_df = pd.concat([travel_df, df], ignore_index=True)
            st.dataframe(save_df)
            save_df.to_csv('travel_data/travel_data.csv', index=False, encoding='utf-8-sig')
            st.success('데이터 저장 완료!')
        
