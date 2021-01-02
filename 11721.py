#내가 제출한 방법
t=input()
for i in range(0,(len(t)//10)+1):
    print(t[i*10:(i+1)*10])

#리펙토링1
t=input()
for i in range(0,(len(t)//10)+1):
    print(t[i*10:(i+1)*10])

#리펙토링2
t=input()
for i in range(0,len(t), 10):
    print(t[i:i+10])