n = int(input())

# 初期値
prev_t, prev_x, prev_y = 0, 0, 0
flag = True

for i in range(n):
    t, x, y = map(int, input().split())
    dt = abs(t - prev_t)
    dx = abs(x - prev_x)
    dy = abs(y - prev_y)

    # 次回ループの初期値として保存
    prev_t = dt
    prev_x = dx
    prev_y = dy

    # 経過時間よりもマンハッタン距離が長かったらNG
    if dt < (dx + dy):
        flag = False
    # 時間の経過とマンハッタン距離の偶奇が違ったらNG
    elif dt % 2 != (dx + dy) % 2:
        flag = False

if flag == True:
    print('Yes')
else:
    print('No')
