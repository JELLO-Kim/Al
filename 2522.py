# #if 문 활용하기
N = int(input())
for i in range(1, N+1) :
    if i != 3 :
        print(" "*(N-i)+"*"*i)
    elif i == 3 :
        for i in range(1, N+1) :
            print(" "*(i-1)+"*"*(N-i+1))


#두개의 for문 활용하기
N = int(input())
for i in range(1, N+1) :
    print(" "*(N-i)+"*"*i)
for k in range(1, N) :
    print(" "*k+"*"*(N-k))