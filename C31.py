# N個の文字を半分ずつ出力

# 偶数 N が入力されます。まず、 1 行目には 1 以上 N / 2 以下の数値を半角スペース区切りですべて出力してください。次に、 2 行目には N / 2 + 1 以上 N 以下の数値を半角スペース区切りですべて出力してください。
# 各行の末尾には、半角スペースの代わりに改行を入れてください。

# 入力される値
# N

# 期待する出力
# 答えの数値を出力してください。
# 1 2 3 ... N/2
# N/2+1 N/2+2 ... N

# 入力例1
# 8

# 出力例1
# 1 2 3 4
# 5 6 7 8

n = int(input())

# TypeError: 'float' object cannot be interpreted as an integer
# n_1 = n / 2
n_1 = int(n / 2)

for i in range(1, n_1 + 1):
    if i == n_1:
        print(i)
    else:
        print(i, end=" ")

for i in range(n_1 + 1, n + 1):
    if i == n:
        print(i)
    else:
        print(i, end=" ")

# or 模範解答
N = int(input())
for i in range(1, N + 1):
    if i % (N // 2) == 0:
        print(i)
    else:
        print(i, end= " ")

+a            # 正数
-a            # 負数
a + b         # 加算
a - b         # 減算
a * b         # 乗算
a / b         # 除算
a % b         # a を b で割った余り
a ** b        # a の b 乗
a // b        # 切り捨て除算