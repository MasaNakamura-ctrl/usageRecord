import streamlit as st
import sqlite3
import datetime

conn = sqlite3.connect('usageRecord.db')
c = conn.cursor()

# データを表示する
def show_data():
    c.execute('SELECT * FROM usageRecord')
    data = c.fetchall()
    for d in data:
        st.write(d)

# データを追加する
def add_data(usrName, usageDate, kisJkn, kisHun, sryJkn, sryHun):
    c.execute('INSERT INTO usageRecord (usrName, usageDate, kisJkn, kisHun, sryJkn, sryHun) VALUES (?, ?, ?, ?, ?, ?)', (usrName, usageDate, kisJkn, kisHun, sryJkn, sryHun))
    conn.commit()
    st.write('登録しました。ページの再読み込みをしてください。')

# データベースにテーブルを作成する
c.execute('CREATE TABLE IF NOT EXISTS usageRecord (id INTEGER PRIMARY KEY, usrName text, usageDate text, kisJkn text, kisHun text, sryJkn text, sryHun text)')

st.title('入退室管理')
st.write('利用者名と入退室時間を登録してください。')

usrName = st.selectbox(
    '利用者名',
    ['AAAA', 'BBBB', 'CCCC', 'DDDD']
)

minDate = datetime.date(1900, 1, 1)
maxDate = datetime.date(2100, 12, 31)
usageDate = st.date_input('利用日を入力してください。', datetime.date(2024, 4, 1), min_value=minDate, max_value=maxDate)

kisJkn = st.selectbox(
    '入室時間(時)',
    ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
)

kisHun = st.selectbox(
    '入室時間(分)',
    ['00', '15', '30', '45']
)

sryJkn = st.selectbox(
    '退室時間(時)',
    ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
)

sryHun = st.selectbox(
    '退室時間(分)',
    ['00', '15', '30', '45']
)

if st.button('登録'):
    add_data(usrName, usageDate, kisJkn, kisHun, sryJkn, sryHun)
if st.button('履歴'):
    show_data()
# データベースをクローズする
conn.close()