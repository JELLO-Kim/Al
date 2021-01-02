#요일 구하기
Day = 0
montly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, input().split())
for i in range(0, x-1):
    Day += montly[i]
Day = (Day+y)%7
print(week[Day])