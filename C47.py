# 文字列とN個の整数の出力

# 自然数 N, A, B が与えられます。(A, B) という形式の文字列を N 回、カンマと半角スペース区切りで出力してください。

# 入力される値
# N A B

# 期待する出力
# 答えの文字列を出力してください。


# (A_1, B_1), (A_2, B_2), ... , (A_N, B_N)

# 入力例1
# 3 10 99

# 出力例1
# (10, 99), (10, 99), (10, 99)

#----------
N, A, B = map(int, input().split())

for _ in range(N):
    print("({}, {}),".format(A, B), end="")

# Wrong Answer
# (10, 99),(10, 99),(10, 99),
#----------

N, A, B = map(int, input().split())

for i in range(N):
    if i != N - 1:
        print("({}, {}),".format(A, B), end=" ")
    else:
        print("({}, {})".format(A, B))

# Success
# (10, 99), (10, 99), (10, 99)
# ---------------------------------

# or 模範解答
values = input().split()
N = int(values[0])
A = int(values[1])
B = int(values[2])

for i in range(N):
    if i < N - 1:
        print("({}, {})".format(A, B), end=", ")
    else:
        print("({}, {})".format(A, B))