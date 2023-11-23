# 10行以内の出力

# 数値 N が入力されます。1 から N までの数値をすべて、改行区切りで出力してください。

# 入力される値
# N

# 期待する出力
# 答えの数値を出力してください。
# 1
# 2
# ...
# N

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# * 1 ≦ N ≦ 10

# 入力例2
# 2
# 出力例2
# 1
# 2


n = int(input())
if 1 <= n <= 10:
    for i in range(n):
        print(i + 1)

# or 模範解答
n = int(input())
for i in range(n):
    print(i + 1)