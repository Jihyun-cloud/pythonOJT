#예제1
a=1
while a<=5:
    print(a)
    a+=1

#예제2
a=1
sum=0
while a<=10:
    sum+=a
    a+=1
print('sum:',sum)
sum(range(11))

#예제3 방법1
a=2
sum=0
while a<=10:
    sum+=a
    a+=2
print('sum:',sum)
#예제3 방법2
a=1
sum=0
while a<=10:
    if a%2==0:
        sum+=a
    a+=1
print('sum:',sum)

#break 사용하기
a=1
while a<=10:
    print('a=',a)
    if a>=5:
        break
    a+=1
print('after while')

#무한루프와 break
a=1
while True:
    print(a)
    if a==5:break
    a+=1

#continue 사용하기
a=0

while a<=10:
    a+=1
    if a%3==0:
        continue
    print('a=',a)
print('after while')

#중첩된 while 반복문-구구단 출력 2-9단
dan=2
while dan<=9:
    n=1
    while n<=10:
        value=dan*n
        print('%3d'%(value), end='')
        n+=1
    print()
    dan+=1
