import sys
from itertools import combinations
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리기
sys.stdin = open("input.txt")
n, m = map(int, input().split())
tmpp = list(map(int, input().split()))
parent = [i for i in range(n+1)]
truth_pp = tmpp[1:]

if not truth_pp:
    root_truth_pp = 0
else:
    root_truth_pp = min(truth_pp)
    for i in tmpp[1:]:
        parent[i] = root_truth_pp

party_info = []
for _ in range(m):
    tmp = list(map(int, input().split()))[1:]
    min_root = max(tmp)
    for y in tmp:
        min_root = min(min_root, parent[y]) # 최단 root 값 구하기
    for yy in tmp:
        parent[yy] = min_root
        # if parent[y] > min_root:
        #     parent[y]
        # if y in truth_pp:
        #     for yy in tmp:
        #         parent[yy] = root_truth_pp
        #     break
    party_info.append(tmp)

lie_count = 0
for party in party_info:
    for one in party:
        if parent[one] == root_truth_pp:
            break
    else:
        lie_count += 1
print(lie_count)


# def check_parent(x):
#     if parent[x] != x:
#         parent[x] = check_parent(parent[x])
#     return parent[x]
#
# def check_lie(party_tuple):
#     lie_count = 0
#     for mm in party_tuple:
#         party_in = party_info[mm]
#         for one in party_in:
#             one_parent = check_parent(one)
#             if one_parent == root_truth_pp:
#                 break
#         else:
#             lie_count += 1
#     return lie_count
# # 파티참석하면서 구라횟수 진실횟수 카운팅
# lt = 0
# rt = m
# res = 0
# def sol1():
#     while lt <= rt:
#         mid = (lt + rt) // 2
#         # mid 개 파티를 참석하는 경우의 수 모두 뽑기
#         for i in combinations([j for j in range(m)], mid):
#             if check_lie(i) == mid:
#                 lt = mid + 1
#                 # 참석 갯수만큼 거짓말 칠수 있으므로 답으로 기록한다.
#                 res = max(res, mid)
#                 break
#         else:
#             rt = mid -1
#     print(res)