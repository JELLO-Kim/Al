import sys

def DFS(x):
    if x == n :
        p_sum = sum(p_list)
        if sum(num_list) - p_sum == p_sum:
            print("YES")
            sys.exit()
    else:
        p_list.append(num_list[x])
        DFS(x+1)
        p_list.pop()
        DFS(x+1)

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))
    p_list = list()
    DFS(0)
    print("NO")
