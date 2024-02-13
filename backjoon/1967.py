"""
시작점을 기준으로 연결된 가장 최 하위 노드까지 모조리 탐색 후 max값 가져오기
visit 체크하기
"""


import sys, time
start = time.time()
sys.stdin = open("input.txt")

n = int(input())
parent_check = set()
r = {}
for _ in range(n-1):
    p, c, w = map(int, input().split())
    parent_check.add(p)
    if p in r:
        r[p].append([c, w])
    else:
        r[p] = [[c, w]]
    if c in r:
        r[c].append([p, w])
    else:
        r[c] = [[p, w]]

leef_nods = []
for i in range(1, n+1):
    if i not in list(parent_check):
        leef_nods.append(i)



total_weight = 0
def dfs(p, w, is_start=True):
    global total_weight
    # 리프노드에 도달했다면 종료하기
    if p in leef_nods and not is_start:
        total_weight = max(total_weight, w)
    else:
        for linked_nodes in r[p]:
            if not visit[linked_nodes[0]]:
                visit[linked_nodes[0]] = True
                dfs(linked_nodes[0], w+linked_nodes[1], False)
                visit[linked_nodes[0]] = False

# 1부터 n 까지 시작점으로 잡기
for one in range(1, n+1):
    visit = [False] * (n+1)
    visit[one] = True
    dfs(one, 0)
print(total_weight)
# 자식노드가 2개 이상인 경우 한쪽으로 선택할 수 있다.
# 자식노드가 1개라면 무조건 선택해야 한다.
end = time.time()
print(f"소요시간 : {end-start}")