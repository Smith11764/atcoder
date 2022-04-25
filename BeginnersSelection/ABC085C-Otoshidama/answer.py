n, otoshidama = map(int, input().split())
otoshidama /= 1000
cnt_10000yen = -1
cnt_5000yen = -1
cnt_1000yen = -1

for i in range(n+1):
    for j in range(n+1):
        # 10000, 5000円札の数から1000円札の調べるべき数は決まる
        k = n - (i + j)
        if k < 0:
            break
        if otoshidama == 10*i + 5*j + k:
            cnt_10000yen = i
            cnt_5000yen = j
            cnt_1000yen = k
print('{} {} {}'.format(cnt_10000yen, cnt_5000yen, cnt_1000yen))
