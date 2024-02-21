"""
2부터 N까지 모든 정수를 적는다.
아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.
"""

import sys
sys.stdin = open("input.txt")
n, k = map(int, input().split())

num_list = ([False] * 2) + ([True] * (n-1))

def check_is_prime(a):
    for i in range(2, a//2+1):
        if a % i == 0:
            return False
    return True

cnt = 0
while True:
    for idx, num in enumerate(num_list):
        if not num:
            continue
        # 소수인가? idx로 확인하기
        if check_is_prime(idx):
            i = 1
            while idx*i < len(num_list):
                if num_list[idx*i]:  # 아직 살아있는 값이면 삭제해주기
                    num_list[idx*i] = False
                    cnt += 1
                    if cnt == k:
                        print(idx*i)
                        sys.exit()
                i += 1
            continue




