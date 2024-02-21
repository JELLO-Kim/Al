import sys

sys.stdin = open("input.txt")
from collections import deque

#
n = int(input())
shark = None
area = []
for x in range(0, n):
    row = list(map(int, input().split()))
    if 9 in row:
        shark = [x, row.index(9), 2, 0]
        row[row.index(9)] = 0
    area.append(row)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque()
q.append(shark)
sq = deque()
def find_fish(x, y, lv, visit) -> list:
    sq.append([x, y, visit])
    loop_lv = 0
    while sq:
        loop_lv += 1
        # 가장 가까운 생선 찾기
        can_eat = set()
        for _ in range(len(sq)):
            target = sq.popleft()
            visit = target[2]
            for i in range(4):
                xx = target[0] + dx[i]
                yy = target[1] + dy[i]
                # 만약 먹을수 있는 생선 찾으면 return 하는데 여러개인지 체크 필요
                # 이동 가능 조건
                if 0 <= xx < n and 0 <= yy < n:
                    # 먹을 수 있는 생선이다.
                    try:
                        if 0 < area[xx][yy] < lv:
                            can_eat.add((xx, yy))
                        # 빈공간은 무조건 이동 가능하다. (먹는건 없음)
                        elif area[xx][yy] in [0, lv] and not visit[xx][yy]:
                            visit[xx][yy] = True
                            sq.append([xx, yy, visit])
                    except Exception as e:
                        print(e)
                        continue

        if can_eat:
            can_eat = list(can_eat)
            # [x, y] 랑 비교해서 1순위 : 위 / 2순위 : 왼쪽 기준인 좌표 뽑아내기
            min_xy = 217400000
            next_target = None
            for idx, eat in enumerate(can_eat):
                # 이동거리를 확인한다.
                x_abs = abs(x-eat[0])
                y_abs = abs(y-eat[1])
                xy_abs = x_abs + y_abs
                if xy_abs < min_xy:
                    # 새로운 최소거리 이다.
                    next_target = can_eat[idx]
                    min_xy = xy_abs
                elif xy_abs == min_xy:
                    # 이동거리가 같다. 1순위 더 위, 2순위인 더 왼쪽을 확인한다. eat과 next_target 비교하기
                    # 1순위 : 더 위에 있는 것
                    if next_target[0] < eat[0]:
                        continue
                    elif next_target[0] == eat[0]:
                        # 2순위 : 더 왼쪽에 있는 것
                        if next_target[1] < eat[1]:
                            continue
                        else:
                            next_target = can_eat[idx]
                    else:
                        next_target = can_eat[idx]
            return next_target

    return None
# shark = [x, row.index(9), 2, 0] | x, y, level, lv_eat
cnt = 0
while True:
    visit = [[False]*n for _ in range(n)]
    visit[shark[0]][shark[1]] = True
    next_fish = find_fish(shark[0], shark[1], shark[2], visit)
    # 한번 이동할때 인접한 크기로 1초씩 이므로 가장 가까운 물고기의 이동 칸수만큼 초가 더해진다
    if not next_fish:
        print(cnt)
        break
    cnt += (abs(shark[0]-next_fish[0]) + abs(shark[1] - next_fish[1]))
    area[next_fish[0]][next_fish[1]] = 0
    shark[3] += 1
    # 레벨 마리수 만큼 먹었으면 레벨업!
    if shark[2] == shark[3]:
        shark[2] += 1
        shark[3] = 0
    shark[0:2] = next_fish




