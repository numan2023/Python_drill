# 数値をM桁半角スペース埋めで出力
# 自然数 N, M が与えられます。N が M けたになるよう数値の前に半角スペースを埋めて出力してください。

# 入力される値
# N M

# 期待する出力
# 答えの数値を解答の形式に従った形で出力してください。
# N

# 入力例1
# 813 4

# 出力例1
# 813

n, m = map(int, input().split())

print("{: >{}}".format(n, m))

# or 模範解答
values = input().split()
N = int(values[0])
M = int(values[1])

print("{: >{}}".format(N, M))