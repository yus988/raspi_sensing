# -*- coding: utf-8 -*-
import datetime
import csv

dt_now = datetime.datetime.now()
filename = "./csv/" + dt_now.strftime("%m-%d_%H-%M-%S") + ".csv"
print(dt_now.strftime("%m%d_%H-%M-%S"))

# ファイルオープン
f = open(filename, "w")
writer = csv.writer(f, lineterminator="\n")

# データをリストに保持
csvlist = []
# csvlist.append("hoge")
# csvlist.append("fuga")

csvlist.append([2,3,4])
csvlist.append([2,4,5])

# 出力
writer.writerows(csvlist)

# ファイルクローズ
f.close()