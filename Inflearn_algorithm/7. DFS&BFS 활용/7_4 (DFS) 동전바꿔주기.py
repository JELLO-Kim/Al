import sys
from time import time
sys.stdin = open("input.txt", "r")
start = time()

T = int(input())
k = int(input())
# def my_sol():
    # # 실패 ㅜㅜ
    # coin_list = []
    # total_count = 0
    # for _ in range(k):
    #     coin, count = map(int, input().split())
    #     coin_list.append([coin, count])
    #     total_count += count
    # # {5: 3, 10: 2, 1: 5}


    # def DFS(idx, sum, count):
    #     global cnt
    #     # 동전 갯수 완료
    #     if count == total_count:
    #         return
    #     # 금액 완료
    #     if sum == T:
    #         cnt += 1
    #         print(f" 20 이다 ~~~ {ch}")
    #         return
    #     if ch[coin_list[idx][0]] == 0:  # 해당 코인 다 씀
    #         return
    #     for i in range(k-idx):
    #         # 이 코인 씀
    #         ch[coin_list[idx][0]] -= 1
    #         DFS(idx+i, sum + coin_list[idx][0], count+1)
    #         # 이 코인 안씀
    #         ch[coin_list[idx][0]] += 1
    #         DFS(idx+i, sum, count+1)

    # res = set()
    # cnt = 0
    # # 모든 동전갯수의 합
    # ch = {one_coin[0]:one_coin[1] for one_coin in coin_list}
    # # {5: 3, 10: 2, 1: 5}
    # DFS(0, 0, 1)
    # print(cnt)  # 375 나옴...

coin_list = []
for _ in range(k):
    # coin, count = map(int, input().split())
    coin_list.append(list(map(int, input().split())))
cnt = 0
def DFS(c_idx, sum):
    global cnt
    if sum > T:
        return
    if c_idx == k:
        if sum == T:
            cnt += 1
    else:
        for c_count in range(coin_list[c_idx][1]+1):
            DFS(c_idx+1, sum + coin_list[c_idx][0]*c_count)

DFS(0, 0) # L : coin idx / sum
print(cnt)
end = time()
print(f"소요시간 : {end-start}") # 0.00011587142944335938