# 회의실 배정
# 그리디는 정렬과 동반된다.
"""
5
1 4
2 3
3 5
4 6
5 7
출력 : 3
"""
import sys
sys.stdin = open("input.txt", "r")
N = int(input())
meet_times = []
for _ in range(N):
    meet_times.append(list(map(int, input().split())))

# 끝나는 시간대로 정렬해주기 : 회의빨리끝나는게 중요하니까
meet_times.sort(key=lambda x: x[1])
do_meet = 0
pre_meet = [0,0]
for i in range(0, N):
    if meet_times[i][0] >= pre_meet[1]:
        do_meet +=1
        pre_meet = meet_times[i]
print(do_meet)