import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

# 描画領域を取得
fig, ax = plt.subplots(1, 1)

# y軸方向の描画幅を指定
ax.set_ylim((-1.1, 1.1))

# x軸:時刻
x = np.arange(0, 100, 0.5)

Hz = 5.

# sin波を取得
y = np.sin(2.0 * np.pi * (x * Hz) / 100)

# グラフを描画する
ax.plot(x, y, color='blue')
plt.show()