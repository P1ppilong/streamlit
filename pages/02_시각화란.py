import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title='IP by AI', layout='wide')

def log_user_activity(userid, action):
    log_filename = f"./log/log_{datetime.now().strftime('%Y%m%d')}.log"
    with open(log_filename, 'a') as f:
        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {userid}, {action}\n"
        f.write(log_entry)

def filteringApp(df, userid):
    if userid == 'asdf':
        return df
    else:
        return df[df['userid'] == userid]

def save_note_to_csv(file_path, userid, note):
    with open(file_path, 'a') as f:
        inputtxt = f'{userid},"{note}"\n'
        f.write(inputtxt)

def delete_note_from_csv(file_path, note_to_delete):
    df = pd.read_csv(file_path, encoding='cp949')
    df = df[df['content'] != note_to_delete]
    df.to_csv(file_path, index=False, encoding='cp949')

st.subheader('시각화란')

if st.session_state.login != '':
    if st.sidebar.button('로그아웃'):
        st.session_state.login = ''

if st.session_state.login == '':
    st.error('로그인을 먼저하세요.')
else:

    log_user_activity(st.session_state.login, '로그인')
    
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = '돌아보기'

    tabs = st.tabs(['시각화의 개념'])
    tab_names = ['시각화의 개념']

    for i, tab in enumerate(tabs):
        if tab_names[i] != st.session_state.current_tab:
            log_user_activity(st.session_state.login, f"탭 '{tab_names[i]}' 선택")
            st.session_state.current_tab = tab_names[i]

    with tabs[0]:  # 시각화의 개념
        with st.expander('시각화'):
            st.subheader('시각화의 개념 및 종류에 대한 소개')
            txtdata_c1 = '''
            시각화는 수치나 통계 데이터를 그래픽으로 표현하여 분석 결과를 직관적으로 이해하기 쉽게 만드는 기술이다.
            '''
            st.markdown(txtdata_c1)

            col1, col2 = st.columns(2)
            with col1:
                st.image("https://i.imgur.com/lgTTS4o.png", use_container_width=True)
                st.markdown("<p style='text-align:center;'>박스 플롯</p>", unsafe_allow_html=True)
            with col2:
                st.image("https://i.imgur.com/n1NwLwG.png", use_container_width=True)
                st.markdown("<p style='text-align:center;'>히스토그램 분포도</p>", unsafe_allow_html=True)

            col3, col4 = st.columns(2)
            with col3:
                st.image("https://i.imgur.com/G0mmU5N.png", use_container_width=True)
                st.markdown("<p style='text-align:center;'>산점도</p>", unsafe_allow_html=True)
            with col4:
                st.image("https://i.imgur.com/nf7BchB.png", use_container_width=True)
                st.markdown("<p style='text-align:center;'>차트</p>", unsafe_allow_html=True)