import sys, time
from collections import deque
sys.stdin = open("input.txt")
n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
mirror = [list(map(int, input().split())) for _ in range(n)]
visit = [[[False]*2 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


q = deque()
d = 1
magic = 0
q.append((hx-1, hy-1, d, magic))
visit[hx-1][hy-1] = [True, True]
exit_done = False
while q:
    x, y, d, magic = q.popleft()
    if x == ex-1 and y == ey-1:
        print(d-1)
        exit_done = True
        q.clear()
        break
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx < n and 0 <= yy < m:
            # 해당 경우의 수에 대한 방문이력 있음
            if visit[xx][yy][magic]:
                continue
            # 칸이 0 이고 0 방문 안했음
            if mirror[xx][yy] == 0:
                visit[xx][yy][magic] = True
                q.append((xx, yy, d + 1, magic))
            else:
                # 마법 안썼다
                if magic == 0:
                    visit[xx][yy][1] = True
                    q.append((xx, yy, d+1, 1))

if not exit_done:
    print(-1)