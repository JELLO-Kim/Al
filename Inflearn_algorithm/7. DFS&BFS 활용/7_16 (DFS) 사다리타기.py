import sys
sys.stdin = open("../input.txt", "r")
rail = [list(map(int, input().split())) for _ in range(10)]
n = 10
"""
좌 우 확인 해서 1이면 우선 순위
좌 우 모두 0이면 무조건 하강
"""

dx = [0, 0]
dy = [-1, 1]

def dfs(x, y, from_xy):
    if x == 9:  # 젤 아래층 도달
        if rail[x][y] == 2:
            return True
        else:
            return False
    else:
        for i in range(2):
            yy = y + dy[i]
            if 0 <= x < n and 0<= yy < n and [x,yy] != from_xy and rail[x][yy] == 1:
                return dfs(x, yy, [x, y])
        # 좌우가 모두 0이다 -> 아래로 내려간다.
        return dfs(x+1, y, from_xy)

start_x = 0
for start_y in range(n):
    if rail[start_x][start_y] == 1:
        if dfs(start_x, start_y, [0,-1]):
            print(start_y)
            break