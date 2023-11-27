# # 割り算

# # 下記の問題をプログラミングしてみよう！
# # 整数 A = 437,326、 B = 9,085 とします。以下の二つの演算の結果を半角スペース区切りで出力してください。

# # 1. A を B で割った商
# # 2. A を B で割った余り

# 入力される値
# ありません

# 期待する出力
# A を B で割った商を X、A を B で割った余りを Y としたとき、X と Y を半角スペース区切り一行で出力してください。末尾に改行を入れ、余計な文字、空行を含んではいけません。
# X Y

A = 437326
B = 9085
X = A // B
Y = A % B
print("{} {}".format(X, Y))