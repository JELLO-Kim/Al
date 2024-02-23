import sys
sys.stdin = open("input.txt")

m, n = map(int, input().split())
# m = 36
# n = 108
# 최대공약수 : m
# 최소공배수 : n
# e = 최소공배수를 최대공약수로 나눈 몫
e = n // m

# e의 조합 구하기
aa = e//2
min_sum = []
for i in range(aa, 0, -1):
    if e%i == 0:
        x = i
        y = e//i
        # 두개의 최대공약수가 1인지 확인
        for j in range(2, min(x, y)+1):
            if x%j == 0 and y%j == 0:
                break
        else:
            a = m * x
            b = m * y
            if not min_sum:
                min_sum = [a, b]
            else:
                if sum(min_sum) > a+b:
                    min_sum = [a, b]
if not min_sum:
    print(m, m*e)
else:
    print(min(min_sum), max(min_sum))
# a = 13200
# b = 13104
#
# # a = 14850
# # b = 11648
# #
# while True:
#     tmp = a%b
#     if tmp != 0:
#         a = b
#         b = tmp
#     else:
#         print(b)
#         break


# for i in range(1, e//2 +1):
#     if i == 11648:
#         print(e%i)
#     if e%i == 0:
#         a = m * i
#         b = m * (e//i)
#         if not min_sum:
#             min_sum = [a, b]
#         else:
#             if sum(min_sum) > a + b:
#                 min_sum = [a, b]
# print(min_sum)

