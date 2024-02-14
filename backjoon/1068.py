import sys
sys.stdin = open("input.txt", "r")

node_count = int(input())
node_list = list(map(int, input().split()))
delete_node = int(input())


def dfs(target_node):
    for node_num, parent_node in enumerate(node_list):
        if parent_node == target_node:
            node_list[node_num] = -2
            dfs(node_num)

def check(target_num):
    global leef_node_count
    if target_num not in node_list:
        # 이녀석을 부모노드로 삼는 것이 없음 = 리프노드!
        leef_node_count[target_num] = "1"
    else:
        # 이녀석을 부모노드로 갖는 자식노드들을 더 탐색한다.
        for node_num, parent_node in enumerate(node_list):
            if parent_node == target_num:
                check(node_num)

leef_node_count = ["0"]*node_count
for node_num, parent_node in enumerate(node_list):
    if node_num == delete_node:
        # 지우기 작업 시작
        node_list[node_num] = -2
        dfs(node_num)

        # 리프노드 추출하기
        for node_num, parent_node in enumerate(node_list):
            if leef_node_count[node_num] == "0" and parent_node >= -1:
                check(node_num)
        aa = eval("+".join(leef_node_count))
        print(aa)
        break
