# 数値をゼロ埋めで出力
# 自然数 N が与えられます。N が 3 けたになるよう数値の前に 0 を埋めて出力してください。

# 入力される値
# N
# 期待する出力
# 答えの数値を出力してください。
# N

# 入力例1
# 12

# 出力例1
# 012

# 入力例2
# 0

# 出力例2
# 000

n = input()
print("{: >03}".format(n))
# -> 0つかず= 12となってしまう


n = input()
print(f"{n:03d}")
# ValueError: Unknown format code 'd' for object of type 'str'


n = str(input())
print(f"{n:03d}")
# ValueError: Unknown format code 'd' for object of type 'str'


# GPT エラーではないが間違い
def print_zero_padded_number(N):
    # Nを3桁の幅でゼロ埋めして出力
    print(f"{N:03d}")

# 入力例1
print_zero_padded_number(12)

# 入力例2
print_zero_padded_number(0)


# or 模範解答
N = input()
print("{:0>3}".format(N))
# 「x桁に右揃えで、足りない部分はiで埋める」は、"{:i>x}"で定義する。