"""
論理積( AND )の基本

0 または 1 の整数 A と B が与えられます。
    Given are two integers A and B, which are either 0 or 1.
A AND B の結果を出力してください。
    Output the result of A AND B.
ここで、 AND 演算とは、以下の表にしたがって算出する論理演算のことを指します。
    Here, the AND operation is a logical operation calculated according to the table below:
入力1	入力2	出力
0	0	0
0	1	0
1	0	0
1	1	1

入力される値
  Input values:
A B
期待する出力
    Expected output:
A AND B の結果を 0 または 1 で出力してください。
    Output the result of A AND B as either 0 or 1.

入力例1
0 0
出力例1
0

入力例2
0 1
出力例2
0
"""

"""
The result of the AND operation with inputs A = 0 and B = 1 is 0.
This follows the logical AND operation where the output is only 1 if both inputs are 1; otherwise, the output is 0.
"""

def and_operation(A, B):
    # Logical AND operation
    return A & B

# Example input values
A = 0
B = 1

# Output the result of A AND B
result = and_operation(A, B)
result

# ------------

A, B = map(int, input().split())
print(A & B)
print(A and B)
# 実行結果ステータス	Success
# 提出コードのアウトプット	0

"""
ポイント
    ・論理積：&, &&, and
"""