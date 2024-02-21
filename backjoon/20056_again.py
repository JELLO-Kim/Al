import sys
sys.stdin = open("input.txt", "r")

n, m, k = map(int, input().split())
fire_ball = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fire_ball[r-1][c-1].append((m, s, d))


fx = [-1, -1, 0, 1, 1, 1, 0, -1]
fy = [0, 1, 1, 1, 0, -1, -1, -1]
def move_fire_ball(fire_ball):
    this_ball = [[[]for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if len(fire_ball[x][y]) > 0:
                for fire in fire_ball[x][y]:
                    new_r = x + (fx[fire[2]]) * fire[1]
                    new_c = y + (fy[fire[2]]) * fire[1]
                    if new_r < 0:
                        new_r = n - (abs(new_r)%n)
                    elif new_r > n:
                        new_r = new_r%n
                    if new_r == n:
                        new_r = 0
                    if new_c < 0:
                        new_c = n - (abs(new_c)%n)
                    elif new_c > n:
                        new_c = new_c%n
                    if new_c == n:
                        new_c = 0
                    this_ball[new_r][new_c].append(fire)
    return this_ball

def check_duple_ball(this_ball):
    new_ball = [[[] for _ in range(n)] for _ in range(n)]
    for x, row in enumerate(this_ball):
        for y, one in enumerate(row):
            if len(one) >= 2:
                new_m = sum([f[0] for f in one]) // 5
                if new_m == 0:
                    continue
                new_s = sum([f[1] for f in one]) // len(one)
                if not check_diff(one):
                    for new_d in range(0, 7, 2):
                        new_ball[x][y].append((new_m, new_s, new_d))
                else:
                    for new_d in range(1, 8, 2):
                        new_ball[x][y].append((new_m, new_s, new_d))
            else:
                new_ball[x][y] = one
    return new_ball

def check_diff(target):
    is_odd = -1
    is_even = -1
    for row in target:
        if row[2] % 2 == 0:
            is_even = 1
        else:
            is_odd = 1
    return bool(is_even + is_odd)

for _ in range(k):
    # 1. 모든 파이어볼 이동
    this_ball = move_fire_ball(fire_ball)

    # 2. 2개 이상 확인
    fire_ball = check_duple_ball(this_ball)

all_ball = 0
for row in fire_ball:
    for one in row:
        all_ball += sum([sep[0] for sep in one])
print(all_ball)

