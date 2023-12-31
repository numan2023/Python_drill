# 大きな数値の入力

# とても大きな数値 N が与えられます。N をそのまま出力してください。

# 入力される値
# N

# 期待する出力
# N をそのまま出力してください。
# N

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# ・ N は整数
# ・ 0 ≦ N ≦ 10^1,000

# 入力例1
# 813

# 出力例1
# 813

# 入力例2
# 12345678901234567890

# 出力例2
# 12345678901234567890

#int型はメモリが許す限り、非常に大きな数を扱うことができる。
# 多倍長整数
n = int(input())
print(n)

# or 模範解答
print(input())
# 受け取った入力をそのまま出力します。
# 入力値の最大値が 10 の 1,000 乗と非常に大きいため、基本的な整数型を用いるとオーバーフローします。
# そこで、文字列型または多倍長整数を用います。