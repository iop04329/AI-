

def read_txt_file(filepath: str, encoding: str = 'utf-8') -> str:
    """
    讀取包含中文的 txt 檔案內容。

    :param filepath: 檔案路徑
    :param encoding: 檔案編碼，預設為 utf-8，可改為 big5 等
    :return: 檔案內容的字串
    """
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            content = f.read()
        return content
    except UnicodeDecodeError:
        print(f"❌ 讀取失敗，可能不是 {encoding} 編碼。可嘗試改用其他編碼（例如 big5）")
        raise
    except FileNotFoundError:
        print("❌ 檔案未找到，請確認路徑正確")
        raise