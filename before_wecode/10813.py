N, M = map(int, input().split())

bucket_init = [str(i) for i in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    bucket_init[a-1], bucket_init[b-1] = bucket_init[b-1] , bucket_init[a-1]
print(*bucket_init)