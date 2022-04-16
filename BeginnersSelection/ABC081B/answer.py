n = int(input())
list_a = list(map(int, input().split()))
cnt = 0

# allですべての要素に対して判定できる
# ジェネレーターを使うと順次作られたものが評価され、False時点で要素を作らないので速い
while all(i%2==0 for i in list_a):
    list_a = [i/2 for i in list_a] # リスト内包表記
    cnt += 1
print(cnt)
