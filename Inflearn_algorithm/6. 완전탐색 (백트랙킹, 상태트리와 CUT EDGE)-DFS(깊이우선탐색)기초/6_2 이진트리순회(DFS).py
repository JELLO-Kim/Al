# 전위순회 : 루트노드 기준 본인 출력 후 왼쪽노드 우선
# 중위순회 : 왼쪽자식, 부모, 오른쪽 자식
# 후위순회 : 왼쪽자식, 오른쪽 자식, 부모

def forwardDFS(v):
    if v > 7:
        return
    else:
        print(v, end = "")
        forwardDFS(v*2)  # 왼쪽 노드
        forwardDFS(v*2+1)  # 오른쪽 노드


def middleDFS(v):
    if v>7:
        return
    else:
        middleDFS(v*2)  # 왼쪽 노드
        print(v, end = "")
        middleDFS(v*2+1)  # 오른쪽 노드


def backDFS(v):
    if v>7:
        return
    else:
        backDFS(v*2)  # 왼쪽 노드
        backDFS(v*2+1)  # 오른쪽 노드
        print(v, end = "")

forwardDFS(1)
print("==============================")
middleDFS(1)
print("==============================")
backDFS(1)
    