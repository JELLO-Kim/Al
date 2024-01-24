# 카드 역배치 
"""
1~20까지 있는 카드배치에서 [a, b] 구간의 위치를 역순으로 바꾸기
"""
# 정답 : 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
import sys

def my_sol():
    """
    직접 확인하지 않고 reverse 활용함
    """
    set_list = list(map(int, open("input.txt").read().split()))

    card_set = [str(i) for i in range(0, 21)]
    for i in range(0, len(set_list)-1):
        card_set[set_list[i]:set_list[i+1]+1] = card_set[set_list[i+1]:set_list[i]-1:-1]
    print(" ".join(card_set[1:]))
    # 출력 : 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

def sol():
    """
    하나씩 자리 바꿔줌
    """
    sys.stdin = open("input.txt", "rt")
    a = list(range(21))
    for _ in range(10):
        s, e = map(int, input().split())
        for i in range((e-s+1)//2):
            a[s+i], a[e-i] = a[e-i], a[s+i]
    print(" ".join(map(str, a[1:])))
    # 출력 : 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
sol()