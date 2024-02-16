import sys
sys.stdin = open("input.txt", "r")
from collections import deque

k = int(input())
w, h = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(h)]
visit = [[0]*w for _ in range(h)]
dx = [-2, -1, 1, 2, 2, 1, -1, -2, -1, 0, 1, 0]
dy = [-1, -2, -2, -1, 1, 2, 2, 1, 0, -1, 0, 1]

h_end_idx = 7
horse_move = 0
dq = deque()
# level, x, y, horse_move
visit[0][0] = 1
dq.append((0, 0, 0, 0))
check = False
while dq:
    for _ in range(len(dq)):
        m_info = dq.popleft()
        move_level = m_info[0]
        move_x = m_info[1]
        move_y = m_info[2]
        horse_move = m_info[3]
        if move_x == h-1 and move_y == w-1:
            print(move_level)
            check = True
            dq.clear()
            break
        else:
            for i in range(12):
                xx = move_x + dx[i]
                yy = move_y + dy[i]
                if 0 <= xx < h and 0 <= yy < w and chess[xx][yy] != 1 and visit[xx][yy] == 0:
                    visit[xx][yy] = 1
                    if horse_move < k and i <= h_end_idx:
                        dq.append((move_level+1, xx, yy, horse_move+1))
                    dq.append((move_level+1, xx, yy, horse_move))

if not check:
    print(-1)