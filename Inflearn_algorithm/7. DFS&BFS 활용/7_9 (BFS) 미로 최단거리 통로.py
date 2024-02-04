import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def first_sol():
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


dq = deque()
# 상하좌우 확인해서 0인 지점으로 이동해야 한다.
dx = [-1,0,1,0]
dy = [0,-1,0,1]

m = [list(map(int, input().split())) for _ in range(7)] # 주어진 미로
ch = [[0]*7 for _ in range(7)] # 이동 횟수 기록용

dq.append((0,0))  # 출발지점 1,1
m[0][0] = 1

while dq:
    now = dq.popleft()
    for i in range(4):
        x = now[0] + dx[i] 
        y = now[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and m[x][y] == 0:
            m[x][y] = 1
            ch[x][y] = ch[now[0]][now[1]] + 1
            dq.append((x,y))

if ch[6][6] == 0:
    print(-1)
else:
    print(ch[6][6])
