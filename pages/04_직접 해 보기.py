import streamlit as st
import streamlit.components.v1 as components
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

st.subheader('제목')

if st.session_state.login != '':
    if st.sidebar.button('로그아웃'):
        st.session_state.login = ''

if st.session_state.login == '':
    st.error('로그인을 먼저하세요.')
else:

    log_user_activity(st.session_state.login, '로그인')
    
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = '활동 안내'

    tabs = st.tabs(['활동 안내', '활동하기', '자료 업로드'])
    tab_names = ['활동 안내', '활동하기', '자료 업로드']

    for i, tab in enumerate(tabs):
        if tab_names[i] != st.session_state.current_tab:
            log_user_activity(st.session_state.login, f"탭 '{tab_names[i]}' 선택")
            st.session_state.current_tab = tab_names[i]

    with tabs[0]:  # 활동 안내
        with st.success('활동 안내'):
            txtdata_c1 = '''
            이번 활동은 ...
            '''
            st.markdown(txtdata_c1)

    with tabs[1]:  # 활동하기
        with st.expander('데이터 수집하기'): #공공 데이터 포털 등을 통한 기후 변화 관련 데이터 수집
            st.subheader('공공 데이터 포털 등을 통한 기후 변화 관련 데이터 수집')
            txtdata_c1 = '''
            공공 데이터 포털 등을 통한 기후 변화 관련 데이터를 수집합시다'''
            st.markdown(txtdata_c1)

        with st.expander('<데이터 수집 사이트>'):
            txtdata = '''
            - OISST(Optimum Interpolation SST/주별 변화)\n\n- ERSST(Extended Reconstructed SST/월별 변화)\n\n- 대한민국 기상청 날씨누리(기후예측 통보문/엘니뇨라니냐 전망)\n\n- http://iri.columbia.edu'''
            st.markdown(txtdata)     

        with st.expander('데이터 분석하기'): #데이터 시각화를 파이썬을 활용해 직접 구현
            st.subheader('데이터 시각화를 파이썬을 활용해 직접 구현')
            txtdata_c2 = '''
            수집한 데이터를 활용해 데이터를 시각화 해봅시다!
            데이터 시각화를 파이썬을 활용해 직접 구현합시다. '''
            st.markdown(txtdata_c2)
            

    
    with tabs[2]:  # 자료 업로드
        with st.expander('활동 결과 게시판'):
            st.subheader('활동 결과 게시하기')
            url = 'https://padlet.com/susan053021/padlet-ngflb7944bqldmg2'
            components.iframe(url, width=1400, height=768)