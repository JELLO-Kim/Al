import sys
sys.stdin = open("input.txt")

T = int(input())
all_case = []
all_name = []
for _ in range(T):
    one_case = []
    one_all_names = []
    case_one_count = int(input())
    for _ in range(case_one_count):
        tmp = list(input().split())
        one_all_names.extend(tmp)
        one_case.append(tmp)
    all_name.append(list(set(one_all_names)))
    all_case.append(one_case)

def check_parent(x):
    if parent_dict[x] != x:
        parent_dict[x] = check_parent(parent_dict[x])
    return parent_dict[x]

# parent 구하기
for i in range(T):
    parent_dict = {}
    rank = {}
    group_count = {}
    for j in all_name[i]:
        parent_dict[j] = j
        rank[j] = 1
        group_count[j] = 1
    for row in all_case[i]:
        a_parent = check_parent(row[0])
        b_parent = check_parent(row[1])
        this_parent = None
        # rank를 비교해서 더 작은 랭크가 더 큰 랭크에 붙도록 한다.
        if rank[a_parent] < rank[b_parent]: # b가 레벨이 더 적다
            parent_dict[a_parent] = b_parent
            # b 그룹에 a 그룹이 합쳐진다.
            group_count[b_parent] += group_count[a_parent]
            group_count[a_parent] = 0
            this_parent = b_parent
        elif rank[a_parent] > rank[b_parent]:
            parent_dict[b_parent] = a_parent
            this_parent = a_parent
            # a 그룹에 b 그룹이 합쳐진다.
            group_count[a_parent] += group_count[b_parent]
            group_count[b_parent] = 0
        else: # 두개의 랭크가 같다면 임의로 a 쪽으로 붙여준다
            parent_dict[b_parent] = a_parent
            rank[a_parent] += 1
            this_parent = a_parent
            # a 그룹에 b 그룹이 합쳐진다.
            group_count[a_parent] += group_count[b_parent]
            group_count[b_parent] = 0
        # value가 this_parent 인 값 찾기
        print(group_count[this_parent])