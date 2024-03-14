import sys
sys.stdin = open("input.txt")
n, m, a, b, c = map(int, input().split())
road = [[] for _ in range(n+ 1)] # index가 교차로 (n+1), 이어지는골목과 비용을 append 한다
for _ in range(m):
    from_c, to_c, cost = map(int, input().split())
    # 양방향 골목이므로 두번 삽입
    road[from_c].append((to_c, cost))
    road[to_c].append((from_c, cost))

res_max_min = sys.maxsize
def dfs(from_city, total_cost, max_cost):
    global res_max_min
    # 경로의 총 비용이 소지한 비용을 넘어서면 return
    if total_cost > c:
        return
    # 위의 validation을 통과하고, 도착지점에 도착하면 값 갱신
    if from_city == b:
        res_max_min = min(res_max_min, max_cost)
        return
    # !! 목표 교차로는 탐색 중 도달 시 visit 체크하면 안되기 때문에 이곳에서 체크하고 그 뒤를 탐색한다.
    # 비용미초과, 도착지점 미도달 상태라면 계속해서 탐색
    for to_city, to_cost in road[from_city]:
        if not visit[to_city]:
            visit[from_city] = True
            dfs(to_city, total_cost+to_cost, max(max_cost, to_cost))
            visit[from_city] = False

visit = [False] * (n+1)
visit[0] = True
visit[a] = True

dfs(a, 0, 0)
if res_max_min == sys.maxsize:
    res_max_min = -1
print(res_max_min)