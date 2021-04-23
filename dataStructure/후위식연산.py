import sys
n=input()
num=[]
for i in n:
    if i.isdecimal(): # 입력된 값들 중 숫자만 포함한다
        num.append(int(i))
    else:
        if i=="+": # 입력된 값이 연산시 + 라면 숫자 뒤에서 두번째 거에서 제일 마지막 수를 더한다. (계산된 수는 없어진다)
            num[-2]=num[-2]+num[-1]
            num.pop()
        if i=="-":
            num[-2]=num[-2]-num[-1]
            num.pop()
        if i=="*":
            num[-2]=num[-2]*num[-1]
            num.pop()
        if i=="/":
            num[-2]=num[-2]/num[-1]
            num.pop()
print(num[0]) # list 형태로 들어있기 때문에 첫번째로 지정해서 출력한다.