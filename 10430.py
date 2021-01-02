# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)

# print((a+b)%c)
# print((a%c)+(b%c)%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

#map 함수 사용
A,B,C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)