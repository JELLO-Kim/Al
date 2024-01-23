# 배열 뒤집기
# N, M, *bucket_set = open("input.txt").read().split()
# print(N)
# print(M)
# print(bucket_set)
# N, M = NM.strip().split()
# bucket_list = [str(i) for i in range(1, int(N)+1)]
# for i in bucket_set:
#     from_b, to_b = map(int, i.strip().split())
#     tmp_set = bucket_list[from_b-1: to_b]
#     tmp_set.reverse()
#     bucket_list[from_b-1:to_b] = tmp_set

# print(" ".join(bucket_list))

"""
python 의 list [::] 활용한 방법
"""
N,M,*l=map(int,open("input.txt").read().split())
*A,=range(N+1)
while l:
    i,j,*l=l
    A[i:j+1]=A[j:i-1:-1]
print(*A[1:])