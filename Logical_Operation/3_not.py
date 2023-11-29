"""
否定( NOT )の基本

0 または 1 の整数 A が与えられます。 NOT A の結果を出力してください。
ここで、 NOT 演算とは、以下の表にしたがって算出する論理演算のことを指します。
入力	出力
0	1
1	0

入力される値
A
期待する出力
NOT A の結果を 0 または 1 で出力してください。

入力例1
0
出力例1
1

入力例2
1
出力例2
0
"""

"""
The result of the NOT operation with input A=0 is 1.
This follows the logical NOT operation, where the output is the opposite of the input: 1 if the input is 0, and 0 if the input is 1.
"""

def not_operation(A):
    # Logical NOT operation
    return 1 if A == 0 else 0

A = 0
result = not_operation(A)
result

# ---------
A = int(input())
print(1 if A == 0 else 0)
# or
print(int(not A))
# 実行結果ステータス	Success
# 提出コードのアウトプット	1

"""
否定演算子：!, not
not演算子:True or Flaseで結果が出力。
    0 or 1を出力する場合、int型に変換する
"""