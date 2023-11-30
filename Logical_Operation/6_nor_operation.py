"""
NOR演算の基本

0 または 1 の整数 A と B が与えられます。 A NOR B の結果を出力してください。
ここで、 NOR 演算とは、以下の表にしたがって算出する論理演算のことを指します。
入力1	入力2	出力
0	0	1
0	1	0
1	0	0
1	1	0

入力される値
A B
期待する出力
A NOR B の結果を 0 または 1 で出力してください。
"""

def nor_operation(A, B):
    return 1 if not(A or B) else 0

A, B = map(int, input().split())
nor_operation(A, B)

# ---------
A, B = map(int, input().split())
nor = 1 if not(A or B) else 0
print(nor)

# 模範解答 ------------
a, b = map(int, input().split())
print(int(not (a or b)))
"""
・NOR演算はNOT OR演算の略で、論理和の否定
・ド・モルガンの法則
    NOT(X OR Y) = NOT(X) AND NOT(Y)
"""
