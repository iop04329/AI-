import streamlit as st

def home_page():
    # 頁面設定
    st.set_page_config(page_title="AI 市場情緒分析助理", layout="wide")

    # 側邊欄設定
    with st.sidebar:
        st.title("AI 市場情緒分析助理")

        # 股票代號輸入
        stock_symbol = st.text_input("請輸入股票代號 (如：AAPL, NVDA)", value="NVDA")

        # API Key 輸入（支援隱藏/顯示）
        st.markdown("### API 設定")
        data_api_key = st.text_input("Data API Key", type="password")
        openai_api_key = st.text_input("OpenAI API Key", type="password")

        # 分析按鈕
        analyze = st.button("🔍 開始分析")

        # 免責聲明
        st.markdown("---")
        st.markdown("#### 📢 免責聲明")
        st.markdown(
            """
            本系統提供的資料與分析結果僅供參考，\
            並不構成任何投資建議。投資有風險，請審慎評估自身風險承受能力，\
            如有需要請諮詢專業投資顧問。
            """
        )

    # 右側主頁面內容
    st.title("AI 市場情緒分析助理")

    if analyze:
        # ✅ 按下分析後顯示的內容，你可自行補上邏輯與視覺化
        st.subheader("一、股價趨勢圖")
        st.markdown(f"**{stock_symbol} 股價走勢**（此區域預留給圖表）")

        st.markdown("### 二、事件分析結果")
        st.markdown("此處可呈現 ChatGPT 對近期新聞與財報的情緒總結")

        st.markdown("### 三、技術指標分析")
        st.markdown("此處可顯示均線、MACD、KD 等指標結果")

    else:
        # ✅ 預設空白（還沒分析時）
        st.markdown("請在左側輸入股票代號與 API Key，並點選 **開始分析**")