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

# 課題9-1: HTMLページを返す
@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>My Homepage</title>
        </head>
        <body>
            <h1>ようこそ！</h1>
            <p>こんにいちは</p>
            <p>最近暑すぎて死にそうです</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# 課題9-2: クリスマスプレゼントのPOST
@app.post("/present")
async def give_present(present: str = Query(...)):
    return {
        "response": f"サンタです🎅 メリークリスマス！『{present}』ありがとう。お返しは🍬キャンディーです！"
    }