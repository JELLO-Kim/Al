"""
DP 속 BFS
각 지점은 BFS로 최소거리를 구한 뒤
DP를 활용해 중복처리 하지 않기


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0, 0, 0, 0, 25]
[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 0, 1, 1, 1, 26]
[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 0, 2, 0, 0, 0]
[14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 3, 1, 1, 1]


"""

import sys, time
start = time.time()
sys.stdin = open("input.txt")

from collections import deque
n, m = map(int, input().split())

road = []
goal = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            goal = [i, j]
    road.append(row)
dp = [[0]*(m) for _ in range(n)]
visit = [[0]*(m) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, count):
    q = deque()
    q.append((x, y, count))
    while q:
        x, y, count = q.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= xx < n and 0 <= yy < m and visit[xx][yy] == 0 and road[xx][yy] == 1:
                visit[xx][yy] = 1
                dp[xx][yy] = count + 1
                q.append((xx, yy, count + 1))

visit[goal[0]][goal[1]] = 1
bfs(goal[0], goal[1], 0)
for x in range(n):
    for y in range(m):
        if visit[x][y] == 0:
            if road[x][y] == 0:
                print(0, end=" ")
            else:
                print(-1, end=" ")
        else:
            print(dp[x][y], end=" ")
    print("")

end = time.time()
print(f"소요시간 : {end-start}")