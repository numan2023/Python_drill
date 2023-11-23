# カンマ区切りで10個出力

# 10 個の数値が半角スペース区切りで与えられます。これらの数値をカンマ区切りで出力してください。
# ただし、末尾にはカンマではなく改行を出力してください。

# 入力される値
# N1 N2 N3 ... N10

# 期待する出力
# 答えの数値を出力してください。
# N1,N2,N3,...,N10


nums = input().split()
for num in nums:
    if num != nums[9]:
        print(num, end=",")
    else:
        print(num)

# or 模範解答
S = input().split()
print(",".join(S))