# 入力された2つの文字列を出力

# 2 つの文字列 S, T が入力されます。S, T を改行区切りで出力してください。

# 入力される値
# S
# T

# 期待する出力
# 答えの文字列を 2 行で出力してください。
# S
# T

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# * S, T の長さは 1 以上 10 以下
# * S, T は英小文字列

# 入力例1
# paiza
# learning

# 出力例1
# paiza
# learning

# -------------
# 正規表現(regular expressions(REs, regexes, regex patterns))
  # 文字列内で文字の組み合わせを照合するために用いられるパターン
  
  #文字列のパターンマッチング・置換
  # テキスト解析
  # データのバリデーション

  # 記法
    # メタ文字：正規表現はいくつかの特別な文字”メタ文字”で表現される。
      # re$ -> adventure, moreなどが抽出される。
      # https://techplay.jp/column/463

s = input()
t = input()

if 1 <= len(s) <= 10 and 1 <= len(t) <= 10 and s.islower() and t.islower():
    print(s)
    print(t)
else:
    print("入力された文字列が条件が満たしていません。")

# or

S = input()
T = input()

print(S)
print(T)