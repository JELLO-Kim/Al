import sys
sys.stdin = open("input.txt")

parent = [i for i in range(10**6+1)]
set_size = [1 for _ in range(10**6+1)]
parent_dict = {}

def check_parent(x):
    if parent[x] != x:
        parent[x] = check_parent(parent[x])
    return parent[x]

order_list = []
for _ in range(int(input())):
    order_list.append(list(input().split()))

for order in order_list:
    if order[0] == "I":
        a = int(order[1])
        b = int(order[2])
        a_parent = check_parent(a)
        b_parent = check_parent(b)
        if a_parent < b_parent:
            parent[b_parent] = a_parent
            set_size[a_parent] += set_size[b_parent]
            set_size[b_parent] = 0
        elif a_parent > b_parent:
            parent[a_parent] = b_parent
            set_size[b_parent] += set_size[a_parent]
            set_size[a_parent] = 0
    else:
        num_parent = check_parent(int(order[1]))
        print(set_size[num_parent])
