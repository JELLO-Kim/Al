import sys, time
sys.stdin = open("input.txt")
start = time.time()
n = int(input())
stones = list(map(int, input().split()))

aa = [[False]*(max(stones) - min(stones)+1) for _ in range(n)]
def dfs(i, k):
    global res_k
    if i == n-1:
        res_k = min(res_k, k)
        return
    for j in range(i+1, n):
        # j 번째 이용하는데 동일조건 결과값이 이미 있으면 확인 하지 않는다
        if not aa[j-i][abs(stones[i]-stones[j])]:
            new_k = (j - i) * (1+ abs(stones[i] - stones[j]))
            aa[j - i][abs(stones[i] - stones[j])] = True
            dfs(j, new_k)

res_k = n*max(stones)
dfs(0, 0)
print(res_k)
# def dfs2(i, k):
#     global all_k
#     if i == n-1:
#         all_k.append(k)
#         return
#     for j in range(i+1, n):
#         # j 번째 이용
#         new_k = (j - i) * (1+ abs(stones[i] - stones[j]))
#         dfs(j, new_k)
#
# all_k = []
# dfs2(0, 0)
# print(min(all_k))
print(f"소요시간 : {time.time() - start}")