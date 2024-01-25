# 결정알고리즘에서 활용되는 이분검색
"""
4 11
802
743
457
539
출력 : 200
"""
n, m, *cab_list = map(int, open("input.txt").read().split())
cm_period = max(cab_list)+1

lt = 1
rt = max(cab_list)+1
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    cut_count = 0
    for row in cab_list:
        cut_count += row//mid
    if cut_count == m:
        res = mid
        lt = mid+1
    elif cut_count < m:
        rt = mid-1
    else:
        lt = mid+1
print(res)