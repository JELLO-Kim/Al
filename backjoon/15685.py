import sys
sys.stdin = open("input.txt")

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def set_dragon(x, y, pre_d_list, this_d_list, generation, all_point):
    if generation > g:
        return all_point
    # 이번세대 이동 작업
    for d in this_d_list:
        x = x + dx[d]
        y = y + dy[d]
        all_point.append([x,y])
    # 이전세대로 이동 넘기기
    pre_d_list.extend(this_d_list)
    next_d_list = []
    # 다음세대 이동작업 세팅
    for i in range(len(pre_d_list)-1, -1, -1):
        check = pre_d_list[i]+1
        if check == 4:
            check = 0
        next_d_list.append(check)
    # 재귀~
    return set_dragon(x, y, pre_d_list, next_d_list, generation+1, all_point)

one_sx = [0, 1, 0, 1]
one_sy = [0, 0, 1, 1]

def check_square(min_x, min_y, x_len, y_len, all_dragon_point):
    cnt = 0
    for iy in range(y_len):
        y = min_y + iy
        for ix in range(x_len):
            x = min_x + ix
            for i in range(4):
                xx = x + one_sx[i]
                yy = y + one_sy[i]
                if [xx,yy] not in all_dragon_point:
                    break
            else:
                cnt += 1
    return cnt


all_dragon_point = []
dragon_exists = []
for _ in range(n):
    x, y, d, g = map(int, input().split())
    all_dragon_point.extend(set_dragon(x, y, [], [d], 0, [[x, y]]))
max_x = max([xy[0] for xy in all_dragon_point])
min_x = min([xy[0] for xy in all_dragon_point])
max_y = max([xy[1] for xy in all_dragon_point])
min_y = min([xy[1] for xy in all_dragon_point])
dragon_exists = [[False] * (abs(max_x - min_x)+1) for _ in range(abs(max_y-min_y))]
cnt = check_square(min_x, min_y, abs(max_x - min_x)+1, abs(max_y-min_y)+1, all_dragon_point)
print(cnt)
