import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

def DFS(L, sum, t):
    global max
    if t > m:
        # # 시간 넘었으면 직전걸로 빼주고 확인하기
        # sum -= p_list[L-1][0]
        # if sum > max:
        #     max = sum
        #     return
        return
    if L == n:
        if sum > max:
            max = sum
            return
        return
    else:
        # 이번 점수 더한거
        DFS(L+1, sum+p_list[L][0], t+p_list[L][1])
        # 이번 점수 안더한거
        DFS(L+1, sum, t)



p_list = list()
for _ in range(n):
    a, b = map(int, input().split())
    p_list.append((a, b))

max = -2174000
DFS(0, 0, 0)
print(max)