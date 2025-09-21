import streamlit as st
from ai.analyze import analyze_run
from ai.analyze_model import StockAnalysis
from tool.finance import get_stock_name

def analyzePage():
    # 頁面設定
    st.set_page_config(page_title="AI 市場情緒分析助理", layout="wide")

    # 側邊欄設定
    with st.sidebar:
        st.title("AI 市場情緒分析助理")

        # 股票代號輸入
        stock_symbol = st.text_input("請輸入股票代號 (如：AAPL, NVDA)", value="NVDA")
        
        # 股票新聞搜尋分析
        stock_name = st.text_input("股票文章搜尋 (如：台積電)", value="台積電")

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

    # 執行分析
    if analyze:
        # if not stock_symbol or not openai_api_key:
        if not stock_symbol or not stock_name:
            st.error("請完整填寫股票代號")
        else:
            ticker_name = get_stock_name(ticker_symbol=stock_symbol)
            if not ticker_name:
                st.error("查無此股票代號，請確認後重新輸入")
            else:
                with st.status("AI 分析中，請稍候...", expanded=True) as status:
                    res = analyze_run(stock_name=stock_name)
                    try:
                        analyze_result:StockAnalysis = StockAnalysis.model_validate_json(res.content)
                    except Exception as e:
                        print('AI分析後解構失敗')
                        analyze_result = None
                    status.update(label="分析完成 ✅", state="complete", expanded=False)
                if analyze_result is not None:
                    # ✅ 按下分析後顯示的內容，你可自行補上邏輯與視覺化
                    st.subheader("一、股價趨勢圖")
                    st.markdown(f"**{stock_symbol} 股價走勢**（此區域預留給圖表）")

                    st.markdown("### 二、事件分析結果")
                    st.markdown("此處可呈現 ChatGPT 對近期新聞與財報的情緒總結")

                    st.markdown("### 三、技術指標分析")
                    st.markdown("此處可顯示均線、MACD、KD 等指標結果")
                    
                    st.title("AI 分析結果")
                    st.subheader("分析總結")
                    st.markdown(analyze_result.AI分析總結)

                    st.subheader("媒體情緒觀察")
                    st.markdown(analyze_result.媒體情緒觀察)

                    st.subheader("短期分析")
                    st.markdown(analyze_result.短期分析)

                    st.subheader("中長期分析")
                    st.markdown(analyze_result.中長期分析)

                    # 詳細新聞列表可折疊
                    with st.expander("詳細新聞列表"):
                        for item in analyze_result.詳細新聞列表:
                            st.markdown(f"- [{item.文章名稱}]({item.文章連結})")

    else:
        # ✅ 預設空白（還沒分析時）
        st.markdown("請在左側輸入股票代號與 API Key，並點選 **開始分析**")