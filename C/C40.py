# 実数をフォーマット指定して出力：複数の実数を出力

# 自然数 Q が与えられます。Q 回以下の問題に答えてください。

# * 実数 N、自然数 M が入力されます。N を丸めて小数第 M 位まで出力してください。また、N の小数部が小数第 M 位に満たない場合は 0 で埋めて出力してください。

# 入力される値
# Q
# N_1 M_1
# N_2 M_2
# ...
# N_Q M_Q

# 期待する出力
# 答えの数値を出力してください。


# Ans1
# Ans2
# ...
# Ans_Q

# 入力例1
# 4
# 0.813 1
# 0.813 2
# 0.813 3
# 0.813 4

# 出力例1
# 0.8
# 0.81
# 0.813
# 0.8130

def round_and_format_numbers(Q, numbers):
    for N, M in numbers:
        # 実数Nを小数第M位まで丸めて出力
        format_string = f"{{:.{M}f}}"
        print(format_string.format(N))

# 入力例
Q_example = 4
numbers_example = [
    (0.813, 1),
    (0.813, 2),
    (0.813, 3),
    (0.813, 4)
]

round_and_format_numbers(Q_example, numbers_example)

# or 模範解答
Q = int(input())

for _ in range(Q):
    values = input().split()
    n = float(values[0])
    m = int(values[1])

    print("{:.{}f}".format(n, m))