a=10
b=20
a>5 and b>10 #True
a>5 and b<5 #False
a<5 and b>10 #False
a<5 and b<5 #False
0<a<b #True
a>5 or b>10 #True
a>5 or b<5 #True
a<5 or b>10 #True
a<5 or b<5 #False
not a<5 #True
not b>10 #False

#조건 논리 유형1 예제
score=int(input('성적을 입력하시오:'))

if score >= 70 :
    print('축하합니다')
print('수고하셨습니다')

#조건 논리 유형2 예제
number=int(input('정수를 입력하시오:'))

if number%2 == 0:
    print(number,'는 짝수입니다.')
else:
    print(number,'는 홀수입니다.')

print('프로그램 종료')

#조건 논리 유형2 예제2
a=int(input('Enter a:'))
b=int(input('Enter b:'))

if a>b:
    max=a
else:
    max=b

print(max)

#조건 논리 유형3 예제
score=int(input('성적을 입력하시오:'))

if score>=90:
    grade='A'
elif 80<=score<90:
    grade='B'
elif 70<=score<80:
    grade='C'
else:
    grade='D'

print('당신의 학점은',grade,'입니다.')

#중첩된 if 조건문
score=int(input('성적을 입력하시오:'))

if score>=70:
    print('통과하셨습니다.')
    if score>=90:
        print('A장학금 지급 대상자입니다.')
    elif score>=80:
        print('B장학금 지급 대상자입니다.')
elif score>=60:
    print('조건부 통과자입니다.')
else:
    print('재수강 대상자입니다.')

print('수고하셨습니다.')    
