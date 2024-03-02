import sys
sys.stdin = open("input.txt")
n, k = map(int, input().split())
lv = [int(input()) for _ in range(n)]


lt = min(lv)
rt = (sum(lv) + k) // n
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    do_k = 0
    for i in lv:
        # mid 값이 되도록 k 값에서 빼서 더해주기
        if mid > i:
            do_k += mid - i
    # 만약 do_k 값이 k 보다 크다면 배분 레벨이 더 크다는 것이므로 목표레벨을 낮춘다
    if do_k > k:
        rt = mid-1
    else:
        # 만약 목표치만큼 채웠는데 do_k 값이 k 보다 작거나 같다면 목표치를 늘려도 된다
        lt = mid + 1
        res = max(res, mid)
print(res)  # 17
print(lt)  # 18 -> 정답 아님!
print(rt)  # 17
