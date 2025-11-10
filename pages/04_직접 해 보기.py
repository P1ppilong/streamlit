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
            txtdata = '''
            이번 활동은 실제 기후 데이터를 직접 분석하고 시각화함으로써, 기후변화의 원인과 양상을 데이터 기반으로 탐구해 보는 시간입니다.\n\n
<font color="BLACK" size="+5"><b>1.데이터 수집하기</b></font>\n\n-기상청, NASA 등에서 제공하는 공신력 있는 기후 데이터를 탐색해 보세요.\n\n-기온, 강수량, 엘니뇨·라니냐 지수 중 분석할 데이터를 선택하여 가져옵니다.\n\n
<font color="BLACK" size="+5"><b>2. 데이터 분석하기</b></font>\n\n-수집한 데이터를 기간(연도, 계절) 또는 지역별로 정리해 보세요.\n\n-평균, 추세선을 계산하며 기후 변화의 패턴을 찾아봅니다.\n\n
<font color="BLACK" size="+5"><b>3. 데이터 시각화하기</b></font>\n\n-그래프, 히트맵, 워드클라우드 등 다양한 방식으로 데이터를 시각화해 보세요.\n\n-그래프를 통해 드러나는 특징을 비교하고, 변화의 의미를 해석해 봅니다.\n\n
<font color="BLACK" size="+5"><b>4. 결과 해석 및 성찰하기</b></font>\n\n-분석 과정에서 얻은 통찰을 바탕으로, “기후변화는 왜 일어나며 앞으로 어떤 영향을 미칠까?”라는 질문에 대한 자신의 생각을 정리해 보세요.\n\n-데이터가 전하는 메시지를 바탕으로 기후문제의 심각성과 우리의 역할을 함께 고민해 봅시
다.'''
            st.markdown(txtdata,  unsafe_allow_html=True)
            

    with tabs[1]:  # 활동하기
        with st.expander('데이터 수집하기'): #공공 데이터 포털 등을 통한 기후 변화 관련 데이터 수집
            st.subheader('기후 변화 관련 데이터를 수집하자')
            txtdata_c1 = '''
            공공 데이터 포털 등을 통한 기후 변화 관련 데이터를 수집합시다'''
            st.markdown(txtdata_c1)

        with st.expander('<데이터 수집 사이트>'):
            txtdata = '''
            - OISST(Optimum Interpolation SST/주별 변화)\n\n- ERSST(Extended Reconstructed SST/월별 변화)\n\n- 대한민국 기상청 날씨누리(기후예측 통보문/엘니뇨라니냐 전망)\n\n- http://iri.columbia.edu'''
            st.markdown(txtdata)     

        with st.expander('데이터 분석하기'): #데이터 시각화를 파이썬을 활용해 직접 구현
            st.subheader('파이썬을 활용해 데이터를 시각화하자')
            # 활동하기 1.데이터 불러오기
            txtdata = '''
            <font color="BLACK" size="+5"><b>1.데이터 불러오기</b></font>\n\n
            - 준비된 CSV 파일(기온, 강수량, 엘니뇨·라니냐 지수 등)을 Python으로 불러옵니다.\n\n
            '''
            st.markdown(txtdata, unsafe_allow_html=True)
            
            st.markdown(
    """
    <div style="
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        background-color: #f9fafb;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.1);
        margin-bottom: 15px;
    ">
        <h4 style="margin-top: 0; margin-bottom: 7px; font-size: 15px;">예시 코드</h4>
        <p style="margin: 0;">
            import pandas as pd<br>
            data = pd.read_csv("climate_data.csv")<br>
            data.head()
            
    </div>
    """,
    unsafe_allow_html=True
)
            txtdata = '''
            - 데이터를 불러온 뒤, 열(column) 이름과 자료의 크기(shape)를 확인해 보세요.
            '''
            st.markdown(txtdata)

            # 활동하기 2.데이터 살펴보기
            txtdata = '''
            <font color="BLACK" size="+5"><b>2.데이터 살펴보기</b></font>\n\n
            - 데이터에 결측치(비어 있는 값)나 이상치가 있는지 확인합니다.'''
            st.markdown(txtdata, unsafe_allow_html=True)
            
            st.markdown(
    """
    <div style="
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        background-color: #f9fafb;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.1);
        margin-bottom: 15px;
    ">
        <h4 style="margin-top: 0; margin-bottom: 7px; font-size: 15px;">예시 코드</h4>
        <p style="margin: 0;">
            data.info()<br>
            data.describe()<br>
            data.isnull().sum()
            
    </div>
    """,
    unsafe_allow_html=True
)
            txtdata = '''
            - 데이터의 기본 통계값(평균, 최소값, 최대값)을 살펴보면 전체적인 경향을 이해할 수 있습니다.'''
            st.markdown(txtdata)

            # 활동하기 3.기간별 변화 분석하기 
            txtdata = '''
            <font color="BLACK" size="+5"><b>3.기간별 변화 분석하기</b></font>\n\n
            - 연도별 혹은 월별 평균 기온이나 강수량을 계산해 보세요.'''
            st.markdown(txtdata, unsafe_allow_html=True)
            
            st.markdown(
    """
    <div style="
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        background-color: #f9fafb;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.1);
        margin-bottom: 15px;
    ">
        <h4 style="margin-top: 0; margin-bottom: 7px; font-size: 15px;">예시 코드</h4>
        <p style="margin: 0;">
            annual_temp = data.groupby("year")["temperature"].mean()<br>
            print(annual_temp)
            
    </div>
    """,
    unsafe_allow_html=True
)
            txtdata = '''
            -  결과를 통해 특정 시기(예: 엘니뇨 발생 시기)에 어떤 변화가 있었는지 탐색합니다.'''
            st.markdown(txtdata)

            # 활동하기 4.상관관계 확인하기 
            txtdata = '''
            <font color="BLACK" size="+5"><b>4.상관관계 확인하기</b></font>\n\n
            - 엘니뇨 지수와 기온, 강수량 간의 관계를 분석해 보세요.'''
            st.markdown(txtdata, unsafe_allow_html=True)
            
            st.markdown(
    """
    <div style="
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        background-color: #f9fafb;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.1);
        margin-bottom: 15px;
    ">
        <h4 style="margin-top: 0; margin-bottom: 7px; font-size: 15px;">예시 코드</h4>
        <p style="margin: 0;">
            corr = data[["el_nino_index", "temperature", "precipitation"]].corr()<br>
            print(corr)
            
    </div>
    """,
    unsafe_allow_html=True
)
            txtdata = '''
            - 상관계수의 값이 1에 가까울수록 강한 양의 관계, -1에 가까울수록 음의 관계를 의미합니다.
            - 패턴과 이상치 탐색하기'''
            st.markdown(txtdata)

    
    with tabs[2]:  # 자료 업로드
        with st.expander('활동 결과 게시판'):
            st.subheader('활동 결과 게시하기')
            url = 'https://padlet.com/susan053021/padlet-ngflb7944bqldmg2'
            components.iframe(url, width=1400, height=768)