# 마구간 정하기
# N : 마구간 수
# C : 말 수
"""
5 3
1
2
8
4
9
출력 : 3
"""
N, C, *house = map(int, open("input.txt").read().split())
lt = 1
house.sort()
rt = max(house)

def Count(diff):
    in_horse = 1
    set_one = house[0]
    for j in range(1, N):
        if house[j] - set_one >= diff:
            in_horse += 1
            set_one = house[j]
    return in_horse

res = max(house)
while lt <= rt:
    mid = (lt+rt)//2

    if Count(mid) >= C:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
print(res)