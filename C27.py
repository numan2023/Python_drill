# 2*2の出力

# 4 つの数値 0, 8, 1, 3 をこの順に、2 行 2 列の形で出力してください。
# ただし、数値の間には半角スペースを、各行の末尾には、半角スペースの代わりに改行を入れてください。

# 入力される値
# ありません。

# 期待する出力
# 答えの数値を出力してください。


# 0 8
# 1 3

list = [0, 8, 1, 3]

for l in range(len(list)):
    if l == 0 or l == 1:
        nums_1 = list[l]
    else:
        nums_2 = list[l]

print(",".join(nums_1))
print(",".join(nums_2))
# エラー文：IndexError: Replacement index 1 out of range for positional args tuple
  # 意味）文字列フォーマット操作において発生する一般的なエラーで、"{}{}".format(1)コードがあるとき、2つのプレースホルダーに対して、フォーマットメソッドには1つの引数しか提供されていないことを意味する。インデックス1は２番目のプレースホルダーに対応する引数がないことを検出している。

# or ChatGPT解答
print("0 8")
print("1 3")

# or 模範解答
print("0 8\n1 3")