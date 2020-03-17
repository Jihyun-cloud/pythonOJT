#실습 2
n=int(input('정수를 입력하시오 : '))
a=1
count=0
while a<=n:
    if n%a == 0:
        print(a)
        count+=1
    a+=1
print()
print(n,'의 약수의 개수 :', count)
