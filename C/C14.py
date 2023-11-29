# 入力された10個の文字列を出力

# 10 個の文字列 S_1, S_2, S_3, ..., S_10 が改行区切りで与えられます。
# これらの文字列をすべて、半角スペース区切りで出力してください。

# 入力される値
# S_1
# S_2
# S_3
# ...
# S_10

# 期待する出力
# 答えの文字列を 1 行で出力してください。
# S_1 S_2 S_3 ... S_10

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# * S_i の長さは 1 以上 10 以下
# * S_i は英小文字列

# 入力例1
# q
# bpdi
# u
# ky
# meqt
# rrnc
# co
# jjw
# e
# fwio

# 出力例1
# q bpdi u ky meqt rrnc co jjw e fwio

strings = []

for _ in range(10):
    # 10回の入力を受け取る
    s = input()
    strings.append(s)

# 受け取った文字列を半角スペースで区切って出力
print(" ".join(strings))
# 解説）リスト内の文字列を連結し、結果を出力するための使用
      # stringsは、文字列のリスト：例えば、["hello", "world", "python"]
      # " ".join(strings)の部分は、strings内のすべての文字列を半角スペース" "で連結する。


# or 模範解答

strings = []
for i in range(10):
    strings.append(input())

for i in range(10):
    if i != 9:
        print(strings[i], end=" ")
    else:
        print(strings[i])