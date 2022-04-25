n, a, b = map(int, input().split())
summary = 0

for i in range(n+1):

    '''
    list('文字列')で['文', '字', '列']に区切られることを利用する
    ex) i=23 は['2','3']となり、
        これをintに変換してsum()でリストの各要素（各桁）を合計する
    '''
    tmp_sum = sum(map(int, list(str(i))))

    if a <= tmp_sum <= b:
        summary += i

print(summary)
