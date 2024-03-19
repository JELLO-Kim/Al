import sys
sys.setrecursionlimit(10**6)

sys.stdin = open("input.txt")
city = int(input())
visit_count = int(input())
parent = [i for i in range(city+1)]

def check(x):
    if parent[x] != x:
        parent[x] = check(parent[x])
    return parent[x]

for i in range(1, city+1):
    row_list = [0] + list(map(int, input().split()))
    for j in range(1, len(row_list)):
        if row_list[j] == 1:
            # i의 부모, j의 부모 구하기
            i_parent = check(i)
            j_parent = check(j)
            if i_parent < j_parent:
                parent[j_parent] = i_parent
            else:
                parent[i_parent] = j_parent


# 이동경로 확인하기
visit_plan = list(map(int, input().split()))
for from_city_idx in range(visit_count-1):
    from_city = visit_plan[from_city_idx]
    to_city = visit_plan[from_city_idx+1]
    from_city_parent = check(from_city)
    to_city_parent = check(to_city)
    if from_city_parent != to_city_parent:
        print("NO")
        break
else:
    print("YES")