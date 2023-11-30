"""
半加算器
    Half Adder

京子ちゃんは 二進数 1 けたの整数 A と B を使って、 A + B を計算したいと思っています。
https://i.gyazo.com/e648d1c63ac63b8d38c98684e4521ebf.png
    Kyoko wants to calculate A + B using two binary digits, integers A and B.
A + B = C S (Cが2桁目(Carry), Sが1桁目(Sum))
    A + B = CS(where C is the second digit (carry), S is the first digit(sum))
A と B を足した結果 (2 進表記) の下から 2 けた目の値を C 、下から 1 けた目の値を S とします。 C と S を出力してください。
    Let C be the second digit from the bottom and S be the first digit from the bottom in the binary representation of the result of A + B. Please output C and S.

入力される値
A B
期待する出力
C, S をこの順に、半角スペース区切りで出力してください。
C S

入力例1
0 1
出力例1
0 1

入力例2
1 1
出力例2
1 0
"""

def half_adder(A, B):
    # calculate sum and carry
    sum = A ^ B # sum is XOR of A and B
    carry = A & B # carry is AND of A and B
    return carry, sum

A, B = map(int, input().split())
half_adder(A, B)

# ---------
A, B = map(int, input().split())
sum = A ^ B
carry = A & B
print(A, B)
# 実行結果ステータス	Success
# 提出コードのアウトプット	0 1

# 模範解答 -------
a, b = map(int, input().split())

c = a & b
s = a ^ b

print(c ,s)

"""
まず、 C について考えましょう。 C は A と B が両方とも 1 のときだけ 1 になります。これは、以下の表のように AND 演算の結果と等しいです。つまり、 C = A AND B となります。
A	B	C
0	0	0
0	1	0
1	0	0
1	1	1

次に S について考えます。 S は A と B のどちらか一方のみ 1 のときだけ 1 になります。これは、以下の表のように XOR 演算の結果と等しいです。つまり、 S = A XOR B となります。
A	B	S
0	0	0
0	1	1
1	0	1
1	1	0

半加算器は簡易的な論理回路図で表現すると以下の通り
https://i.gyazo.com/0e0f51f36a0205fdb7002633ecdad0b7.png
"""