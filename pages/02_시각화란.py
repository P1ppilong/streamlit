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

st.subheader('엘니뇨 라니냐에 대한 데이터 분석')

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
데이터 시각화(data visualization)는 데이터 분석 결과를 쉽게 이해할 수 있도록 시각적으로 표현하고 전달하는 과정을 말한다. 데이터 시각화의 목적은 도표(graph)라는 수단을 통해 정보를 명확하고 효과적으로  전달하는 것이다(Friedman, 2008). 때로는 한 장의 그림이 책 한 권의 설명보다 더 설득력이 있기 때문이다. 우리 속담에도 백번 듣는 것보다 한 번 보는 게 낫다고 했다. 프리드먼(Friedman)은 데이터 시각화는 지나치게 기능적인 측면을 강조하거나 아름답게 표현하는 데만 매달려서는 안 된다고 설명한다. 의미를 효과적으로 전달하기 위해서는 심미적인 형태와 기능적인 요소가 조화를 이루어야 하기 때문이다. 이상적인 시각화란 단지 명확하게 의사를 전달하는 데 머물러서는 안 되고 보는 사람을 집중하게 하고 참여하게 만들어야 한다.
            '''
            st.markdown(txtdata_c1)

            def centered_image(url, width=400):
                return f"""
                <div style='text-align: center;'>
                    <img src='{url}' style='width:{width}px; height:auto;'/>
                </div>
                """

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(centered_image("https://i.imgur.com/lgTTS4o.png"), unsafe_allow_html=True)
                st.markdown("<p style='text-align:center;'>박스 플롯은 데이터의 분포를 요약하여 보여준다. 박스플롯은 최솟값, 제 1사분위수(Q1), 중앙값(Q2), 제3사분위수(Q3), 최대값을 시각적으로 표현한다.</p>", unsafe_allow_html=True)

            with col2:
                st.markdown(centered_image("https://i.imgur.com/n1NwLwG.png"), unsafe_allow_html=True)
                st.markdown("<p style='text-align:center;'>히스토그램은 데이터의 분포를 시각적으로 표현하는 데 사용된다. 각 막대는 특정 범위의 값을 가지는 데이터의 개수를 나타낸다.</p>", unsafe_allow_html=True)


            col3, col4 = st.columns(2)

            with col3:
                st.markdown(centered_image("https://i.imgur.com/G0mmU5N.png"), unsafe_allow_html=True)
                st.markdown("<p style='text-align:center;'>산점도는 도표를 이용해 좌표상의 점들을 표시함으로써 두개 변수 간의 관계를 나타내는 그래프 방법이다. 도표 위에 두 변수 값이 만나는 지점을 표시한 그림이다.</p>", unsafe_allow_html=True)

            with col4:
                st.markdown(centered_image("https://i.imgur.com/nf7BchB.png"), unsafe_allow_html=True)
                st.markdown("<p style='text-align:center;'>차트는 데이터의 패턴, 변화, 관계 등을 시각적으로 쉽게 이해할 수 있도록 도와주는 도구이다. 막대, 선, 파이 등 다양한 종류의 차트가 있다.</p>", unsafe_allow_html=True)

