import streamlit as st
if 'login' not in st.session_state:
    st.session_state['login'] = ''

    # {'login': ''}

st.set_page_config(page_title='IP by AI', layout='wide')
st.title('제목')

if st.session_state.login != '':
    if st.sidebar.button('로그아웃'):
        st.session_state.login = ''


c1, c2 = st.columns(2)
with c1:
    st.image('./images/01.png')
with c2:
    t1, t2 = st.tabs(['Login', 'Register'])
    with t1: 
        if st.session_state['login'] != '':
            st.info(f'{st.session_state.login}님 환영합니다. 로그인에 성공하였습니다.')
        else:
            with st.form('loginform'):
                userid = st.text_input('userID', key='luserid')
                passwd = st.text_input('passWD', key='lpasswd')
                if st.form_submit_button('Login'):
                    if all([userid, passwd]):
                        import pandas as pd
                        df = pd.read_csv('./users.csv', encoding = 'cp949')
                        idlist = list(df.iloc[:, 1])
                        passwdlist = list(df.iloc[:, 2])
                        if userid in idlist and passwd in passwdlist:
                            st.session_state['login'] = userid
                            st.success(f'{userid}의 로그인이 성공했습니다.')
                            st.rerun()
                        else:
                            st.error('등록된 사용자가 아닙니다. 또는 ID와 PASSWD가 일치하지 않습니다.')
                        st.table(df)
                        st.success('로그인 성공')
                    else:
                        st.error('모든 정보를 입력해야 합니다.')
    with t2: 
        with st.form('register'):
                #import pandas as pd
                #df = pd.read_csv('./users.csv')
                #st.table(df)
            
            grade = st.selectbox('학년선택', [f'{x}학년' for x in range(1,13)], key='grade')
            userid = st.text_input('userID')
            passwd = st.text_input('passWD')
            if st.form_submit_button('Register'):
                if all([grade, userid, passwd]):
                    with open('./users.csv', 'a') as f:
                        inputtxt = f'{grade},{userid},{passwd}\n'
                        f.write(inputtxt)
                        f.close()
                        
                    st.success('등록 성공')
                else:
                    st.error('모든 정보를 입력해야 합니다.')
st.info('copyfight(c) all rights reserved since 2025 powered by B3A2')
