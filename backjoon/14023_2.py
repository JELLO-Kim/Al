import sys, time
from collections import deque
sys.stdin = open("input.txt")
n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())

mirror = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def go_mirror(x, y, d, magic, visit):
    q = deque()
    q.append((x, y, d, magic, visit))
    while q:
        x, y, d, magic, visit = q.popleft()
        if x == ex-1 and y == ey-1:
            return d
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx < n and 0 <= yy < m and not visit[xx][yy]:
                if mirror[xx][yy] == 0:
                    visit[xx][yy] = True
                    q.append((xx, yy, d+1, magic, visit))
                    visit[xx][yy] = False
                else:
                    if not magic:
                        visit[xx][yy] = True
                        q.append((xx, yy, d+1, True, visit))
                        visit[xx][yy] = False

visit = [[False] * m for _ in range(n)]
visit[hx-1][hy-1] = True
res = go_mirror(hx-1, hy-1, 0, False, visit)
print(res if res else -1)