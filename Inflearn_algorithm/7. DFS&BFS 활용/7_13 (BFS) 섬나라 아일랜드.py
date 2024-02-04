import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dq = deque()

dx = [-1, -1, 0, 1, 1, 1 ,0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
cnt = 0 # 섬의 갯수

for i in range(n):
    for j in range(n):
        if land[i][j] == 1:
            land[i][j] = 0
            dq.append((i, j))
            while dq:
                now = dq.popleft()
                for k in range(8):
                    x = now[0] + dx[k] 
                    y = now[1] + dy[k]
                    if 0<=x<n and 0<=y<n and land[x][y] == 1:
                        land[x][y] = 0
                        dq.append((x, y))
            cnt += 1
print(cnt)