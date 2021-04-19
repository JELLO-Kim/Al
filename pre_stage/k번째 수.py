import sys
T = int(input())
for t in range(T): # test 케이스 만큼 반복진행하도록 한다.
    n, s, e, k = map(int, input().split()) # n=주어진 자연수, s=시작순서, e=종료순서, k=구하고자 하는 index
    t1= list(map(int, input().split()))

    t1=t1[s-1:e]
    t1.sort()
    print(f"#{t+1}", t1[k-1])