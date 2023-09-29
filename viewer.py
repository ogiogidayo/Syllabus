import streamlit as st
import requests
import json
import pandas as pd

page = st.sidebar.selectbox('Choose your page', ['users', 'シラバス登録', 'シラバス一覧'])

if page == 'users':
    st.title('ユーザー登録画面')
    with st.form(key='user'):
        username: str = st.text_input('ユーザー名', max_chars=12)
        data = {'username': username}
        submit_button = st.form_submit_button(label='ユーザー登録')

    if submit_button:
        url = 'https://syllabus-api-i5xd.onrender.com/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('ユーザー登録完了!')
            st.json(res.json())


elif page == 'シラバス一覧':
    st.title('シラバス一覧')
    # シラバス一覧の取得
    url_lectures = 'https://syllabus-api-i5xd.onrender.com/read_lecture'
    res = requests.get(url_lectures)
    lectures = res.json()
    df_lectures = pd.json_normalize(lectures)
    df_lectures = ['講義名', '担当教員', '講義情報', '更新者ID', '識別ID']
    df_lectures


elif page == 'シラバス登録':
    st.title('シラバス登録画面')
    # ユーザー一覧取得
    url_users = 'https://syllabus-api-i5xd.onrender.com/users'
    res = requests.get(url_users)
    users = res.json()
    users_dict = {}
    for user in users:
        users_dict[user['username']] = user['user_id']

    with st.form(key='syllabus'):
        username: str = st.text_input('ユーザー名(登録済みのもの)')
        lecture_name: str = st.text_input('講義名', max_chars=30)
        lecture_tech: str = st.text_input('教員名', max_chars=20)
        lecture_info: str = st.text_area('講義情報', max_chars=200)
        submit_button = st.form_submit_button(label='シラバス登録')

    if submit_button:
        user_id: int =users_dict[username]

        data = {
            'lecture_name': lecture_name,
            'lecture_tech': lecture_tech,
            'lecture_info': lecture_info,
            'user_id': user_id
        }
        # シラバス登録
        url = 'https://syllabus-api-i5xd.onrender.com/create_lecture'
        try:
            res = requests.post(
            url,
            data=json.dumps(data)
            )
        except KeyError:
            st.text('エラー')
        if res.status_code == 200:
                st.success('シラバス登録完了')
                st.json(res.json())
