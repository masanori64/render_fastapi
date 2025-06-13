from typing import Optional
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# Hello World エンドポイント（元に戻したバージョン）
@app.get("/")
async def root():
    return {"message": "Hello World"}

# おみくじ API
@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉", "中吉", "小吉", "吉", "半吉",
        "末吉", "末小吉", "凶", "小凶", "大凶"
    ]
    return {"result": random.choice(omikuji_list)}

# 課題9-1: HTMLを返すエンドポイント
@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>FastAPI Index Page</title>
        </head>
        <body>
            <h1>Hello! This is your homepage.</h1>
            <p>課題9-1のHTML出力テストです。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# 課題9-2: POSTでクエリパラメータを受け取り、メッセージを返す
@app.post("/present")
async def present(present: str = Query(...)):
    return {
        "response": f"サーバーです。メリークリスマス！{present}ありがとう。お返しはキャンディーです。"
    }
