import sys
# 완벽한 로직이 아님. 정답일때도, 오답일때도 있다...
'''
a, b = map(int, input().split())
a_list=[int(x) for x in str(a)]
stack=[]
maxx=max(a_list[0:-b])
sp=a_list.index(maxx)
trash=0

for i in a_list:
    if not stack:
        stack.append(i)
    else:
        stack.append(i)
        if stack[-1]!=stack[-2]:
            while stack[-1]>stack[-2]:
                    stack.pop(-2)
                    trash+=1
                    if len(stack)==1:
                        break
                    if trash==b:
                        break
            if trash==b:
                stack+=a_list[a_list.index(i)+1:]
                break
lp=len(a_list)-b
stack=stack[:lp]
'''

# 소스코드
num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x: # 반복 조건 : stack이 비어있지 않고 + 제거해야 할 수가 남아있고 + 들어갈 숫자보다 stack의 마지막수가 작을때
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))