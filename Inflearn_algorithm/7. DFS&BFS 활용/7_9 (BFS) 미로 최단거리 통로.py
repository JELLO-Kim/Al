import sys
from collections import deque
sys.stdin = open("input.txt", "r")
dq = deque()

m = [list(map(int, input().split())) for _ in range(7)]
start = (0,0)  # 원래는 (1,1)
end = (6,6)  # 원래는 (6,6)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dis = [[0]*7 for _ in range(7)]
dq.append(start)
# 시작점 체크
m[start[0]][start[1]] = 1
while dq:
    now = dq.popleft()
    for i in range(4):
        x = now[0] + dx[i]
        y = now[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and m[x][y] == 0:
            m[x][y] = 1
            dis[x][y] = dis[now[0]][now[1]] + 1
            dq.append((x, y))

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])

