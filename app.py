import streamlit as st
import pandas as pd

from app_module.app_travel import run_travel_func
from app_module.app_about import run_about_func
from app_module.app_upload import run_upload_csv

from dateutil.relativedelta import relativedelta

def main(): 
    st.sidebar.header('이전 여행 검색 트렌드')
    
    st.sidebar.image('image/sidebar.png')

    side_list = ['about', '해외여행', '국내여행', 'Data Upload']
    selected_trand = st.sidebar.selectbox('보고 싶은 트렌드를 선택하세요!', side_list)
    
    if selected_trand != side_list[-1]:
        st.sidebar.image(f'image/{selected_trand}.png')

    df = pd.read_csv('travel_data/travel_data.csv')
    df['SCCNT_DE'] = pd.to_datetime(df['SCCNT_DE'])

    # about
    if selected_trand == side_list[0]:
        run_about_func(df)
    elif selected_trand == side_list[-1]:
        run_upload_csv()
    # 외국, 한국 여행
    else : 
        date_list = ['1개월', '3개월', '6개월', '1년', '사용자 지정']
        selected_date = st.sidebar.selectbox('보고 싶은 날짜를 선택하세요!', date_list)
        
        date_dic = {
            date_list[0] : 1,
            date_list[1] : 3,
            date_list[2] : 6,
            date_list[3] : 12
        }
        end_ = df.loc[df['LWPRT_CTGRY_NM'] == selected_trand, 'SCCNT_DE'].max()
        start_ = end_

        if selected_date == date_list[-1]:
            
            max_date_value = end_
            min_date_value = df.loc[df['LWPRT_CTGRY_NM'] == selected_trand, 'SCCNT_DE'].min()
            
            start_date = st.sidebar.date_input('시작일', 
                                            max_date_value, min_date_value, max_date_value)
            end_date = st.sidebar.date_input('종료일', 
                                            max_date_value, min_date_value, max_date_value)
            if start_date > end_date:
                st.sidebar.error('시작일이 종료일 보다 클 수 없습니다!')
            else :
                end_ = pd.to_datetime(end_date)
                start_ = pd.to_datetime(start_date)
        else :
            start_ -= relativedelta(months=date_dic[selected_date])

        run_travel_func(df, selected_trand, start_, end_)

if __name__ == '__main__':
    main()