# ITCBOT

這是一個用於DC社團的BOT，可以用來管理社團成員讓社員可以領取身份組，並享受冷掉的披薩。

## 目錄

- 檔案介紹
- 使用方法
- 貢獻
- 授權


## 檔案介紹:
    檔案架構請依照下方縮排去放置，勿隨意更改檔案位置。
```
- 資料夾
        - main.py 主程式，用來啟動機器人。
        - log.py 紀錄執行過的指令。
        - start_pip.txt 是此機器人執行所需的套件清單。
        - config.env 是機器人的設定檔，不可外傳的檔案。
        - version.txt 是版本更新紀錄。
        - 注意事項.txt 是這台機器人的所有注意事項，請先看完再進行動作。
        - data資料夾
            - 是機器人的資料庫，用來儲存機器人所需的資料。
            - students.csv 是全部學生的資料
            - claimed.csv 是已領取過身分組的帳號的資料
- cogs資料夾
            - 是機器人的功能模組，用來儲存機器人所需的功能模組。
            - __pycache__ 資料夾是 Python 編譯器所產生的暫存檔案(請忽略他，可刪可不刪，不影響程式運作(反正程式執行之後他自己會生成出來))
            - game.py 是遊戲的；使用 "%" 作為前綴指令
            - other_commands.py 是其他斜線指令的
            - role_command.py 是領身分組的
            - message_responses.py 是回應訊息的
            - announce.py 是公告的
```
## 使用方法

### 1. 需要先安裝 Python 和 Dcbot。

#### 安裝 Python

請訪問 [Python 官方網站](https://www.python.org/)下載並安裝適合你操作系統的版本。

#### 安裝 Dcbot

你可以使用以下命令來安裝 Dcbot：

```bash
pip install dcbot
```

### 2. 把社團成員名單匯入 **students.csv** 檔案中

### 3. 啟動你的Bot並開始享受冷掉的披薩吧


## 貢獻

特別感謝以下成員對本專案的貢獻：

- **TNCVS ITC 社長 Oscar**
- **TNCVS ITC 副社長 kkallen**

## 授權

![image](https://github.com/user-attachments/assets/1f84bf69-5f7f-4c60-ab54-8d0afb8e97b0)
