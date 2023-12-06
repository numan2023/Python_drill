"""
標準入力でN行それぞれで文字列が与えられるので、それらを入力して、順にそのままN行で出力してください。

入力される値
1行目でNが与えらます。
続くN行の各行で文字列が与えられます。

期待する出力
N行での出力

入力例1
3
aaaaa
bbbbbb
cccc

出力例1
aaaaa
bbbbbb
cccc
"""

n = int(input())
for i in range(n):
    s = input()
    print(s)