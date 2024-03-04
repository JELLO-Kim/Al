import sys
import heapq
import math

input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())

dist = [math.inf for i in range(v + 1)]
gph = [[] for i in range(v + 2)]
edges = []

for _ in range(e):
    u, v, w = map(int, input().split())
    gph[u].append((v, w))

dist[s] = 0
heapq.heappush(edges, (dist[s], s))
while edges:
    cost, pos = heapq.heappop(edges)
    for p, c in gph[pos]:
        c += cost
        if dist[p] > c:
            dist[p] = c  # 업데이트
            heapq.heappush(edges, (c, p))

for item in dist[1:-1]:
    if item == math.inf:
        print("INF")
    else:
        print(item)
