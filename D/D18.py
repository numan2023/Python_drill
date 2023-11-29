# 単純な条件分岐

# 文字列Sが与えられます。Sがpaizaと一致する場合はYESを、一致しない場合はNOを出力してください。

# 入力される値
# S

# 期待する出力
# YESまたはNOを出力してください。末尾に改行を入れ、余計な文字、空行を含んではいけません。

# YES
# または
# NO

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# ・ Sは英小文字からなる文字列
# ・ Sの長さは 1 以上 20 未満

# 入力例1
# paiza
# 出力例1
# YES

# 入力例2
# pizza
# 出力例2
# NO

s = input()
if s.islower() and 1 <= len(s) <= 20:
    if s == "paiza":
        print("YES")
    else:
        print("NO")

# or
s = input()

if s == "paiza":
    print("YES")
else:
    print("NO")

# ==演算子：値が「等しいか」を判定する
  # A == B -> True or False