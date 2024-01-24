# 주어진 조건대로 이중배열 속 단일 배열 회전 후 모래시계 모양대로 숫자 더하기
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
gam_list = [list(map(int, input().split())) for _ in range(5)]
m = int(input())
for _ in range(m):
    row, way, num = map(int, input().split())
    for _ in range(num):
        if way == 0:  # 왼쪽으로
            gam_list[row-1].append(gam_list[row-1].pop(0))
        else:
            gam_list[row-1].insert(0,gam_list[row-1].pop())

s=0
e=n-1
gam_sum = 0
for idx, gam in enumerate(gam_list):
    for i in range(s, e+1):
        gam_sum += gam[i]
    if idx < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(gam_sum)
