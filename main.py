import streamlit as st
from custom_pages import dashboard, home, setting
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    # 側邊欄導航
    page = st.sidebar.selectbox("選擇頁面", ["首頁", "報表", "設定"])
    if page == "首頁":
        home.homePage()
    elif page == "報表":
        dashboard.dashboardPage()
    elif page == "設定":
        setting.settingPage()


if __name__ == "__main__":
    main()
