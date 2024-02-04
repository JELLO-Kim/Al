import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def first_sol():
    m = [list(map(int, input().split())) for _ in range(7)]
    m[0][0] = 1 # 출발지 체크
    start = (0,0)  # 원래는 (1,1)
    end = (6,6)  # 원래는 (6,6)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def DFS(now):
        global cnt
        if now[0] == 6 and now[1] == 6:
            cnt += 1
            return
        else:
            for i in range(4):
                new_x = now[0] + dx[i] 
                new_y = now[1] + dy[i]
                if 0 <= new_x <= 6 and 0 <= new_y <= 6 and m[new_x][new_y] == 0:
                    m[new_x][new_y] = 1
                    DFS((new_x, new_y))
                    m[new_x][new_y] = 0

    DFS(start)
    print(cnt)

m = [list(map(int, input().split())) for _ in range(7)]
m[0][0] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = 0

def DFS_two(xy):
    global cnt
    if xy[0] == 6 and xy[1] == 6:
        cnt += 1
    else:
        for i in range(4):
            next_x = xy[0] + dx[i]
            next_y = xy[1] + dy[i]
            if 0 <= next_x <= 6 and 0 <= next_y <= 6 and m[next_x][next_y] == 0:
                m[next_x][next_y] = 1
                DFS_two((next_x, next_y))
                m[next_x][next_y] = 0

DFS_two((0,0))
print(cnt)

