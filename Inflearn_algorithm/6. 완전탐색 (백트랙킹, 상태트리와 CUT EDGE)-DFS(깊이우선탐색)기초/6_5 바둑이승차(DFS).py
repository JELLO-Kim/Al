import sys
sys.stdin = open("input.txt", "r")


""" 부분 집합을 구하고 그중에 조건 내 최대값 구하기 """

def DFS(i, sum, t_sum):
    global result
    if sum + (total-t_sum) < result:
        return
    if C < sum:
        return
    if i == N:
        if result < sum:
            result = sum
    else:
        DFS(i+1, sum+num_list[i], t_sum+num_list[i])
        DFS(i+1, sum, t_sum+num_list[i])

if __name__ == "__main__":
    C, N = map(int, input().split())
    num_list = [int(input()) for _ in range(N)]
    result = -2174000000
    DFS(0, 0, 0)
    total = sum(num_list)
    print(result)