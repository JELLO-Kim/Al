N = int(input())
for i in range(1, N+1) :
    print(("*"*i)+(" "*((N-i)*2)+"*"*i))
for k in range(1, N) :
    print(("*"*(N-k)+(" "*k*2)+"*"*(N-k)))