"""
標準入力で3つの文字列が1行で与えられるので、それらを入力して、順にそのまま3行で出力してください。

入力される値
3つの文字列が半角スペース区切りで1行で与えれます。

期待する出力
3行での出力

入力例1
aaaaa bbbbbb cccc

出力例1
aaaaa
bbbbbb
cccc
"""

a, b, c = input().split()
print(a)
print(b)
print(c)

# 模範解答
a = input().split()

for i in a:
    print(i)