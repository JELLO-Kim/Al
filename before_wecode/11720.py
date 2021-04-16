N=int(input())
n=list(input())
sum = 0
for i in n:
    sum += int(i)
print(sum)

#다른 사람 코드
input()
print(sum(map(int,input())))