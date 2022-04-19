#!/usr/bin/python3
# condig: UTF-8

import matplotlib.pyplot as plt
import pandas as pd
import sys

# read csv file
df = pd.read_csv(sys.argv[1], index_col=0)

# グラフ情報
GRAPHNUM = len(df.columns)  # 数
LABEL = df.columns.values   # 種類

## X軸情報(X軸共通化のため別途定義)
x = df.index.values
# データプロットと表示レイアウト
fig, axis = plt.subplots(GRAPHNUM, sharex=True)  # 複数グラフを表示するときに使う.この場合は縦に2つ並べて、x軸を共有
for i, d in enumerate(df.T.values):
    axis[i].plot(x, d, drawstyle='steps-post', label=LABEL[i])   # データをステップでプロット
    axis[i].set_xticks(x)                                   # ラベル位置指定
    axis[i].set_yticks(d)                                   # ラベル位置指定
    # axis[i].set_ylim(min(d), max(d))                      # y軸範囲設定
    axis[i].spines['right'].set_visible(False)              # 右枠非表示
    axis[i].spines['top'].set_visible(False)                # 上枠非表示
    axis[i].spines['bottom'].set_visible(False)             # 下枠非表示
    axis[i].legend()                                        # 凡例表示
    axis[i].grid(linestyle='--')                            # グリッド線表示
# 縦方向に、間隔を密にグラフをレイアウト
fig.subplots_adjust(hspace=0.1)

# グラフ表示
plt.show()