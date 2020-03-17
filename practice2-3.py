#실습 3
n=int(input('정수를 입력하시오 : '))
max=n

loop_count=1
while loop_count<=4:
    n=int(input('정수를 입력하시오 : '))
    if n>max:
        max=n
    loop_count+=1

print()
print('가장 큰 값 :', max)
