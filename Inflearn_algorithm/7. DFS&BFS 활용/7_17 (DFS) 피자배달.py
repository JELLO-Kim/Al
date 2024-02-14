# 72
import sys
from collections import deque
sys.stdin = open("../input.txt", "r")
n, m = map(int, input().split())
pizza = [list(map(int, input().split())) for _ in range(n)]

def dfs(l, s):
    global res
    if l == m :
        sum = 0
        for k in range(len(hs_xy)):
            x1 = hs_xy[k][0]
            y1 = hs_xy[k][1]
            city_diff = 21740000
            for f in cb:
                pz_target_x = pz_xy[f][0]
                pz_target_y = pz_xy[f][1]
                city_diff = min(city_diff, (abs(pz_target_x-x1) + (abs(pz_target_y-y1))))
            sum += city_diff
        if sum < res:
            res = sum
    else:
        for j in range(s, len(pz_xy)):
            cb[l] = j
            dfs(l+1, j+1)

new_pizza = []
pz_xy = []
hs_xy = []
res = 21740000
cb = [0]*m
for x in range(n):
    for y in range(n):
        if pizza[x][y] == 2:
            pz_xy.append((x, y))
        elif pizza[x][y] == 1:
            hs_xy.append((x, y))

dfs(0, 0)

print(res)
