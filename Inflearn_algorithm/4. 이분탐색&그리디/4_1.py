# 이분검색
"""
8 32
23 87 65 12 57 32 99 81
출력 : 3
"""
def my_sol():
    # 이분탐색이 뭔지 모르는 상태임
    n, m, *num_list = open("input.txt", "r").read().split()
    num_list.sort()
    print(num_list.index(m)+1)

def sol():
    # 이분검색 활용
    """
    lt [0], rt [-1] 활용
    mid = (lt + rt)// 2
    """
    n, m, *num_list = open("input.txt", "r").read().split()
    num_list.sort()
    lt = 0
    rt = int(n)-1
    while lt <= rt:
        mid = (lt + rt)// 2
        if num_list[mid] > m:
            # rt -= 1
            rt = mid-1
        elif num_list[mid] == m:
            print(mid+1)
            break
        else:
            # lt += 1
            lt = mid+1
sol()