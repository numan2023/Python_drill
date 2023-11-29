# 出力幅を指定して出力
# N個の数値をM桁半角スペース埋めで出力

# 自然数 N, M と N 個の自然数 A_1, A_2, ..., A_N が与えられます。それぞれの数値が M けたになるよう数値の前に半角スペースを埋めて、改行区切りで出力してください。

# 入力される値
# N M
# A_1
# A_2
# A_3
# ...
# A_N

# 期待する出力
# 答えの数値を解答の形式に従った形で出力してください。


# A_1
# A_2
# A_3
# ...
# A_N

# 入力例1
# 4 3
# 0
# 8
# 81
# 813

# 出力例1
# 0
# 8
# 81
# 813

n, m = map(int, input().split())

for i in range(n):
    a = input()
    print("{: >{}}".format(a, m))

# or 模範解答
values = input().split()
N = int(values[0])
M = int(values[1])

for _ in range(N):
    a = int(input())
    
    print("{: >{}}".format(a, M))