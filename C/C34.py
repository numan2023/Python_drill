# すべての行の長さが不定な2次元配列の出力

# 自然数 N と N 個の要素の数列 M が与えられます。1 ≦ i ≦ N の各 i について、i 行目には以下の数列を出力してください。
# * 1 以上 M_i 以下のすべての自然数を昇順、半角スペース区切りで出力してください。

# 入力される値
# N
# M_1 M_2 M_3 ... M_N

# 期待する出力
# 答えの数値を出力してください。


# 1 2 3 4 ... M_1
# 1 2 3 4 ... M_2
# ...
# 1 2 3 4 ... M_N

# 入力例1
# 4
# 2 4 3 1

# 出力例1
# 1 2
# 1 2 3 4
# 1 2 3
# 1

# GPT
def print_variable_length_arrays(N, M_list):
    # 各行に対して、1からM_iまでの自然数を出力
    for M in M_list:
        for i in range(1, M + 1):
            print(i, end=" ")
        print()  # 各行の終わりに改行を挿入

# 入力例
N_example = 4
M_list_example = [2, 4, 3, 1]
print_variable_length_arrays(N_example, M_list_example)


# or 模範解答
# ポイント
  # 直角三角形の出力
  # 変更点：i行目に出力する数値の個数がi-> M_i個
  # 配列に値を入れておいて、1つずつiだった部分をM_iにする。
N = int(input())

# N個の整数m_iを受け取るために要素数NのリストをMを[0]*Nで用意する。
M = [0] * N
values = input().split()
for i in range(N):
    # 整数型としてリストMに要素として代入
    M[i] = int(values[i])

for i in range(N):
    for j in range(1, M[i] + 1):
        if j == M[i]:
            print(j)
        else:
            print(j, end=" ")

# M = [0] * N:

# これは、長さ N のリスト M を作成し、すべての要素を 0 で初期化します。N はあらかじめ定義された自然数です。このリストは後で入力される値で更新されます。
# 以下の説明文の意味をもう少しわかりやすく説明してください。またM = []でリストを作るのとは違うのでしょうか？
# M = [0] * N
# -> これは、長さ N のリスト M を作成し、すべての要素を 0 で初期化します。
# M = [0] * N というコード行の意味は、長さが N で、すべての要素が 0 であるリスト M を作成することです。これはリストの初期化の一般的な方法の一つです。例えば、N が 4 の場合、このコードは M = [0, 0, 0, 0] と同じ意味になります。
# M = [] でリストを作る場合、これは空のリストを作成することを意味します。ここで重要なのは、リスト M に最初から特定のサイズや値がないということです。後で、このリストに対して新しい要素を追加することができます。
# それに対して M = [0] * N を使う場合、リストは最初から特定のサイズ（この場合は N）を持っており、すべての要素が 0 で初期化されます。この方法は、あらかじめ決まったサイズのリストが必要で、すべての要素を同じ値（この場合は 0）で始めたいときに便利です。
# 要約すると、M = [0] * N は特定のサイズと初期値を持つリストを作成する方法であり、M = [] はサイズや初期値を指定せずに空のリストを作成する方法です。
# ----------
# values = input().split():

# ここでユーザーからの入力を受け取り、入力された文字列を空白で分割して values リストに格納します。このリストは文字列のリストです。
# 最初の for ループ:

# このループは values リストの各要素を反復し、それを整数に変換してリスト M の対応する位置に格納します。結果的に M はユーザーから入力された数値のリストになります。
# 2番目の for ループ:

# 外側のループ (for i in range(N)) はリスト M の各要素に対して反復処理を行います。
# 内側のループ (for j in range(1, M[i] + 1)) は 1 から M[i] までの数値を反復します。
# 内側のループ内で、if j == M[i]: 条件は、現在の反復が M[i] の値に達したかどうかをチェックします。もし達していれば、print(j) は数値 j を出力し、新しい行に移動します。
# それ以外の場合（else）、print(j, end=" ") は数値 j を出力し、行末にスペースを追加します（新しい行には移動しません）。


# or 解答例2
N = int(input())
M = [int(x) for x in input().split()]

for i in range(N):
    for j in range(1, M[i] + 1):
        if j == M[i]:
            print(j)
        else:
            print(j, end=" ")