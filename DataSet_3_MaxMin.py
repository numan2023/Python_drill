# 最大値と最小値
# 自然数 A, B, C が与えられます。(A, B, C の最大値) - (A, B, C の最小値)を答えてください。

# 入力される値
# A B C

# 期待する出力
# 答えを1行に出力してください。

# 入力例1
# 30 50 10

# 出力例1
# 40


n = [int(x) for x in input().split()]
print(max(n) - min(n))

# or 模範解答1
li = [int(x) for x in input().split()]
li.sort()
print(li[2] - li[0])
# sortメソッド：昇順にソート、先頭の要素が最小値、末尾の要素が最大値

# 模範解答2
li = [int(x) for x in input().split()]
sorted_li = sorted(li)
print(sorted_li[2] - sorted_li[0])
# sorted関数を使用

# 模範解答3
li = [int(x) for x in input().split()]
print(max(li) - min(li))