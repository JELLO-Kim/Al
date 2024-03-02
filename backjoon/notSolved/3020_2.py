import sys

sys.stdin = open("input.txt")
n, h = map(int, input().split())

cave = [0] * h
bottom = [0] * h
top = [0] * h
for i in range(n):
    stone = int(input())
    if i == 0 or i%2==0:
        # 석순 # 바닥에 있어야댐..
        bottom[i] += stone
    else:
        top[i] += stone

new_bottom = [0]*h
new_top = [0]*h
new_bottom[0] = bottom[0]
new_top[0] = top[0]
for i in range(1, h):
    new_bottom[i] = bottom[i] + new_bottom[i-1]
    new_top[i] = top[i] + new_top[i - 1]
print()
answer = [0]*h
# for i in range(h):
#     answer[i] =

answer = [top[i] + bottom[i] - 6 for i in range(h)]
min = 200001
count = -1
for idx in range(len(answer)):
    if answer[idx] < min:
        min = answer[idx]
        count = 1
    elif answer[idx] == min:
        count += 1
print(min, count)


# lt = 0
# rt = n-1
# break_list = [0]*h
#
# for h_idx in range(h):
#     break_mid = 0
#     for s_idx, s_num in enumerate(stone_list):
#         if s_idx == 0 or s_idx%2 == 0:
#             # 짝수면 석순이다.
#             break_stone = (h_idx + s_num) - (h-1)
#             if break_stone > 0:
#                 break_mid += 1
#         else:
#             # 홀수면 종유석이다.
#             if h_idx <= s_num-1:
#                 break_mid += 1
#
#     # 해당 높이에서 부순 장애물 기록하기
#     break_list[h_idx] = break_mid
# print(min(break_list), break_list.count(min(break_list)))