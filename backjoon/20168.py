import sys
input = sys.stdin.readline
n, m, a, b, c = map(int, input().split())
road = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    from_c, to_c, cost = map(int, input().split())
    road[from_c][to_c] = cost
    road[to_c][from_c] = cost

res_max_min = sys.maxsize
def dfs(from_city, total_cost, max_cost):
    global res_max_min
    if total_cost > c:
        return
    if from_city == b:
        res_max_min = min(res_max_min, max_cost)
        return
    for to_city, to_cost in enumerate(road[from_city]):
        if to_cost != 0 and not visit[to_city]:
            visit[to_city] = True
            dfs(to_city, total_cost+to_cost, max(max_cost, to_cost))
            visit[to_city] = False
visit = [False] * (n+1)
visit[0] = True
visit[a] = True
dfs(a, 0, 0)
if res_max_min == sys.maxsize:
    res_max_min = -1
print(res_max_min)