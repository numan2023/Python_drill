"""
Please code the following problem in Python.
論理和( OR )の基本
    Basic of Logical OR

0 または 1 の整数 A と B が与えられます。 
    Given are two integers A and B, which are either 0 or 1.
A OR B の結果を出力してください。
    Output the result of A OR B.
ここで、 OR 演算とは、以下の表にしたがって算出する論理演算のことを指します。
    Here, the OR operation is a logical operation calculated according to the table below:
入力1	入力2	出力
0	0	0
0	1	1
1	0	1
1	1	1

入力される値
A B
期待する出力
A OR B の結果を 0 または 1 で出力してください。

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
The result of the OR operation with inputs A = 1 and B = 0 is 1.
This follows the logical OR operation where the output is 1 if either of the inputs is 1; otherwise, the output is 0.
"""

def or_operation(A, B):
    # Logical OR operation
    return A | B

A = 1
B = 0

result = or_operation(A, B)
result

# ------------
A, B = map(int, input().split())
print(A | B)
print(A or B)
# 実行結果ステータス	Success
# 提出コードのアウトプット	0

"""
論理積：| , || , or
"""