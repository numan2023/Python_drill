"""
排他的論理和( XOR )の基本
    Basics of Exclusive OR(XOR)

0 または 1 の整数 A と B が与えられます。A XOR B の結果を出力してください。
ここで、 XOR 演算とは、以下の表にしたがって算出する論理演算のことを指します。
入力1	入力2	出力
0	0	0
0	1	1
1	0	1
1	1	0

入力される値
A B
期待する出力
A XOR B の結果を 0 または 1 で出力してください。

入力例1
0 0
出力例1
0

入力例2
0 1
出力例2
1
"""

"""
The result of the XOR operation with inputs A=1 and B =1 is 0.
This follows the logical XOR operation where the output is 1 if the inputs are different (0 and 1 or 1 and 0) and 0 if the inputs are the same (both 0 or both 1).
"""

def xor_operation(A, B):
    return A ^ B

A = 1
B = 1
result = xor_operation(A, B)
result

# --------
A, B = map(int, input().split())
print(A ^ B)

"""
排他的論理和：^, xor
排他的論理和：2つの条件P,Qの片方だけが真であるとき、結果が真になる論理演算
排他的論理和は、and演算、or演算、not演算だけで計算することもできる
X XOR Y = (X AND NOT(Y)) OR (NOT(X) AND Y)
    ※注意点）not演算子はbool型で計算、そのためxor関数にてint型で受け取ったx、yはnot演算後bool型に変換されてしまう。
"""