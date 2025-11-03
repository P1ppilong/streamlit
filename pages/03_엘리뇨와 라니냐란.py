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

st.subheader('제목')

if st.session_state.login != '':
    if st.sidebar.button('로그아웃'):
        st.session_state.login = ''

if st.session_state.login == '':
    st.error('로그인을 먼저하세요.')
else:

    log_user_activity(st.session_state.login, '로그인')
    
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = '남방 진동'

    tabs = st.tabs(['남방 진동', '엘리뇨와 라니냐', '우리나라 기후에 미치는 영향', '엘리뇨와 라니냐의 기준', '엘리뇨와 라니냐 전망'])
    tab_names = ['남방 진동', '엘리뇨와 라니냐', '우리나라 기후에 미치는 영향', '엘리뇨와 라니냐의 기준', '엘리뇨와 라니냐 전망']

    for i, tab in enumerate(tabs):
        if tab_names[i] != st.session_state.current_tab:
            log_user_activity(st.session_state.login, f"탭 '{tab_names[i]}' 선택")
            st.session_state.current_tab = tab_names[i]

    with tabs[0]:  # 남방 진동
        with st.expander('남방 진동'):
            st.subheader('남방 진동')
            txtdata_c1 = '''
            남방 진동이란 동태평양에서 기압이 상승하거나 하강하면, 반대로 서태평양에서는 기압이 하강하거나 상승하는 것이다.
            '''
            st.markdown(txtdata_c1)

    with tabs[1]:  # 엘리뇨와 라니냐
        with st.expander('엘리뇨와 라니냐 1'):
            st.subheader('엘리뇨와 라니냐 정의')
            txtdata_c1 = '''
            평소 서태평양의 해수면 온도는 높고 동태평양은 상대적으로 낮아 서고-동저의 해수면온도 분포를 보인다. 대기에서는 적도를 따라 무역풍이 동쪽에서 서쪽으로 불고 있으며, 서태평양에서 대류활동이 활발하게 나타난다.
 2-5년마다 상대적으로 낮았던 열대 동태평양과 중태평양의 해수면온도가 평상시보다 높은 상태로 수개월이상 지속되는 현상이 나타는데 이를 엘니뇨라 한다. 엘니뇨는 대체로 봄~여름철에 발생해 겨울까지 발달하다가 이후 점차 약해지며, 이듬해 봄∼여름철에 소멸하는 경향을 보인다. 이 시기에 적도 태평양의 무역풍은 약해지고 강한 대류활동 영역이 서태평양에서 중태평양으로 확장·이동하게 된다. 대기의 변화로 인해 해양에서는 동태평양에서 수온약층이 깊어지고 해수면온도가 상승해 다시 대기의 변화를 유도한다. 라니냐는 엘니뇨의 반대 현상으로 중동태평양의 해수면온도가 평상시보다 낮아지고 무역풍이 평소보다 강해진다.
            '''
            st.markdown(txtdata_c1)

        with st.expander('엘리뇨와 라니냐 2'):
            st.subheader('엘리뇨와 라니냐의 전지구 기후 관련성')
            txtdata_c2 = '''
            엘니뇨·라니냐는 열대 태평양에 국한되어 나타나는 현상이지만, 대기와 해양을 통해 전 지구 기상·기후에 영향을 미치게 되며, 그 영향은 지역과 계절에 따라 다르게 나타난다.
 엘니뇨가 최고조로 발달하는 겨울철에 북반구에서는 유라시아 중·동부와 알래스카 지역을 포함하는 북미 서북부에서 평상시보다 높은 기온을 보이고, 남반구에서는 아프리카 남서부 지역과 호주 서쪽, 그리고 남미 북부 지역이 상대적으로 높은 기온을 보인다. 강수량은 열대 서·중태평양에서 증가하고 인도네시아 부근과 호주 북부에서 평상시보다 감소한다.
 라니냐가 최고조로 발달하는 북반구의 겨울철에, 열대 서·중태평양에서 강수가 감소하고, 인도네시아 부근에서 강수가 뚜렷하게 증가한다. 남미 북부에서는 강수량이 증가, 남미 중·동부 지역에서는 감소하는 현상이 나타난다. 유라시아 북부와 캐나다 북부를 제외하고는 북반구에서 대체로 평상시보다 기온이 낮은 경향을 보이는 것이 특징이다.
            '''
            st.markdown(txtdata_c2)
            st.image("https://imgur.com/tML4fVu.png", use_container_width=True)
    
    with tabs[2]:  # 우리나라 기후에 미치는 영향
        with st.expander('우리나라 기후에 미치는 영향'):
            st.subheader('우리나라 기후에 미치는 영향')
            txtdata_c1 = '''
            엘니뇨·라니냐가 발달하는 시기의 우리나라 여름철 강수 변화는 월별로 차이가 있지만, 7월 중순부터 8월 중순까지 엘니뇨 시기에 우리나라 강수가 증가하고, 라니냐 시기에는 강수가 감소하는 경향이 한반도 남부 지역을 중심으로 나타난다. 엘니뇨가 최대로 발달하는 이른 겨울철(11, 12월)에 한반도의 강수는 증가하고 기온은 상승하는 경향 보인다. 11월 강수가 평년의 2배 이상인 100 ㎜ 이상 내렸던 해는 1982, 1997, 2015년으로 모두 엘니뇨가 강하게 발달했던 해이다. 라니냐 시기의 11월과 12월에 강수가 감소하고, 기온이 하강하는 경향을 보인다.
            '''
            st.markdown(txtdata_c1)

    with tabs[3]:  # 엘리뇨와 라니냐의 기준
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

        with st.expander('엘리뇨와 라니냐의 빈도 및 주기'):
            st.subheader('엘리뇨의 빈도 및 주기')
            html_table = """
<table style="width:90%; margin:auto; border-collapse:collapse; font-size:16px;">
  <tr style="background-color:#f0f2f6; text-align:center;">
    <th style="border:1px solid #ccc; padding:8px;">항목</th>
    <th style="border:1px solid #ccc; padding:8px;">내용</th>
  </tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">발생 횟수</td><td style="border:1px solid #ccc; padding:8px;">1951년부터 2023년까지 총 24회</td></tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">주기</td><td style="border:1px solid #ccc; padding:8px;">평균적으로 약 3년 주기</td></tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">빈도</td><td style="border:1px solid #ccc; padding:8px;">1970년대 이후 발생 빈도가 높아짐</td></tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">특징</td><td style="border:1px solid #ccc; padding:8px;">특히 1997~1998년, 2015~2016년, 2023년에 강한 엘니뇨(극값, 온도편차 2℃ 이상) 발생</td></tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">특징</td><td style="border:1px solid #ccc; padding:8px;">지속기간은 보통 8개월~1년 반 정도, 최근 발생은 단기간보다 장기간 경향이 강화</td></tr>
</table>
"""
            st.markdown(html_table, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader('라니냐의 빈도 및 주기')
            html_table2 = """
<table style="width:90%; margin:auto; border-collapse:collapse; font-size:16px;">
  <tr style="background-color:#f0f2f6; text-align:center;">
    <th style="border:1px solid #ccc; padding:8px;">항목</th>
    <th style="border:1px solid #ccc; padding:8px;">내용</th>
  </tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">발생 횟수</td><td style="border:1px solid #ccc; padding:8px;">1954년부터 2023년까지 총 16회</td></tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">주기</td><td style="border:1px solid #ccc; padding:8px;">평균적으로 약 4~5년 주기</td></tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">빈도</td><td style="border:1px solid #ccc; padding:8px;">1970년대 후반과 2000년대 이후에 빈도 다소 증가</td></tr>
  <tr><td style="border:1px solid #ccc; padding:8px;">특징</td><td style="border:1px solid #ccc; padding:8px;">특히 2010~2012년, 2020~2022년에는 연속된 라니냐가 발생하여 장기적인 기후 패턴 이상 초래</td></tr>
</table>
"""
            st.markdown(html_table2, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader('비교')
            txtdata_c3 = '''
            - 전체적으로 엘니뇨(24회)가 라니냐(16회)보다 더 자주 발생한다.
- 엘니뇨는 강한 단일 이벤트(극단적 기온 상승)를 자주 보이는 반면, 라니냐는 상대적으로 지속적이고 완만한 기온 하강 패턴을 보인다.
- 주기성에서 보면, 엘니뇨는 주기가 짧으나 강도가 세고, 라니냐는 긴 주기에 지속성이 길다는 특징이 나타난다.
            '''
            st.markdown(txtdata_c3)
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader('기후변화적 의미')
            txtdata_c4 = '''
최근 30년간(1990년대 이후) 엘니뇨·라니냐 모두 발생 주기가 짧아지고, 강도가 커졌다. 이는 엘니뇨 라니냐 현상이 지구온난화와 결합하여 전 세계적으로 폭염, 가뭄, 홍수, 태풍 등 극단적 기상 현상 발생 빈도를 높이는 주요 원인으로 작용하고 있음을 알 수 있다. 
            '''
            st.markdown(txtdata_c4)
            st.markdown("<br>", unsafe_allow_html=True)

    with tabs[4]:  
        with st.expander('엘리뇨와 라니냐의 전망'):
            st.subheader('2025. 08. 22 (금) 11:00 기준')

            txtdata_c1 = """
            **- 해수면 온도:**  
            최근(8월 10일~16일) 해수면 온도 현황 - 열대 태평양의 엘니뇨·라니냐 감시구역의 해수면 온도는 26.6℃로, 평년보다 0.3℃ **낮은 상태**를 보이고 있다.  

            **- 전망:**  
            현재 엘니뇨도 라니냐도 아닌 **중립 상태**이며,  
            전망 기간(2025년 9~11월) 동안 해수면 온도가 점차 하강하여 **약한 라니냐 경향**을 보일 것으로 예상된다.
            """
            st.markdown(txtdata_c1)

            st.image("https://imgur.com/uVxIJgR.png", use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
