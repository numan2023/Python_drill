# 数行の出力

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
# * 1 ≦ N ≦ 5


n = int(input())
if 1 <= n <= 5:
    for i in range(n):
        print(i + 1)
# for i in n:
# TypeError: 'int' object is not iterable(イテラブル・イテレータ＝繰り返す)

# or 模範解答

N = int(input())

if N >= 1:
    print(1)
if N >= 2:
    print(2)
if N >= 3:
    print(3)
if N >= 4:
    print(4)
if N == 5:
    print(5)