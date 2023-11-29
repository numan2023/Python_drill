# 複数の数値を半角スペース埋めで出力
# 自然数 N が与えられます。N 個の自然数が与えられるので、それぞれを数値 M_i について以下の処理を行ってください。
# * M_i が 3 けたになるよう数値の前に半角スペースを埋めて出力してください。

# 入力される値
# N
# M_1
# M_2
# M_3
# ...
# M_N

# 期待する出力
# 答えの数値を解答の形式に従った形で出力してください。
# M_1
# M_2
# M_3
# ...
# M_N

# 入力例1
# 12
# 0
# 8
# 81
# 813
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0

# 出力例1
# 0
# 8
# 81
# 813
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0


n = input()

for i in range(n):
    m = input()
    print("{: >3}".format(m))
# TypeError: 'str' object cannot be interpreted as an integer
  # 文字列型のオブジェクトが整数型として扱われようとした時に発生。Pythonでは、input()関数は常に文字列を返すため、数値として扱うには、明示的に型変換が必要。
    # n = input()はstr型 -> range(n)には整数が必要。
    # ※ mの方はstrで問題なし！（模範解答確認） <- m = input()も文字列型。フォーマット指定子`{: >3}`は数値のためのもの、mを整数に変換する。

# -> 修正版
n = int(input())

for i in range(n):
    m = int(input())
    print("{: >3}".format(m))


# or 模範解答
N = int(input())

for _ in range(N):
    m = input()

    print("{: >3}".format(m))