# 整数の入力
a = int(input())

# スペース区切りの整数の入力
# mapは第一引数に適用する関数、第２引数に適用したいオブジェクトを指定
b, c = map(int, input().split())

# 文字列の入力
s = input()

# output
print('{} {}'.format(a+b+c, s))
