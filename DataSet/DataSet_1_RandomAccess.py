# ランダムアクセス
# 配列の指定された場所にアクセス

# 要素数 N の数列 A と数値 M が与えられます。A の M 番目の値を出力してください。

# 入力される値
# N M
# A_1 ... A_N

# 期待する出力
# A の M 番目の値を出力してください。
# A_M

# 入力例1
# 5 2
# 1 2 3 4 5

# 出力例1
# 2



N, M = map(int, input().split())
# Error : A = input()
A = list(map(int, input().split()))

print(A[M - 1])

# or 模範解答
N, M = map(int, input().split())
A = [int(x) for x in input().split()]
print(A[M - 1])