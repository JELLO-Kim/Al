# 4번 실행됨.
for i in range(4) :
    N = int(input())
    for i in range(1, N+1):
        if i%2==1 :
            print((" "*(N-i))+("* "*i).rstrip())
        else:
            print((" "*(N-i))+("* "*i).rstrip())
# 한번 실행됨 / for문과 if문 중첩 사용
N = int(input())
for i in range(1, N+1):
    if i%2==1 :
        print((" "*(N-i))+("* "*i).rstrip())
    else:
        print((" "*(N-i))+("* "*i).rstrip())

#for문만 사용
N=int(input())
for i in range(1, N+1):
    print(' '*(N-i)+('* '*i).rstrip())
