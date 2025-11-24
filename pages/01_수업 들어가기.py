import streamlit as st
import pandas as pd
from datetime import datetime

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

st.subheader('엘니뇨 라니냐에 대한 데이터 분석')

if st.session_state.login != '':
    if st.sidebar.button('로그아웃'):
        st.session_state.login = ''

if st.session_state.login == '':
    st.error('로그인을 먼저하세요.')
else:

    log_user_activity(st.session_state.login, '로그인')
    
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = '들어가기'

    tabs = st.tabs(['지난 시간에 우리는', '학습목표'])
    tab_names = ['지난 시간에 우리는', '학습목표']

    for i, tab in enumerate(tabs):
        if tab_names[i] != st.session_state.current_tab:
            log_user_activity(st.session_state.login, f"탭 '{tab_names[i]}' 선택")
            st.session_state.current_tab = tab_names[i]

    with tabs[0]: #지난 시간에 우리는
        with st.expander('지난 시간 복습'):
            st.subheader('자료 수집 및 분석 방법')
            txtdata_c1 = '''
            자료 수집 및 분석 방법에는 검색 엔진 활용, 전문기관 자료 활용, 온라인 설문 활용, 측정 및 실험 활용 등이 있습니다. 
'''
            st.markdown(txtdata_c1)

    with tabs[1]: #학습목표
        html = """
    <html>
      <body>
        <div style="position: relative; border: 1px dashed #999; border-radius: 5px; padding: 20px; 
                    font-family: Arial, sans-serif; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
                    margin: 20px auto; max-width: 500px; background-color: #f9f9f9;">
          <span style="position: absolute; top: -10px; left: 10px; background-color: #fff; 
                       padding: 0 10px; font-weight: bold; color: #333; font-size: 14px;">
            오늘의 학습 목표
          </span>
          <div style="text-align: center; margin-top: 40px; font-size: 16px; 
                      line-height: 1.5; color: #555;">
            엘리뇨 라니냐에 대해 알고 이에 관한 분석 프로그래밍을 할 수 있다.
            <br>
            <br>
          </div>
        </div>
      </body>
    </html>
    """

        st.markdown(html, unsafe_allow_html=True)


