# 数値を異なる長さで2行出力

# 自然数 N, M が与えられます。1 行目には 1 以上 N 以下の数値を半角スペース区切りで出力してください。また、2 行目には 1 以上 M 以下の数値を半角スペース区切りで出力してください。
# さらに、各行の末尾には、半角スペースの代わりに改行を入れてください。

# 入力される値
# N M

# 期待する出力
# 答えの数値を出力してください。
# 1 2 3 ... N
# 1 2 3 ... M

n, m = map(int, input().split())
for i in range(1, n + 1):
    if i == n:
        print(i)
    else:
        print(i, end=" ")

for i in range(1, m + 1):
    if i == m:
        print(i)
    else:
        print(i, end=" ")

values = input().split()
N = int(values[0])
M = int(values[1])

for i in range(1, N + 1):
    if i == N:
        print(i)
    else:
        print(i, end=" ")

for i in range(1, M + 1):
    if i == M:
        print(i)
    else:
        print(i, end=" ")