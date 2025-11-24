import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title='IP by AI', layout='wide')

# -----------------------------
# 기능 함수들
# -----------------------------
def log_user_activity(userid, action):
    log_filename = f"./log/log_{datetime.now().strftime('%Y%m%d')}.log"
    os.makedirs("./log", exist_ok=True)
    with open(log_filename, 'a') as f:
        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {userid}, {action}\n"
        f.write(log_entry)

def filteringApp(df, userid):
    if userid == 'asdf':
        return df
    else:
        return df[df['userid'] == userid]

def save_note_to_csv(file_path, userid, note):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'a', encoding='utf-8') as f:
        inputtxt = f'{userid},"{note}"\n'
        f.write(inputtxt)

def delete_note_from_csv(file_path, note_to_delete):
    df = pd.read_csv(file_path, encoding='cp949')
    df = df[df['content'] != note_to_delete]
    df.to_csv(file_path, index=False, encoding='cp949')

# -----------------------------
# 로그인 확인
# -----------------------------
st.subheader('제목')

if st.session_state.login != '':
    if st.sidebar.button('로그아웃'):
        st.session_state.login = ''

if st.session_state.login == '':
    st.error('로그인을 먼저하세요.')
else:

    log_user_activity(st.session_state.login, '로그인')

    # -----------------------------
    # 탭 구성
    # -----------------------------
    tab1, tab2 = st.tabs(['정리하기', '다음차시 예고'])

    # -----------------------------
    # 탭 1 : 연습 문제 + 채점
    # -----------------------------
    with tab1:

        # ⚠ success 박스에는 텍스트만 넣기!
        st.success('연습 문제를 통해 배운 내용 정리 및 복습')
        st.markdown("아래 연습 문제를 풀어보고 채점해봅시다!")

        # -----------------------------
        # 문제 UI (success 박스 밖으로 빼기)
        # -----------------------------

        st.write("## 1. 엘니뇨(El Niño)와 라니냐(La Niña)의 주요 차이를 올바르게 설명한 것은 무엇인가?")
        q1 = st.radio("객관식", ["① 엘니뇨는 해수 온도가 낮아지고, 라니냐는 해수 온도가 높아진다.", "② 엘니뇨는 해수 온도가 높아지고, 라니냐는 해수 온도가 낮아진다", "③ 두 현상 모두 해수 온도가 높아지는 현상이다.", "④ 엘니뇨와 라니냐는 모두 기온에 영향을 주지 않는다."], index=None)

        st.write("## 2. 엘니뇨와 라니냐가 전 세계 기후에 미치는 공통된 영향은 무엇인가?")
        q2 = st.radio("객관식", ["① 폭염과 가뭄만 증가시킨다.", "② 지역별로 다른 형태의 이상기후를 유발한다.", "③ 한파를 약화시킨다.", "④ 기후에는 영향을 주지 않는다."], index=None)

        st.write("## 3. 다음은 1951~2023년도의 해수면 평균 기온 변화 그래프다. 그래프에서 나타나는 특징을 가장 올바르게 해석한 것은 무엇인가?")
        st.image("https://imgur.com/pDmvYbn.png", use_container_width=True)
        q3 = st.radio("객관식", ["① 기온의 변화폭이 일정하다.", "② 엘니뇨 기간 동안 기온이 평년보다 상승하는 경향을 보인다.", "③ 엘니뇨 기간 동안 기온이 하락한다.", "④ 기온은 엘니뇨와 관계가 없다."], index=None)

        st.write("## 4. 2020~2022년 라니냐 기간 동안 강수량 데이터에서 평균 강수량이 증가한 지역이 있다면, 이 현상은 어떤 기후적 의미를 가지는가?")
        q4 = st.text_area("서술형", key="q4_unique_key")

        st.write("## 5.아래와 같은 상관계수(correlation coefficient)가 계산되었다면, 어떤 의미로 해석할 수 있는가?")
        st.markdown(
            """
            <div style='background-color:#f0f0f0; padding:10px; border-radius:5px; width:fit-content;'>
                corr = 0.78
            </div>
            """,
            unsafe_allow_html=True
        )
        q5 = st.text_area("서술형", key="q5_unique_key")

        st.write("## 6. 최근 30년 동안 엘니뇨·라니냐의 발생 주기가 짧아지고 강도가 커졌다는 것은 어떤 기후적 의미를 가지는가?")
        q6 = st.text_area("서술형",  key="q6_unique_key")

        # -----------------------------
        # 채점 버튼
        # -----------------------------
        if st.button("채점하기"):
            mcq_answers = {"q1": "②", "q2": "②", "q3": "②"}
            score = 0
            wrong = []

            if q1 == mcq_answers["q1"]:
                score += 1
            else:
                wrong.append("1번")

            if q2 == mcq_answers["q2"]:
                score += 1
            else:
                wrong.append("2번")

            if q3 == mcq_answers["q3"]:
                score += 1
            else:
                wrong.append("3번")

            st.subheader("📌 객관식 채점 결과")
            st.write(f"총점: **{score} / 3점**")

            if wrong:
                st.error(f"틀린 문제: {', '.join(wrong)}")
            else:
                st.success("모든 객관식 문제 정답!")

            # -----------------------------
            # 서술형 정답 예시
            # -----------------------------
            st.subheader("📌 서술형 정답 예시")

            st.write("### 4번 예시 답안")
            st.write("- 라니냐는 지역별 기후 영향을 다르게 나타내며 일부 지역 강수 증가 가능")

            st.write("### 5번 예시 답안")
            st.write("- corr=0.78은 강한 양의 상관관계를 의미")

            st.write("### 6번 예시 답안")
            st.write("- 기후 변동성 심화, 극단적 기상 증가 가능성")

            # -----------------------------
            # 서술형 저장
            # -----------------------------
            save_path = "./notes/subjective_answers.csv"
            save_note_to_csv(save_path, st.session_state.login, f"Q4: {q4}")
            save_note_to_csv(save_path, st.session_state.login, f"Q5: {q5}")
            save_note_to_csv(save_path, st.session_state.login, f"Q6: {q6}")

            st.success("서술형 답안이 저장되었습니다!")

    # -----------------------------
    # 탭 2
    # -----------------------------
    with tab2:
        st.success('다음 차시 예고')
        url = 'https://youtu.be/xuOny2OIiC0?si=Fd7DflFqui6bfj3K'
        st.video(url)

