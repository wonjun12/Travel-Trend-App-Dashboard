import streamlit as st
import pandas as pd

from app_module.app_travel import run_travel_func
from app_module.app_about import run_about_func
from app_module.app_upload import run_upload_csv
from app_module.app_side_date import run_side_date

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
        df = df.loc[df['LWPRT_CTGRY_NM'] == selected_trand, ]

        st.image(f'image/{selected_trand}.png')
        st.header(f'{selected_trand} 검색 트랜드') 

        start_date, end_date = run_side_date(df)
        run_travel_func(df, start_date, end_date)

if __name__ == '__main__':
    main()