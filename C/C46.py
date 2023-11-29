# 2つの文字列を出力
# 文字列 S, T が与えられます。S + T = ST という形式で文字列を出力してください。

# 入力される値
# S
# T

# 期待する出力
# 答えの文字列を出力してください。


# S + T = ST


S = input()
T = input()
ST = S + T

print("{} + {} = {}".format(S, T, ST))
# or
print("{} + {} = {}".format(S, T, S + T))