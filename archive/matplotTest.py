# -*- coding: utf-8 -*-
"""
matplotlibでリアルタイムプロットする例

無限にsin関数をplotし続ける
"""
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots(1, 1)
    # x = np.arange(-np.pi, np.pi, 0.1)
    x = np.arange(0, 1, 0.1)
    # y = np.sin(x)
    y = np.zeros(10)
    i = 0
    # 初期化的に一度plotしなければならない
    # そのときplotしたオブジェクトを受け取る受け取る必要がある．
    # listが返ってくるので，注意
    lines, = ax.plot(x, y)

    # ここから無限にplotする
    while True:
        # plotデータの更新
        x += 0.1
        print(x)
        # y = np.sin(x)
        i += 1
        y = np.append(y, i)
        y = np.delete(y, 0)
        print(y)
        # 描画データを更新するときにplot関数を使うと
        # lineオブジェクトが都度増えてしまうので，注意．
        # 一番楽なのは上記で受け取ったlinesに対して
        # set_data()メソッドで描画データを更新する方法．
        lines.set_data(x, y)

        # set_data()を使うと軸とかは自動設定されないっぽいので，
        # 今回の例だとあっという間にsinカーブが描画範囲からいなくなる．
        # そのためx軸の範囲は適宜修正してやる必要がある．
        ax.set_xlim((x.min(), x.max()))

        # 一番のポイント
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # ----> plt.pause(interval) これを使う!!! 引数はsleep時間
        plt.pause(.1)

        # except KeyboardInterrupt:
        #     break

if __name__ == "__main__":
    main()






# import numpy as np
# from matplotlib import pyplot as plt
# import random

# t = np.zeros(100)
# y = np.zeros(100)

# plt.ion()
# plt.figure()
# li, = plt.plot(t, y)
# plt.ylim(0, 5)
# plt.xlabel("time[s]")
# plt.ylabel("Voltage[V]")

# data = random.random()
# tInt = float(data)

# while True:
#     try:
#         data = random.random()
#         data2 = random.random()
#         # 配列をキューと見たてて要素を追加・削除
#         t = np.append(t, data)
#         t = np.delete(t, 0)
#         y = np.append(y, data2)
#         y = np.delete(y, 0)

#         li.set_xdata(t)
#         li.set_ydata(y)           
#         plt.xlim(min(t), max(t))
#         plt.draw()

#     except KeyboardInterrupt:
#         break
#####
# import numpy as np
# import matplotlib.pyplot as plt
 
# #一旦ここでグラフを描画。
# step = np.random.choice([-1,1],500)
# arr = np.cumsum(step)
# x = np.arange(0, 500, 1)
# plt.figure(figsize=(10,6))
# lines, = plt.plot(x, arr) #グラフオブジェクトを受け取る
 
# #1秒ごとに再描画
# #set_dataメソッドで描画データを更新する
# while True:
#     step = np.random.choice([-1,1],500)
#     arr = np.cumsum(step)
#     lines.set_data(x, arr) #データ更新
#     plt.ylim([arr.min()-1,arr.max()+1])
#     plt.pause(1)