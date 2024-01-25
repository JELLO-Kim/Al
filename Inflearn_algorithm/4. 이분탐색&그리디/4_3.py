# 뮤직비디오 (결정알고리즘)
"""
9 3
1 2 3 4 5 6 7 8 9
출력 : 17
"""
N, M, *dvd_list = map(int, open("input.txt").read().split())
lt = 1
rt = sum(dvd_list)
answer = 0

def Count(mid):
    cnt = 1
    tmp = 0
    for row in dvd_list:
        if tmp+row > mid:
            cnt += 1
            tmp = row
        else:
            tmp += row
    return cnt


while lt <= rt:
    mid = (lt+rt)//2
    cnt = Count(mid)
    if mid > max(dvd_list) and cnt <= M:
        answer = mid
        rt = mid-1
    else:
        lt =mid+1
print(answer)