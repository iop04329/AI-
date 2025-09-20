# AI-Stock

1.  **Activate the Virtual Environment:**
    ```bash
    uv init  # init porject (first create project after that no need call)
    uv sync  # install env
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate     # On Windows
    ```

2. **Run app**
    ```bash
    streamlit run main.py
    ```

3. **Knowledge **
    1. google search api 需到[google console](https://console.cloud.google.com) 設定api key
    2. google engine 需要到 [cse.google.com](https://programmablesearchengine.google.com) 設定 engine_id
    3. 上述參考[搜尋引擎教學](https://www.youtube.com/watch?v=Rdt4wDHHHLw)

4. **Debug設置 **
   1. stackoverflow[解決debug](https://stackoverflow.com/questions/60172282/how-to-run-debug-a-streamlit-application-from-an-ide)