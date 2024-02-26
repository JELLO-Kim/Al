import sys, time
from collections import deque
sys.stdin = open("input.txt")
n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())

wall_count = 0
mirror = []
for _ in range(n):
    row = list(map(int, input().split()))
    wall_count += sum(row)
    mirror.append(row)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def go_mirror(x, y, d, mirror):
    q = deque()
    q.append((x, y, d))
    while q:
        x, y, d = q.popleft()
        if x == ex-1 and y == ey-1:
            return d
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx < n and 0 <= yy < m and not visit[xx][yy] and mirror[xx][yy] == 0:
                visit[xx][yy] = True
                q.append((xx, yy, d+1))


short_time = 21740000
exit_time = []
for x in range(n):
    if wall_count == 0:
        break
    for y in range(m):
        if mirror[x][y] == 1:
            wall_count -= 1
            mirror[x][y] = 0
            visit = [[False] * m for _ in range(n)]
            visit[hx-1][hy-1] = True
            exit_time.append(go_mirror(hx-1, hy-1, 0, mirror))
            mirror[x][y] = 1
            if wall_count == 0:
                break

if len(exit_time) > 0:
    print(min(exit_time))
else:
    print(-1)