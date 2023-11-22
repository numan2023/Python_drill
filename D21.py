# 占い

# ある占いでは、箱の中に 1~9 までのいずれかの数字が書かれている玉を取り出し、その玉に書かれている数字から運勢を占います。
# 玉に書かれている数字が 7 の時は大吉となります。占いで取り出した玉に書かれている数字が 1 つ与えられます。大吉かどうかを判定してください。

# 入力される値
# n

# 期待する出力
# 大吉の場合は「Yes」、そうでない場合は「No」と 1 行に出力してください。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。
# ・ 1 ≦ n ≦ 9

# 入力例1
# 7
# 出力例1
# Yes

# 入力例2
# 3
# 出力例2
# No

# randomモジュール
import random

n = random.randint(1, 9)
if n == 7:
    print("Yes")
else:
    print("No")

# より詳細なコーディング
import random

def fortune_telling():
    n = random.randint(1, 9)
    print(f"取り出した数字： {n}")

    if n == 7:
        return "Yes"
    else:
        return "No"
    
result = fortune_telling()
print(f"大吉かどうか： {result}")

# or 模範解答
n = int(input())

if n == 7:
    print("Yes")
else:
    print("No")