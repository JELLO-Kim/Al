import sys
sys.stdin=open("input.txt", "r")

# 전위순회 / 중위순회 / 후위순회

def DFS(x):
    if x>7: # 7까지만 출력
        return
    else:
        # 전위순회
        print(x, end=' ')
        DFS(x*2)
        DFS(x*2+1)

        # 중위순회
        DFS(x*2)
        print(x, end=' ')
        DFS(x*2+1)

        # 후위순회 ex)병합정렬
        print(x)
        DFS(x*2)
        DFS(x*2+1)
        print(x, end=' ')

if __name__='__main__':
    DFS(1)