# 3*3の出力

# 9 個の数値が半角スペース区切りで入力されます。この数値を 3 行 3 列の形式で出力してください。
# 具体的には、入力された数値を N_1 , N_2 , N_3 , ..., N_9 とするとき、 1 行目にはN_1 からN_3 を、2 行目には N_4 から N_6 を、3 行目には N_7 から N_9 を出力してください。
# ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

# 入力される値
# N_1 N_2 N_3 ... N_9

# 期待する出力
# 答えの数値を出力してください。
# N_1 N_2 N_3
# N_4 N_5 N_6
# N_7 N_8 N_9

## GPT解答
# 入力された数値を受け取り、空白で分割して数値のリストに変換
numbers = list(map(int, input().split()))

# 与えられた数字を3行3列の形式で出力
for i in range(0, 9, 3):
    print(" ".join(map(str, numbers[i:i+3])))

# or 模範解答
N = input().split()

for i in range(len(N)):
    print(N[i], end="")
    if i % 3 == 2:
        print()
    else:
        print(" ", end="")


## ------------------------------------------
# range関数の使い方
  # 連番を生成してfor文で使ったり、そのリストを取得するためにrange()を使う。

for i in range(3):
    print(i)
# 0
# 1
# 2

print(list(range(3)))
# [0, 1, 2]

print(list(range(3, 10)))
# [3, 4, 5, 6, 7, 8, 9]

print(list(range(10, 3)))
# []

print(list(range(-3, 3)))
# [-3, -2, -1, 0, 1, 2]

print(list(range(3, 10, 2)))
# [3, 5, 7, 9]

print(list(range(10, 3, 2)))
# []

print(list(range(10, 3, -2)))
# [10, 8, 6, 4]

print(list(range(3, 10, -2)))
# []

print(range(3, 10, 1) == range(3, 10))
# True

print(range(0, 10, 1) == range(0, 10) == range(10))
# True


print(list(range(3, 10, 2)))
# [3, 5, 7, 9]

print(list(range(9, 2, -2)))
# [9, 7, 5, 3]

print(list(reversed(range(3, 10, 2))))
# [9, 7, 5, 3]

for i in reversed(range(3, 10, 2)):
    print(i)
# 9
# 7
# 5
# 3

## リスト内包表記の基本型
# [式 for 任意の変数名 in イテラブルオブジェクト]
squares = [i**2 for i in range(5)]
print(squares)
# [0, 1, 4, 9, 16]
squares = []
for i in range(5):
    squares.append(i**2)

print(squares)
# [0, 1, 4, 9, 16]


# [式 for 任意の変数名 in イテラブルオブジェクト if 条件式]
odds = [i for i in range(10) if i % 2 == 1]
print(odds)
# [1, 3, 5, 7, 9]

odds = []
for i in range(10):
    if i % 2 == 1:
        odds.append(i)

print(odds)
# [1, 3, 5, 7, 9]