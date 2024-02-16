import sys
sys.stdin = open("input.txt", "r")

from collections import deque

k = int(input())
w, h = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(h)]
visit = [[0]*w for _ in range(h)]
hx = [-2, -1, 1, 2, 2, 1, -1, -2]
hy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# h_end_idx = 7
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
        # print(f"이동레벨 :{move_level}")
        move_x = m_info[1]
        move_y = m_info[2]
        horse_move = m_info[3]
        if move_level >= w*h:
            dq.clear()
            break
        if move_x == h-1 and move_y == w-1:
            print(move_level)
            check = True
            dq.clear()
            break
        else:
            if horse_move < k:
                for i in range(8):
                    xx = move_x + hx[i]
                    yy = move_y + hy[i]
                    if 0 <= xx < h and 0 <= yy < w and chess[xx][yy] != 1:
                        dq.append((move_level + 1, xx, yy, horse_move + 1))
            for j in range(4):
                xx = move_x + dx[j]
                yy = move_y + dy[j]
                if 0 <= xx < h and 0 <= yy < w and chess[xx][yy] != 1:
                    dq.append((move_level + 1, xx, yy, horse_move))



            # for i in range(12):
            #     xx = move_x + dx[i]
            #     yy = move_y + dy[i]
                # if 0 <= xx < h and 0 <= yy < w and chess[xx][yy] != 1 and visit[xx][yy] == 0:
                # if 0 <= xx < h and 0 <= yy < w and chess[xx][yy] != 1:
                #     # visit[xx][yy] = 1
                #     if i <= h_end_idx:
                #         if horse_move >= k:
                #             # visit[xx][yy] = 0
                #             continue
                #         dq.append((move_level+1, xx, yy, horse_move+1))
                #     else:
                #         dq.append((move_level+1, xx, yy, horse_move))


if not check:
    print(-1)