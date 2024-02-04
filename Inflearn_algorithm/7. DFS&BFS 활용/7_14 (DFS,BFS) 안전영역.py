# DFS, BFS 모두 풀이 가능 / DFS로 풀어봄
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]


# 체크하고 0으로 만들기 or 빗물이랑 같은 레벨로 만들기도 가능함 / 높이는 1~100
# 확인필요한 영역 = 최소값 ~ 최대값 까지
min_rain = 101
max_rain = 0
for row in city:
    if min_rain > min(row):
        min_rain = min(row)
    if max_rain < max(row):
        max_rain = max(row)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

sys.setrecursionlimit(10**6)
def DFS(x, y, rain):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i] 
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and city[xx][yy] > rain and ch[xx][yy] == 0:
            DFS(xx, yy, rain)



check_rain = [a for a in range(min_rain, max_rain+1)] # 이하로 잠긴다.
max_safe = 0
for rain in check_rain:
    ch = [[0]*n for _ in range(n)]
    safe_land = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] > rain and ch[i][j] == 0:
                DFS(i, j, rain)
                safe_land += 1
    max_safe = max(max_safe, safe_land)
print(max_safe)
