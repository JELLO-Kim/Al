import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리기
sys.stdin = open("input.txt")
n, m = map(int, input().split())
parent = [i for i in range(n+1)] # 앞 : 원소 / 뒤 : 부모

def check_union(x):
    if parent[x] != x:
        parent[x] = check_union(parent[x])
    return parent[x]

for _ in range(m):
    act, a, b = map(int, input().split())
    if act == 0:
        # 더 작은 부모노드를 다른 부모노드의 부모노드로 승격
        a_parent = check_union(a)
        b_parent = check_union(b)
        if a_parent < b_parent:
            parent[b_parent] = a_parent
        else:
            parent[a_parent] = b_parent
    else:
        # act == 1 => a와 b가 같은 집합인지 확인한다.
        a_check = check_union(a)
        b_check = check_union(b)
        if a_check == b_check:
            print("YES")
        else:
            print("NO")
