"""
2 つの文字列 a, b が入力されます。文字列が一致していれば "OK" 、異なっていれば "NG" と出力してください。

入力される値
入力は以下のフォーマットで与えられます。

a
b

・1 行目に文字列 a
・2 行目に文字列 b

期待する出力
文字列 a と文字列 b が一致していれば "OK" 、異なっていれば "NG" と出力してください。

入力例1
paiza
paiza

出力例1
OK

入力例2
paiza
aziap

出力例2
NG
"""

a = input()
b = input()
if a == b:
    print("OK")
else:
    print("NG")

