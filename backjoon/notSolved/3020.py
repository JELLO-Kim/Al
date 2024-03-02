import sys

sys.stdin = open("input.txt")
n, h = map(int, input().split())

n_idx = 0

stone_list = [int(input()) for _ in range(n)]

lt = 0
rt = n-1
break_list = {}
break_mid = 0
while lt <= rt:
    mid = (lt + rt) // 2
    mid_break_available = 0
    # 모든 높이구간 확인하기
    for h_idx in range(h):
        break_mid = 0
        for s_idx, s_num in enumerate(stone_list):
            if s_idx == 0 or s_idx%2 == 0:
                # 짝수면 석순이다.
                break_stone = (h_idx + s_num) - (h-1)
                if break_stone > 0:
                    break_mid += 1
            else:
                # 홀수면 종유석이다.
                if h_idx <= s_num-1:
                    break_mid += 1
            # 더 많이 뿌셨으면 바로 다음줄 확인
            if break_mid > mid:
                break
        if break_mid == mid:
            mid_break_available += 1
        elif break_mid < mid:
            # 더 적게 뿌셨다!! 범위 바로 줄이자
            rt = mid -1
            break
    else:
        # 뿌술 수 있고, 이보다 더 적게 뿌순 기록이 없으면 그냥 얘가 답이다.
        if mid_break_available > 1:
            print(mid, mid_break_available)
            break
        else:  # 주어진 경우로는 탈출 불가능 하다면 더 뿌수게 한다.
            lt = mid + 1