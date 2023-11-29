# 1つの実数を出力
# 実数 N、自然数 M が入力されます。N を丸めて小数第 M 位まで出力してください。
# また、N の小数部が小数第 M 位に満たない場合は 0 で埋めて出力してください。

# 入力される値
# N M

# 期待する出力
# 答えの数値を出力してください。
# N

# 入力例1
# 0.813 1

# 出力例1
# 0.8

# 入力例2
# 0.813 2

# 出力例2
# 0.81

# GPT
def round_to_specific_decimal_input():
    # 実数 N と 自然数 M を入力として受け取る
    N, M = input().split()
    N = float(N)
    M = int(M)

    # 実数Nを小数第M位まで丸めて出力
    format_string = f"{{:.{M}f}}"
    return format_string.format(N)

# 入力を受け取って関数を実行する
print(round_to_specific_decimal_input())

# or 模範解答
values = input().split()
N = float(values[0])
M = int(values[1])

print("{:.{}f}".format(N, M))