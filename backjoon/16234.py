import sys
sys.stdin = open("input.txt", "r")
from collections import deque
n, l, r = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    team = []
    q = deque()
    q.append((x, y))
    team.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and visit[xx][yy] == 0:
                if l <= abs(country[x][y] - country[xx][yy]) <= r:
                    visit[xx][yy] = 1
                    team.append((xx, yy))
                    q.append((xx, yy))
    return team
day = 0
while True:
    visit = [[0] * n for _ in range(n)]
    is_exists = False
    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0:
                visit[x][y] = 1
                team = bfs(x, y)
                if len(team) > 1:
                    is_exists = True
                    new_p = sum([country[xy[0]][xy[1]] for xy in team]) // len(team)
                    for xy in team:
                        country[xy[0]][xy[1]] = new_p

    # 인구이동 없으면 즉시 브레이크
    if not is_exists:
        break
    day += 1
print(day)

