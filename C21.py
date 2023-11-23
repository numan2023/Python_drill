# バーティカルライン区切りで3つの文字列を出力

# 3 つの文字列が改行区切りで与えられます。
# これらの文字列をバーティカルライン | 区切りで出力してください。

# 入力される値
# S1
# S2
# S3

# 期待する出力
# 答えの数値を出力してください。
# S1|S2|S3

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# * すべての文字列の長さは 1 以上 10 以下
# * すべての文字列は英小文字からなる

s1 = input()
s2 = input()
s3 = input()

strings = []
strings.append(s1)
strings.append(s2)
strings.append(s3)

print("|".join(strings))

# or 模範解答
S1 = input()
S2 = input()
S3 = input()
print("{}|{}|{}".format(S1, S2, S3))