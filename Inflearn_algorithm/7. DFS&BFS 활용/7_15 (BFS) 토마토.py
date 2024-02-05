import sys
from collections import deque
import time
start = time.time()
sys.stdin = open("input.txt", "r")
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dq = deque()


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
day = 0
for x in range(n):
    for y in range(m):
        if box[x][y] == 1:
            dq.append((x, y))
while dq:
    for _ in range(len(dq)):
        now = dq.popleft()
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            if 0 <= xx < n and 0<= yy < m and box[xx][yy] == 0:
                box[xx][yy] = 1
                dq.append((xx,yy))
    if not dq:
        break
    day += 1
    # print(f"after day : {day}")
    # if day == 4:
    #     print("?")
    # for aa in box:
    #     print(aa)
    # print("===============================")
for a in box:
    if 0 in a:
        print(-1)
        break
else:
    print(day) 

end = time.time()
print(f"소요 시간 : {end-start}")