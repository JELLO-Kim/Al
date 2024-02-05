#두개의 for문 활용
N = int(input())
for i in range(1, N+1) :
    print((" "*(i-1))+"*"*((N*2)-(i*2-1)))
for k in range(1, N) :
    print((" "*(N-k-1))+"*"*(k*2+1))

#if문과 for문의 중첩 활용
N  = int(input())
for i in range(1, N+1):
    if i!=5:
        print((" "*(i-1))+"*"*((N*2)-(i*2-1)))
    elif i==5:
        for i in range(1, N+1):
            print((" "*(N-i))+"*"*(i*2-1))