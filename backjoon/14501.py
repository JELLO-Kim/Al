"""
모든 경우의 수 확인 (DFS) 하고 그중 조건에 맞는 최댓값 구하기
"""

import sys
sys.stdin = open("input.txt","r")
n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
res = set()
def DFS(t_day, earn):
    if t_day == n:
        res.add(earn)
        return
    else:
        res.add(earn)
        day = meet[t_day][0]
        money = meet[t_day][1]
        if t_day + day <= n:
            DFS(t_day + day, earn+money) # 이날꺼 수행
        DFS(t_day+1, earn) # 이날꺼 수행 X

DFS(0, 0)
print(max(list(res)))