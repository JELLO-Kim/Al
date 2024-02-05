A = input() #472
B = input() #385

A = int(A) #출력에 앞서 A를 int로 다시 인식시켜주지 않으면 '문자열'로 인식하여 3번 결과 값으로 472가 5번 반복출력된다..

print(A*int(B[2])) #3번 출력
print(A*int(B[1])) #4번 출력
print(A*int(B[0])) #5번 출력
print(A*int(B)) #6번 출력