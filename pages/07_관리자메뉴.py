import glob
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='IP by AI', layout='wide')

import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
import tempfile
from langchain.document_loaders import PyPDFLoader

import os
os.environ["OPENAI_API_KEY"] = "sk-proj-DfGg8BUXGOBwIP0hx7h3T3BlbkFJVgwEqnUvzgHn6VCPBNV7" #openai 키 입력

uploaded_file = st.sidebar.file_uploader("upload", type="pdf")



# 관리자 계정 아이디 설정
ADMIN_USER_ID = 'asdf'

# 관리자 여부 설정 함수
def check_admin_login(userid):
    return userid == ADMIN_USER_ID

# 로그 기록 함수
def log_user_activity(userid, action):
    log_filename = f"./log/log_{datetime.now().strftime('%Y%m%d')}.log"  # 로그 파일 이름
    with open(log_filename, 'a') as f:
        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {userid}, {action}\n"
        f.write(log_entry)

# 로그 확인 기능
def show_logs(selected_date):
    log_filename = f"./log/log_{selected_date}.log"  # 선택된 날짜의 로그 파일
    try:
        log_data = pd.read_csv(log_filename, header=None, names=["Timestamp", "UserID", "Action"], encoding='ISO-8859-1')
        st.write(log_data)
    except FileNotFoundError:
        st.error("로그 파일이 존재하지 않습니다.")

# 로그인 상태 초기화
if 'login' not in st.session_state:
    st.session_state.login = ''
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False  # 관리자 여부 초기화

# 로그인 확인 및 관리자 설정
if st.session_state.login != '':
    st.session_state.is_admin = check_admin_login(st.session_state.login)

    # 로그아웃 버튼
    if st.sidebar.button('로그아웃'):
        st.session_state.login = ''
        st.session_state.is_admin = False

# 로그인 상태 확인
if st.session_state.login == '':
    st.error('로그인을 먼저하세요.')
else:
    # 관리자 여부 확인
    if not st.session_state.is_admin:
        st.error("이 페이지는 관리자만 접근할 수 있습니다.")
    else:

        if 'current_tab' not in st.session_state:
            st.session_state.current_tab = '활동완성본'

        tabs = st.tabs(['활동완성본', '로그 확인', '로그 분석'])
        tab_names = ['활동완성본', '로그 확인', '로그 분석']

        for i, tab in enumerate(tabs):
            if tab_names[i] != st.session_state.current_tab:
                log_user_activity(st.session_state.login, f"탭 '{tab_names[i]}' 선택")
                st.session_state.current_tab = tab_names[i]

        with tabs[0]: 
            if uploaded_file :
                with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name

                loader = PyPDFLoader(tmp_file_path)
                data = loader.load()

                embeddings = OpenAIEmbeddings()
                vectors = FAISS.from_documents(data, embeddings)

                chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0.0,model_name='gpt-4'), retriever=vectors.as_retriever())

                def conversational_chat(query):  #문맥 유지를 위해 과거 대화 저장 이력에 대한 처리
                    result = chain({"question": query, "chat_history": st.session_state['history']})
                    st.session_state['history'].append((query, result["answer"]))
                    return result["answer"]

                if 'history' not in st.session_state:
                    st.session_state['history'] = []

                if 'generated' not in st.session_state:
                    st.session_state['generated'] = ["안녕하세요! 어디가 아파서 오셨나요?"]

                if 'past' not in st.session_state:
                    st.session_state['past'] = ["안녕하세요!"]

                #챗봇 이력에 대한 컨테이너
                response_container = st.container()
                #사용자가 입력한 문장에 대한 컨테이너
                container = st.container()

                with container: #대화 내용 저장(기억)
                    with st.form(key='Conv_Question', clear_on_submit=True):
                        user_input = st.text_input("Query:", placeholder="U-헬스케어에 대해 얘기해볼까요? (:", key='input')
                        submit_button = st.form_submit_button(label='Send')

                    if submit_button and user_input:
                        output = conversational_chat(user_input)

                        st.session_state['past'].append(user_input)
                        st.session_state['generated'].append(output)

                if st.session_state['generated']:
                    with response_container:
                        for i in range(len(st.session_state['generated'])):
                            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style = "fun-emoji", seed = "Nala")
                            message(st.session_state["generated"][i], key=str(i), avatar_style = "bottts", seed = "Fluffy")


        with tabs[1]:
            log_filename = f"./log/log_{datetime.now().strftime('%Y%m%d')}.log"
            try:
                with open(log_filename, "r") as f:
                    log_data = f.read()
                st.text_area("로그 기록", log_data, height=400)
            except FileNotFoundError:
                st.error("로그 파일이 존재하지 않습니다.")

        with tabs[2]:

            log_folder_path = "C:/Users/yoonh/ethicproject/log"
            log_files = glob.glob(f"{log_folder_path}/*.log")  # 폴더 내 모든 CSV 파일 선택

            try:
                # 모든 로그 파일을 읽어들여 하나의 데이터프레임으로 결합
                log_data_list = []
                for log_filename in log_files:
                    log_data = pd.read_csv(log_filename, header=None, names=["Timestamp", "UserID", "Action"], encoding='ISO-8859-1')
                    log_data_list.append(log_data)
                
                # 여러 파일의 데이터프레임을 하나로 결합
                log_data = pd.concat(log_data_list, ignore_index=True)
                log_data["Timestamp"] = pd.to_datetime(log_data["Timestamp"])

                # 기본 분석
                st.write(f"총 로그 수: {len(log_data)}")

                # 사용자별 활동 요약
                st.subheader("사용자별 활동 요약")
                user_activity = log_data["UserID"].value_counts()
                st.bar_chart(user_activity)

                # 시간대별 활동 빈도
                log_data["Hour"] = log_data["Timestamp"].dt.hour
                st.subheader("시간대별 활동 분석")
                hourly_activity = log_data.groupby("Hour").size()
                st.line_chart(hourly_activity)

            except FileNotFoundError:
                st.error("로그 파일이 존재하지 않습니다.")
            except pd.errors.EmptyDataError:
                st.error("파일에 데이터가 없습니다.")
