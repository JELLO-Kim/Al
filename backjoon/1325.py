import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# n, m = map(int, input().split())
# visit = [0]*(n+1)
# dq = deque()

# # 첫번째
# for _ in range(m):
#     y, x = map(int, input().split())
#     visit[x] += 1
#     dq.append((y, x))

# while dq:
#     new_visit = [0]*(n+1)
#     for _ in range(len(dq)):
#         target = dq.popleft()
#         x = target[1]
#         y = target[0]
#         if visit[x] == 0:
#             new_visit[x] += 1
#             dq.append((y, x))
#         else:
#             new_visit[x] = visit[x] + visit[y]
#     visit = new_visit

# for idx, a in enumerate(visit):
#     if a == max(visit):
#         print(idx, end=" ")

#####################################################################

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

hack = [0] * (n + 1)
for i in range(1, n+1):
    if not graph[i]:
        continue
    visit = [False] * (n + 1)
    i_check = 0

    dq = deque()
    dq.append(i)
    visit[i] = True
    while dq:
        target = dq.popleft()
        for x in graph[target]:
            if not visit[x]:
                visit[x] = True
                dq.append(x)
                i_check += 1
    hack[i] = i_check
answer = ""
for i in range(1, n+1):
    if hack[i] == max(hack):
        print(i, end=" ")