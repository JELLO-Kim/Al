import sys
import math
sys.stdin=open("input.txt", "r")

# 내가 푼 방식 : 재귀함수 사용 안함
def DFS(x):
    cnt=[]
    t=0
    while True:
        a = x//2**t
        if a < 1:
            cnt.append(2**(t-1))
            x-=(2**(t-1))
            t=0
        else:
            t+=1
        if x == 0:
            break
    cnt.sort()
    k=0
    i=cnt[-1]
    while i!=1:
        k+=1
        i=i//2
    answer=[0]*(k+1)
    for j in cnt:
        answer[int(math.log2(j))]=1
    answer=answer[::-1]
    an=''
    for i in answer:
        an+=str(i)
    return an

if __name__=='__main__':
    n=int(input())
    DFS(n)

# 십진수를 이진수를 바꾸는 법 활용 & 재귀함수 사용
def DFS(x):
    if x==0:
        return
    DFS(x//2)
    print(x%2, end='')

if __name__=='__main__':
    n=int(input())
    DFS(n)