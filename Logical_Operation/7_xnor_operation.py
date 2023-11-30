"""
XNOR演算の基本

0 または 1 の整数 A と B が与えられます。 A XNOR B の結果を出力してください。 ここで、 XNOR 演算とは、以下の表にしたがって算出する論理演算のことを指します。
入力1	入力2	出力
0	0	1
0	1	0
1	0	0
1	1	1

入力される値
A B
期待する出力
A XNOR B の結果を 0 または 1 で出力してください。
"""

def xnor_oparation(A, B):
    return 1 if A == B else 0

A, B = map(int, input().split())
xnor_operation(A, B)

# ---------
A, B = map(int, input().split())
xnor = 1 if A == B else 0
print(xnor)

# 模範解答 ---------
a, b = map(int, input().split())
print(int(not (a ^ b)))

"""
・XNOR演算はNOT XNOR演算の略、XOR演算を計算した後に、not演算を行う演算。
X XNOR Y
  = NOT(X XOR Y)
  = NOT((X AND NOT(Y)) OR (NOT(X) AND Y))  //Xが真かつYが偽であるときに式全体が真になる論理式。つまりX または Yのうち、どちらか一方のみが真であれば結果が真になるというXOR演算の論理式。
  = NOT(X AND NOT(Y)) AND NOT(NOT(Y) AND Y)  //全体に対してドモルガンんも法則を適用
  = (NOT(X) OR Y) AND (X OR NOT(Y))

X XNOR Y
  = (入力値が両方0の時だけ結果が真になる演算) or (入力値が両方1の時だけ結果が真になる演算)
  = ( (NOT X) AND (NOT Y) ) OR (X AND Y)
"""