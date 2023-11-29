# 半角スペースとバーティカルライン区切りで10個出力

# 10 個の数値が改行区切りで与えられます。これらの数値を半角スペース 2 つとバーティカルライン | 区切りで出力してください。ただし、末尾には改行を出力してください。

# 入力される値
# N1
# N2
# N3
# ...
# N10

# 期待する出力
# 答えの数値を出力してください。
# N1 | N2 | N3 | ... | N10

nums = []
for _ in range(10):
    n = input()
    nums.append(n)

print(" | ".join(nums))

# or 模範解答
for i in range(10):
    if i == 9:
        print(input())
    else:
        print(input(), end=" | ")