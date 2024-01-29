import sys
sys.stdin = open("input.txt", "r")

n = int(input())
h_list = [list(map(int, input().split())) for _ in range(n)]
h_list.insert(0, [0,0])

max = -217400000
def DFS(days, money):
    global max
    if days==n+1:
        if max < money:
            max = money
        return
    if days + h_list[days][0] > n+1:
        return
    DFS(days+h_list[days][0], money+h_list[days][1])
    DFS(days+1, money)  # 그냥 다음날짜

DFS(1, 0)
print(max)