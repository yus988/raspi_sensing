# -*- coding:utf-8 -*-
import tkinter

start_flag = False

# タイマー
def timer(count):
    global label, app
    global start_flag

    if start_flag and count <= 10:
        label.config(text=count)
        app.after(1000, timer, count + 1)

# スタートボタンが押された時の処理
def start_button_click(event):
    global app
    global start_flag
    start_flag = True

    app.after(0, timer, 1)

# ストップボタンが押された時の処理
def stop_button_click(event):
    global start_flag
    start_flag = False

# メインウィンドウを作成
app = tkinter.Tk()
app.geometry("200x100")

# ボタンの作成と配置
start_button = tkinter.Button(
    app,
    text="スタート",
)
start_button.pack()

stop_button = tkinter.Button(
    app,
    text="ストップ",
)
stop_button.pack()


# ラベルの作成と配置
label = tkinter.Label(
    app,
    width=5,
    height=1,
    text=0,
    font=("", 20)
)
label.pack()

# イベント処理の設定
start_button.bind("<ButtonPress>", start_button_click)
stop_button.bind("<ButtonPress>", stop_button_click)

# メインループ
app.mainloop()