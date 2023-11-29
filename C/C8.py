# 10個の数値を出力(末尾に半角スペース有)

# 1 から 10 までの数値をすべて、出力してください。
# ただし、数値の後には必ず半角スペースを出力してください。

# 入力される値
# 入力はありません。

# 期待する出力
# 答えの数値を 1 行で出力してください。

# 1 2 3 4 5 6 7 8 9 10

# Bad Code
print("{} {} {} {} {} {} {} {} {} {} ".format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# or 模範解答

for i in range(10):
    print(i + 1, end=" ")

print()
# print関数はデフォルトで末尾開業を出力しますが、キーワード引数でend=XXXのように記述すると改行の代わりに末尾でXXXを出力することができる。
# print関数を引数なしでprint()のように使うと、改行のみ出力されるので、最後にこれを記述して末尾に改行を入れることができる。