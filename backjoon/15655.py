import sys
# import copy
from itertools import combinations
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
# done_ch = []

# def DFS(l, ch):
#     if l == m:
#         # 중복 체크
#         tmp = copy.deepcopy(ch)
#         tmp.sort()
#         if tmp not in done_ch:
#             done_ch.append(copy.deepcopy(ch))
#             for i in ch:
#                 print(i, end=" ")
#             print("")
#     else:
#         for j in num:
#             if j not in ch:
#                 ch.append(j)
#                 DFS(l+1, ch)
#                 ch.pop()

# ch = []
# for row in num:
#     ch.append(row)
#     DFS(1, ch)
#     ch.pop()

for i in combinations(num, m):
    for a in list(i):
        print(a, end=" ")
    print("")