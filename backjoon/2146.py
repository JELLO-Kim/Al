import sys
sys.stdin = open("input.txt")

from collections import deque

n = int(input())
visit = []
tmp_island = []
set_land = []

for _ in range(n):
    visit.append([False]*n)
    tmp_island.append(list(map(int, input().split())))
    set_land.append([0]*n)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def set_island_work(x, y, land_lv):
    i_q = deque()
    i_q.append((x, y))
    while i_q:
        x, y = i_q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and not visit[xx][yy] and tmp_island[xx][yy] == 1:
                visit[xx][yy] = True
                set_land[xx][yy] = land_lv
                i_q.append((xx, yy))


land_lv = 1
for x in range(n):
    for y in range(n):
        if not visit[x][y] and tmp_island[x][y] == 1:
            set_land[x][y] = land_lv
            visit[x][y] = True
            set_island_work(x, y, land_lv)
            land_lv += 1

# 다리 놓을수 있는 최단거리 파악하기
def get_short_bridge(x, y, d, land_lv):
    qq = deque()
    qq.append((x, y, d))
    # 값이 0인곳으로 이동해야 한다 (다른섬 찾아야 하니까)
    while qq:
        x, y, d = qq.popleft()
        if set_land[x][y] not in [0, land_lv]:
            return d-1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and not visit2[xx][yy]:
                visit2[xx][yy] = True
                qq.append((xx, yy, d+1))



done_land = [False] * (land_lv)
shortes_bridge = n*2
for x in range(n):
    for y in range(n):
        # 체크안한 섬이면 체크시작
        if set_land[x][y] != 0 and not done_land[set_land[x][y]]:
            visit2 = [[False] * n for _ in range(n)]
            visit2[x][y] = True
            this_bridge = get_short_bridge(x, y, 0, set_land[x][y])
            shortes_bridge = min(shortes_bridge, this_bridge)
print(shortes_bridge)