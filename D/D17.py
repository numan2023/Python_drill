# 乗客人数

# ある電車に a 人が乗っています。
# 駅に到着した時に b 人が降りて新たに c 人が乗車する時、電車に乗っている乗客人数を求めてください。

# 入力される値
# a b c
# ・ 1 行目に 整数 a,b,c がそれぞれ半角スペース区切りで与えられます。

# 期待する出力
# 電車に乗っている乗客人数を出力してください。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# ・ 1 ≦ a ≦ 1000
# ・ 0 ≦ b ≦ a
# ・ 1 ≦ c ≦ 1000

# 入力例1
# 5 3 2
# 出力例1
# 4

def calculate_passengers(a, b, c):
    if 1 <= a <= 1000 and 0 <= b <= a and 1 <= c <= 1000:
        passengers = a - b + c
        return passengers

a, b, c = map(int, input().split(" "))
result = calculate_passengers(a, b, c)
print(result)

# or
a, b, c = map(int, input().split())

print(a - b + c)