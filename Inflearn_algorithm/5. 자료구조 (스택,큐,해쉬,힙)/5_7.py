# 교육과정 설계 (큐)
"""
입력 :
CBA
3
CBDAGE
FGCDAB
CTSBDEA
출력 : 
#1 YES
#2 NO
#3 YES
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

def my_sol():
    need = input()
    N = int(input())
    study_list = [input() for _ in range(N)]
    
    for idx, row in enumerate(study_list):
        now_q = deque(row)
        check_count = 0
        while check_count < N:
            a = now_q.popleft()
            if check_count != 0:
                if a == need[check_count]:
                    check_count += 1
                else:
                    if a in need:
                        print(f"#{idx+1} NO")
                        break
                    else:
                        now_q.append(a)
            else:
                if a == need[check_count]:
                    check_count += 1
                else:
                    now_q.append(a)
        if check_count == N:
            print(f"#{idx+1} YES")

def sol():
    need = input()
    N = int(input())
    study_list = [input() for _ in range(N)]
    for idx, plan in enumerate(study_list):
        dq = deque(need)
        for x in plan:
            if x in dq:
                if x != dq.popleft():
                    print(f"#{idx+1} NO")
                    break
        else:
            if len(dq) > 0:
                print(f"#{idx+1} NO")
            else:
                print(f"#{idx+1} YES")


sol()