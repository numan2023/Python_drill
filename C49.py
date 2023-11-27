# ペアの数値の入った表を罫線入りで出力

# 自然数 H, W, A, B が与えられます。縦に H 行、横に W 行で計 H * W 個の (A, B) という形式の文字列を出力してください。ただし、横は | (半角スペース 2 つとバーティカルライン) 区切りで、縦は = で区切って出力してください。また、縦の文字列間で = を出力する際は、その上の行と文字数が等しくなるように出力します。

# 入力される値
# H W A B

# 期待する出力
# 答えの文字列を出力してください。


# (A_{1,1}, B_{1,1}) | (A_{1,2}, B_{1,2}) ... (A_{1,W}, B_{1,W})
# =================== ... ====================
# (A_{2,1}, B_{2,1}) | (A_{2,2}, B_{2,2}) ... (A_{2,W}, B_{2,W})
# =================== ... ====================
# ...
# ...
# ...
# =================== ... ====================
# (A_{H,1}, B_{H,1}) | (A_{H,2}, B_{H,2}) ... (A_{H,W}, B_{H,W})

# 2 3 7 8

# 出力例1
# (7, 8) | (7, 8) | (7, 8)
# ========================
# (7, 8) | (7, 8) | (7, 8)


# エラー
H, W, A, B = int(input().split())

for h in range(H):
    for w in range(W):
        print("({}, {})".format(A, B), end="")
        if w == W:
            print()
        else:
            print(" | ")

    if h < H:
        print("=" * (6 + 3 * (H - 1)))
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'


H, W, A, B = map(int, input().split())

for h in range(H):
    for w in range(W):
        print("({}, {})".format(A, B), end="")
        if w == W:
            print()
        else:
            print(" | ")

    if h < H:
        print("=" * (6 + 3 * (H - 1)))

# (7, 8) | 
# (7, 8) | 
# (7, 8) | 
# =========
# (7, 8) | 
# (7, 8) | 
# (7, 8) | 
# =========

H, W, A, B = map(int, input().split())

for i in range(H):
    for j in range(W):
        print("({}, {})".format(A, B), end="")
        if j == W - 1:
            print()
        else:
            print(end=" | ")

    if i < H - 1:
        print("=" * (6 * W + 3 * (W - 1)))


# or 模範解答
values = input().split()
H = int(values[0])
W = int(values[1])
A = int(values[2])
B = int(values[3])

for i in range(H):
    for j in range(W):
        print("({}, {})".format(A, B), end="")
        if j == W - 1:
            print()
        else:
            print(end=" | ")

    if i < H - 1:
        print("=" * (6 * W + 3 * (W - 1)))