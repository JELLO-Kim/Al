import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리기
sys.stdin = open("input.txt")
n, m = map(int, input().split())
pure_group = set(list((map(int, input().split())))[1:])
party_info = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)] # 0 부터 n까지 parent 자기자신 세팅

# 들어온 x 의 root 찾기
def check(x):
    if parent[x] != x:
        parent[x] = check(parent[x])
    return parent[x]

for one in party_info:
    p = one[1:] # 젤 앞 수는 참여인원 수
    p.sort()  # 오름차순 정렬
    p_parent = p[0] # 젤 앞에수가 가장 적으므로 이 그룹내의 parent 로 지정
    for i in p:
        check_p_parent = check(i)
        p_parent = min(p_parent, check_p_parent)
    # 각 값의 root를 p_parent 로 바꾼다.
    for j in p:
        j_parent = check(j)
        parent[j_parent] = p_parent

    # 각 root 확인해서 pure랑 관련있으면 넣는다
    for nods, row in enumerate(parent):
        if nods in pure_group:
            pure_group.add(row)

# 파티체크 하면서 해당 노드의 루트가 거짓그룹에 있는지 확인하기
count = 0
for one_party in party_info:
    one = one_party[1:]
    for i in one:
        if check(i) in pure_group:
            break
    else:
        count += 1

print(count)