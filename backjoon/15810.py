import sys
sys.stdin = open("input.txt")

staff, ba = map(int, input().split())
times = list(map(int, input().split()))

lt = 1
rt = max(times) * ba
res = rt
while lt <= rt:
    mid = (lt + rt) // 2
    # 총 소요시간이 mid일때 몇개까지 풍선을 불 수 있는가
    total_balloon = 0
    for one in times:
        # 불고나서 몇분 남았다 해도 그 시간안에 부는것 완성 못하므로 나머지는 버린다.
        total_balloon += mid//one
    if total_balloon >= ba:
        # 목표갯수와 같거나 보다 많다면 총 소요시간을 줄여본다
        rt = mid - 1
        res = min(res, mid)
    else:
        # 목표갯수보다 모자르다면 총 소요시간을 늘려준다
        lt = mid + 1
print(res)