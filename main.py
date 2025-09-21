import streamlit as st
from custom_pages import analyze, home, setting
import os
from dotenv import load_dotenv

from custom_pages.router_enum import RouterEnum

def main():
    load_dotenv()
    # 取得 URL query 參數
    query_params = st.query_params    
    current_page = query_params.get("page", RouterEnum.home.name)
    
    # 側邊欄導航
    cnPages = [p.val for p in RouterEnum]
    enPages = list(RouterEnum.__members__)
    # 找到當前頁面對應的 index
    current_index = enPages.index(current_page) if current_page in enPages else 0
    selectCNPage = st.sidebar.selectbox("選擇頁面", cnPages, index=current_index)
    selectPageEnum = RouterEnum.first_where(lambda e: e.val == selectCNPage, default=RouterEnum.home)
    selectPage = selectPageEnum.name
    
    # 更新 URL
    # if selectPage != current_page:
    #     st.query_params = {"page": selectPage}  # ✅ 新版寫法
    # 根據 page 執行對應函式
    if selectPage == RouterEnum.home.name:
        home.homePage()
    elif selectPage == RouterEnum.analyze.name:
        analyze.analyzePage()
    elif selectPage == RouterEnum.setting.name:
        setting.settingPage()
    

if __name__ == "__main__":
    main()
