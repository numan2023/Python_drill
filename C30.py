# n*nの2次元配列の表示

# 自然数 N が入力されます。N 行 N 列の九九表を出力してください。具体的には、出力の i 行 j 列目 (1 ≦ i, j ≦ N ) の数値は i * j になるように出力してください。
# ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

# 入力される値
# N

# 期待する出力
# 答えの数値を出力してください。


# A_{1,1} A_{1,2} A_{1,3} ... A_{1,N}
# A_{2,1} A_{2,2} A_{2,3} ... A_{2,N}
# ...
# A_{N,1} A_{N,2} ... A_{N,N}

n = int(input())
# TypeError: object of type 'int' has no len()

n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n:
            print(i * j)
        else:
            print(i * j, end=" ")