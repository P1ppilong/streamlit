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
        st.session_state.current_tab = '데이터 분석 정리하기 '

    tabs = st.tabs(['데이터 분석 정리하기', '느낀 점 공유하기'])
    tab_names = ['데이터 분석 정리하기', '느낀 점 공유하기', ]

    for i, tab in enumerate(tabs):
        if tab_names[i] != st.session_state.current_tab:
            log_user_activity(st.session_state.login, f"탭 '{tab_names[i]}' 선택")
            st.session_state.current_tab = tab_names[i]

    with tabs[0]:  # 시각화된 데이터를 통한 분석 정리
        with st.expander('데이터 분석 정리하기'):
            st.subheader('시각화된 데이터를 통한 분석 정리하기')
            url = 'https://padlet.com/susan053021/padlet-ngflb7944bqldmg2'
            components.iframe(url, width=1400, height=768)

    with tabs[1]:  # 패들렛을 활용해 기후변화의 심각성에 대해 느낀 내용을 친구들과 공유
        with st.expander('데이터 분석을 통해 느낀 점'):
            st.subheader('데이터 분석을 통해 느낀 점')
            txtdata_c1 = '''
            이번 활동을 통해 지구온난화의 심각성 등 깨달은 것을 작성해봅시다. '''
            st.markdown(txtdata_c1)
            url = 'https://padlet.com/susan053021/class-activities-sfflhnru5ew5ndbc'
            components.iframe(url, width=1400, height=768)

        with st.expander('감상평 작성하기'):
            st.subheader('감상평 작성하기 ')
            txtdata_c2 = '''
            기후변화의 심각성에 대해 느낀 내용을 토대로 '지구 온난화'의 심각성 및 예방실천방안에 대한 감상평을 작성해봅시다.'''
            st.markdown(txtdata_c2)
            url = 'https://padlet.com/susan053021/class-activities-sfflhnru5ew5ndbc'
            components.iframe(url, width=1400, height=768)

        with st.expander('발표하기'):
            st.subheader('발표하기')
            txtdata_c2 = '''
             기후변화의 심각성에 대해 느낀 내용을 친구들과 공유해봅시다!
             친구들의 데이터 분석 결과 발표를 듣고, '지구 온난화'의 심각성 및 예방실천방안에 대한 감상평을 작성해봅시다.'''
            st.markdown(txtdata_c2)
            url = 'https://padlet.com/susan053021/class-activities-sfflhnru5ew5ndbc'
            components.iframe(url, width=1400, height=768)
