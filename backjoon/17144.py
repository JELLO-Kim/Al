import sys
sys.stdin = open("input.txt")

r, c, t = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def spread_dust(x, y):
    spread_count = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < r and 0 <= yy < c and dust[xx][yy] != 1:
            dust[xx][yy] += (dust[x][y] // 5)
            spread_count += 1
    # 잔여 미세먼지 계산
    dust[x][y] -= (dust[x][y]//5)*spread_count

air_x = []
for _ in range(t):
    visit = [[False] * (c) for _ in range(r)]
    # 1 확산하기 + 공기청정기 위치 확인
    for x in range(r):
        for y in range(c):
            if dust[x][y] == -1:
                if len(air_x) < 2:
                    air_x.append(x)
            elif dust[x][y] > 0:
                spread_dust(x, y)

    # 2 공기청정기 가동
    r_clock = [0, air_x[0]]
    o_clock = [0, air_x[1]]

