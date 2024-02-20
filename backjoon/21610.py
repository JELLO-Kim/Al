import sys
sys.stdin = open("input.txt")
from collections import deque

n, m = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

rx = [-1, -1, 1, 1]
ry = [-1, 1, -1, 1]

move_ds = deque([list(map(int, input().split())) for _ in range(m)])

rain = deque()
rain.extend([(n - 1, 1 - 1), (n - 1, 2 - 1), (n - 1 - 1, 1 - 1), (n - 1 - 1, 2 - 1)])

def bfs(x, y, visit, prior_rain):
    q = deque()
    q.append((x, y))
    next_rain = deque()
    while q:
        x, y = q.popleft()
        if visit[x][y] == 0:
            visit[x][y] = 1
            if basket[x][y] >= 2 and [x, y] not in prior_rain:
                basket[x][y] -= 2
                next_rain.append((x, y))
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and visit[xx][yy] == 0:
                visit[xx][yy] = 1
                q.append((xx, yy))
                if basket[xx][yy] >= 2 and [xx,yy] not in prior_rain:
                    # 구름 생기면 물의 양 2 줄음
                    basket[xx][yy] -= 2
                    next_rain.append((xx, yy))
    return next_rain

def set_rain(visit):
    for x in range(n):
        for y in range(n):
            if basket[x][y] >= 2 and not visit[x][y]:
                basket[x][y] -= 2
                rain.append((x, y))
            # if visit[x][y] == 0:
            #     next_rain = bfs(x, y, visit, prior_rain)
            #     rain.extend(next_rain)
    return rain
while m > 0:
    visit = [[False]*n for _ in range(n)]

    # if not rain:
    move = move_ds.popleft()
    move_d = move[0]-1
    move_s = move[1]
    duple_area = []
    for _ in range(len(rain)):
        one_x, one_y = rain.popleft()

        new_x = one_x + dx[move_d]*move_s
        new_y = one_y + dy[move_d]*move_s
        if new_x < 0:
            new_x = n - (abs(new_x) % n)
        elif new_x >= n:
            new_x = new_x % n
        if new_x == n:
            new_x = 0
        if new_y < 0:
            new_y = n - (abs(new_y) % n)
        elif new_y >= n:
            new_y = new_y % n
        if new_y == n:
            new_y = 0
        try:
            basket[new_x][new_y] += 1  # 구름 이동하여 물양 1 증가됨. 이동한 구름은 없어진다.
        except Exception as e:
            print()
        # 물복사를 위해 값 저장
        duple_area.append((new_x, new_y))
        visit[new_x][new_y] = True


    for new_x, new_y in duple_area:
        # 물복사
        add_r = 0
        for i in range(4):
            duple_rx = new_x + rx[i]
            duple_ry = new_y + ry[i]
            if 0 <= duple_rx < n and 0 <= duple_ry < n and basket[duple_rx][duple_ry] > 0:
                add_r += 1
        basket[new_x][new_y] += add_r

    # 이동이 끝난 후 구름

    # 구름 세팅
    rain = set_rain(visit)

    m -= 1
tt = 0
for a in basket:
    tt += sum(a)
print(tt)
