"""
Please code the following problem in Python language.
NAND演算の基本
    Basics of NAND Operation

0 または 1 の整数 A と B が与えられます。 A NAND B の結果を出力してください。
    You are given two integers, A and B, which are either 0 or 1. Please output the result of A NAND B.
ここで、 NAND 演算とは、以下の表にしたがって算出する論理演算のことを指します。
    Here, the NAND operation is logical operation that is calculated according to the following table.
入力1	入力2	出力
0	0	1
0	1	1
1	0	1
1	1	0

入力される値
A B
期待する出力
A NAND B の結果を 0 または 1 で出力してください。
"""

def nand_operation(A, B):
    return 1 if not (A and B) else 0

A, B = map(int, input().split())
nand_operation(A, B)

# ---------
A, B = map(int, input().split())
nand = 1 if not (A and B) else 0
print(nand)
# 実行結果ステータス	Success
# 提出コードのアウトプット	1

# 模範解答--------- 
a, b = map(int, input().split())
print(int(not (a and b)))
# not演算子はbool型で計算されるため、int型に変換する必要がある。

"""
・NAND演算はNot And演算の略、論理積の否定となる。
・ド・モルガンの法則：
    NOT(X AND Y) = NOT(X) OR NOT(Y)
    NOT(X OR Y) = NOT(X) AND NOT(Y)
"""