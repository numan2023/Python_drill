# 期待する出力
# 名前, 言語, 一言"を以下のフォーマットで出力してください
  # name: 名前
  # language: 言語
  # hitokoto: 一言

# 条件
# ・出力は 3 行でおこなってください
# ・出力の各行は 1000 文字以内で出力してください

name = "名前"
language = "言語"
hitokoto = "一言"

output = f"name: {name}\nlanguage: {language}\nhitokoto: {hitokoto}"
print(output)

# f文字列(f-string): python3.6以降で導入された文字列の中に直接変数やしきを埋め込むための機能。
# fやFを文字列の前に置くことで、波括弧{}内に変数やしきを書くことができる。