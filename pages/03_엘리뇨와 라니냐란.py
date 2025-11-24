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
        st.session_state.current_tab = '남방 진동'

    tabs = st.tabs(['엘리뇨와 라니냐', '엘리뇨와 라니냐의 기준'])
    tab_names = ['엘리뇨와 라니냐', '엘리뇨와 라니냐의 기준']

    for i, tab in enumerate(tabs):
        if tab_names[i] != st.session_state.current_tab:
            log_user_activity(st.session_state.login, f"탭 '{tab_names[i]}' 선택")
            st.session_state.current_tab = tab_names[i]
      
    with tabs[0]:  # 엘리뇨와 라니냐
        with st.expander('남방 진동'):
            st.subheader('남방 진동')
            txtdata_c1 = '''
            남방 진동이란 동태평양에서 기압이 상승하거나 하강하면, 반대로 서태평양에서는 기압이 하강하거나 상승하는 것이다.
            '''
            st.markdown(txtdata_c1)
        with st.expander('엘리뇨와 라니냐의 정의'):
            st.subheader('엘리뇨와 라니냐의 정의')
            txtdata_c1 = '''
            평소 서태평양의 해수면 온도는 높고 동태평양은 상대적으로 낮아 서고-동저의 해수면온도 분포를 보인다. 대기에서는 적도를 따라 무역풍이 동쪽에서 서쪽으로 불고 있으며, 서태평양에서 대류활동이 활발하게 나타난다.
 2-5년마다 상대적으로 낮았던 열대 동태평양과 중태평양의 해수면온도가 평상시보다 높은 상태로 수개월이상 지속되는 현상이 나타는데 이를 엘니뇨라 한다. 엘니뇨는 대체로 봄~여름철에 발생해 겨울까지 발달하다가 이후 점차 약해지며, 이듬해 봄∼여름철에 소멸하는 경향을 보인다. 이 시기에 적도 태평양의 무역풍은 약해지고 강한 대류활동 영역이 서태평양에서 중태평양으로 확장·이동하게 된다. 대기의 변화로 인해 해양에서는 동태평양에서 수온약층이 깊어지고 해수면온도가 상승해 다시 대기의 변화를 유도한다. 라니냐는 엘니뇨의 반대 현상으로 중동태평양의 해수면온도가 평상시보다 낮아지고 무역풍이 평소보다 강해진다.
            '''
            st.markdown(txtdata_c1)

        with st.expander('엘리뇨와 라니냐의 전지구 기후 관련성'):
            st.subheader('엘리뇨와 라니냐의 전지구 기후 관련성')
            txtdata_c2 = '''
            엘니뇨·라니냐는 열대 태평양에 국한되어 나타나는 현상이지만, 대기와 해양을 통해 전 지구 기상·기후에 영향을 미치게 되며, 그 영향은 지역과 계절에 따라 다르게 나타난다.
 엘니뇨가 최고조로 발달하는 겨울철에 북반구에서는 유라시아 중·동부와 알래스카 지역을 포함하는 북미 서북부에서 평상시보다 높은 기온을 보이고, 남반구에서는 아프리카 남서부 지역과 호주 서쪽, 그리고 남미 북부 지역이 상대적으로 높은 기온을 보인다. 강수량은 열대 서·중태평양에서 증가하고 인도네시아 부근과 호주 북부에서 평상시보다 감소한다.
 라니냐가 최고조로 발달하는 북반구의 겨울철에, 열대 서·중태평양에서 강수가 감소하고, 인도네시아 부근에서 강수가 뚜렷하게 증가한다. 남미 북부에서는 강수량이 증가, 남미 중·동부 지역에서는 감소하는 현상이 나타난다. 유라시아 북부와 캐나다 북부를 제외하고는 북반구에서 대체로 평상시보다 기온이 낮은 경향을 보이는 것이 특징이다.
            '''
            st.markdown(txtdata_c2)
            st.image("https://imgur.com/zQbmSym.png", use_container_width=True)
            
        with st.expander('우리나라 기후에 미치는 영향'):
            st.subheader('우리나라 기후에 미치는 영향')
            txtdata_c1 = '''
            엘니뇨·라니냐가 발달하는 시기의 우리나라 여름철 강수 변화는 월별로 차이가 있지만, 7월 중순부터 8월 중순까지 엘니뇨 시기에 우리나라 강수가 증가하고, 라니냐 시기에는 강수가 감소하는 경향이 한반도 남부 지역을 중심으로 나타난다. 엘니뇨가 최대로 발달하는 이른 겨울철(11, 12월)에 한반도의 강수는 증가하고 기온은 상승하는 경향 보인다. 11월 강수가 평년의 2배 이상인 100 ㎜ 이상 내렸던 해는 1982, 1997, 2015년으로 모두 엘니뇨가 강하게 발달했던 해이다. 라니냐 시기의 11월과 12월에 강수가 감소하고, 기온이 하강하는 경향을 보인다.
            '''
            st.markdown(txtdata_c1)
    
    with tabs[1]:  # 엘리뇨와 라니냐의 기준
        with st.expander('엘리뇨와 라니냐의 기준'):
            st.subheader('엘리뇨와 라니냐의 기준')
            txtdata_c1 = '''
            엘니뇨·라니냐 감시구역(열대 태평양 Nino 3.4 지역 : 5°S~5°N, 170°W~120°W)의 3개월 이동평균한 해수면온도 편차가 +0.5℃ 이상(-0.5℃ 이하)으로 5개월 이상 지속될 때 그 첫 달을 엘니뇨(라니냐)의 시작으로 본다.
            '''
            st.markdown(txtdata_c1)

        with st.expander('엘리뇨와 라니냐의 감시 구역'):
            st.subheader('엘리뇨와 라니냐의 감시 구역')
            txtdata_c2 = '''
            Nino 3.4(ⓐ:5°S~5°N, 170~120°W)
            '''
            st.markdown(txtdata_c2)

            st.image("https://imgur.com/wmYwzwb.png", use_container_width=True)



