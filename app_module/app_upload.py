import streamlit as st
import pandas as pd
from datetime import date

def run_upload_csv():
    st.header('현재 없는 데이터를 추가하실수 있습니다.')
    data1, data2 = st.tabs(['해외여행 데이터', '국내여행 데이터'])
    with data1:
        st.write('해외 데이터 : https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=2ed02b20-1e55-11eb-a4e6-a9a03a61580b')
    with data2:
        st.write('국내 데이터 : https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=25c89d50-1e55-11eb-a4e6-a9a03a61580b')
    
    st.text('\n')
    st.subheader('데이터 추가하기')
    upload_data = st.file_uploader('추가할 데이터를 넣으세요!', type=['csv'])

    if upload_data is not None:
        st.subheader('원본 데이터 확인')
        df = pd.read_csv(upload_data)
        st.dataframe(df)
        
        try:
            df.drop(['SEQ_NO', 'UPPER_CTGRY_NM'], axis=1, inplace=True)
            if df['LWPRT_CTGRY_NM'].unique() == '해외여행':
                df.drop(['CNTT_NM'], axis=1, inplace=True)
                df.rename(columns={'COUNTRY_NM' : 'AREA_NM'}, inplace=True)
            
            df['SCCNT_DE'] = df['SCCNT_DE'].map(lambda x : date(x//10000, x%10000//100, x%100))

            st.success('가공된 데이터 확인')
            st.dataframe(df)

            if st.button('데이터 추가 하기'):
                travel_df = pd.read_csv('travel_data/travel_data.csv')
                
                if str(df['SCCNT_DE'][0]) in travel_df.loc[travel_df['LWPRT_CTGRY_NM'] == df['LWPRT_CTGRY_NM'][0], 'SCCNT_DE'].unique():
                    st.error('해당 날짜 데이터가 이미 존재합니다!')
                else :
                    save_df = pd.concat([travel_df, df.iloc[:10, ]], ignore_index=True)
                    save_df.to_csv('travel_data/travel_data.csv', index=False, encoding='utf-8-sig')
                    st.success('데이터 저장 완료!')

        except:
            st.error('정상적인 데이터가 아닙니다! 링크된 데이터를 넣어주세요!')
        
