import streamlit as st

def page_2():
    st.title("Page 2")

pg = st.navigation(["page_1.py", page_2],position='top')
pg.run()