import streamlit as st
import pandas as pd

from dateutil.relativedelta import relativedelta

def run_side_date(df):
    end_ = df['SCCNT_DE'].max()
    start_ = end_
    
    date_list = ['1개월', '3개월', '6개월', '1년', '사용자 지정']
    selected_date = st.sidebar.selectbox('보고 싶은 날짜를 선택하세요!', date_list)
    
    date_dic = {
        date_list[0] : 1,
        date_list[1] : 3,
        date_list[2] : 6,
        date_list[3] : 12
    }

    if selected_date == date_list[-1]:
            
        max_date_value = end_
        min_date_value = df['SCCNT_DE'].min()
        
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

    return start_, end_
    