"""
5 つの正の整数が入力されるので、最も小さい数字を出力して下さい。

入力される値
入力は以下のフォーマットで与えられます。

n_1
n_2
n_3
n_4
n_5

期待する出力
n_1, n_2, n_3, n_4, n_5 のうち最も小さい数字を出力して下さい。

入力例1
10
12
4
8
46

出力例1
4
"""

for i in range(5):
    n = int(input())

print(min(n))
# Error
    # print(min(n))
    # TypeError: 'int' object is not iterable


# Success 30点
for i in range(5):
    n = input()

print(min(n)) # min関数を使用し、リストの要素の最小値を取得することができる。


# 模範解答
n = [int(input()) for _ in range(5)]
print(min(n))


"""
Please tell me the difference between the following codes
->
The two code snippets(切れ端) you've provided in Python are designed to read a series of inputs and then find the minimum value among them. However, there are key differences in how they handle and store the input, which affects their functionality and correctness.

Code 1 :
・Functionality : This code reads an input value n five times in a loop. However it overwrites the values of n in each iteration of the loop. This means that only the last input values is stored in n after the loop completes.
・Problem : When min(n) is called, it's actually trying to find the minimum character (based on ASCⅡ value) in the string n, which is the last input value. This is not the intended functionality of finding the minimum of five inputs.
・Conclusion : This code will not work correctly for the intended purpose of finding the minimum of five input numbers. It will only find the minimum character of the last input string.

Code 2 :
・Functionality : This code uses a list comprehension to read five inputs and store each as an integer in a list n. The int(input()) inside the list comprehension converts each input into an integer before storing it in the list.
・Correctness : After reading and storing all five inputs in the list n, min(n) correctly finds the minimum value among these five integers.
・Conclusion : This code works as intended for the purpose of finding the minimum of five input numbers.

Summary : 
The main difference is that the first code snippet only keeps the last input and tries to find the minimum character in this string, which is not the intended functionality. The second snippet correctly reads and stores all five inputs as integers in a list and then finds the minimum value among these numbers.
"""
