# 要素数 N の数列 A と要素数 Q の数列 B が与えられます。 1 ≦ i ≦ Q の各 i について、i 行目に A の B_i 番目の値を出力してください。

# 入力される値
# N
# A_1 A_2 ... A_N
# Q
# B_1 B_2 ... B_Q

# 期待する出力
# Q 行出力してください。
# i 行目には、A の B_i 番目の値を出力してください。
# A_{B_1}
# ...
# A_{B_Q}

# 入力例1
# 5
# 10 20 30 40 50
# 3
# 2 4 1

# 出力例1
# 20
# 40
# 10


N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
B = [int(x) for x in input().split()]

for i in range(Q):
    print(A[B[i] - 1])

# or 模範解答
N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
B = [int(x) for x in input().split()]

for i in range(Q):
    print(A[B[i]-1])