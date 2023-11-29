# 入力された10個の文字列を出力

# 10 個の文字列 S_1, S_2, S_3, ..., S_10 が半角スペース区切りで与えられます。
# これらの文字列をすべて、改行区切りで出力してください。

# 入力される値
# S_1 S_2 S_3 ... S_10
# 入力値最終行の末尾に改行が１つ入ります。

# 期待する出力
# 答えの文字列を 10 行で出力してください。
# S_1
# S_2
# S_3
# ...
# S_10
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# * S_i の長さは 1 以上 1,000 以下
# * S_i は英小文字列

# 入力例1
# a a a a a a a a a a

# 出力例1
# a
# a
# a
# a
# a
# a
# a
# a
# a
# a

# 文字列を入力として受け取る
input_string = input()

# 半角スペースで区切られた文字列をリストに分割
strings = input_string.split()

# 各文字列を改行で区切って出力
for s in strings:
    print(s)


# or 模範解答
strings = input().split()
for s in strings:
    print(s)


# その他条件を考慮したコード
strings = input().split()
for s in strings:
    if 1 <= len(s) <= 1000 and s.islower():
        print(s)