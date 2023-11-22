# 代入演算

# 整数 A, B, C が与えられます。以下のアルゴリズムを実行してください。

# 変数 N を 0 で初期化する
# N に A を足した値を N へ代入する
# N に B をかけた値を N へ代入する
# N を C で割ったあまりを N へ代入する
# N を出力する

# 入力される値
# A B C

# 期待する出力
# 計算結果 N を一行で出力してください。末尾に改行を入れ、余計な文字、空行を含んではいけません。
# N

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# ・ A, B, C は整数
# ・ A, B, C は 1 以上 1,000 未満

# 入力例1
# 149 825 262
# 出力例1
# 47

# 入力例2
# 581 938 515
# 出力例2
# 108

a, b, c = map(int, input().split(" "))
n = 0
n += a
n *= b
n %= c
print(n)