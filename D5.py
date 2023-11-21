## 2つの数値を出力

# 2つの 1 を半角スペース区切りで出力してください

# 入力される値
# 入力はありません。

# 期待する出力
# 答えの数値を 1 行で出力してください。
# 1 1

print("1 1")
# or
print("{} {}".format(1, 1))
# formatメソッドを使用する方法はより柔軟で、特に変数の値を文字列に組み込む場合に便利。

##-------------------
# 変数の値を文字列に組み込むとは、文字列の中で変数の実際の値を使用することを指す。
# これにより、プログラムの実行中に変化するデータを出力する際に便利。

# 変数定義
name = alice
age = 30

# 変数を文字列に組み込む
message = "{}は{}歳です。".format(name, age)

print(message)