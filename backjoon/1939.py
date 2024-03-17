import sys
sys.stdin = open("input.txt")
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
costs = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    costs.append(c)

# 공장 있는 위치 번호
start, end = map(int, input().split())

def dijk(limit):
    dist = [sys.maxsize] * (n+1)
    edge = []
    heapq.heappush(edge, (0, 0, start))
    while edge:
        total_cost, this_cost, this_node = heapq.heappop(edge)
        for next_node, next_cost in graph[this_node]:
            if next_cost < limit:
                continue
            # 기존 값과 비교
            if dist[next_node] > total_cost + next_cost:
                dist[next_node] = total_cost+next_cost
                heapq.heappush(edge, (total_cost+next_cost, next_cost, next_node))

    if dist[end] == sys.maxsize:
        return False
    return True

# 이분탐색으로 무게 구하기
costs.sort()
lt = 0
rt = len(costs) -1
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    mid_cost = costs[mid]
    check = dijk(mid_cost)
    if check:
        # 지나갈수 있음! 무게 더 줄여보기
        lt = mid + 1
        res = max(res, mid_cost)
    else:
        rt = mid - 1

print(res)

