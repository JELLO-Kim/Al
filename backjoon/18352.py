import sys
sys.stdin = open("input.txt")
from math import inf
from collections import deque
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
dist = [inf for i in range(n + 1)] # x 의 이동거리
# 자기자신으로 가는 최단거리는 0이다
dist[x] = 0
dq = deque()

for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

dq.append((dist[x], x))
while dq:
    cost, pos = dq.popleft()
    for row in city[pos]:
        row_cost = cost + 1
        if dist[row] > row_cost:
            dist[row] = row_cost
            dq.append((row_cost, row))

if dist.count(k) == 0:
    print(-1)
else:
    for idx, i in enumerate(dist):
        if i == k:
            print(idx)