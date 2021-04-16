N=int(input())
for i in range(1, N+1):
    if i == 1:
        print(' '*(N-i)+'*')
    elif 1<i<N:
        print(' '*(N-i)+'*'+' '*((i-1)*2-1)+'*')
    else:
        print('*'*(i*2-1))


#리팩토링 후
N=int(input())
for i in range(1, N+1):
    if i == 1 or i == N:
        print(' '*(N-i)+'*'*(i*2-1))
    elif 1<i<N:
        print(' '*(N-i)+'*'+' '*((i-1)*2-1)+'*')