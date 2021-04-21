import sys
sys.stdin=open("input.txt", "r")
a=input()
stack=[]
res=0
for idx, i in enumerate(a):
    if i=="(":
        stack.append(i)
    else:
        stack.pop()
        if a[idx-1]=="(": # 직전 괄호가 여는 괄호라면 레이저를 쏜다. 쇠막대기를 절단. 이어서 쇠막대기가 진행된다.
            res+=len(stack)
        else: # 직전 괄호가 닫는 괄호라면 쇠막대기 하나를 종료한다.
            res+=1
print(res)