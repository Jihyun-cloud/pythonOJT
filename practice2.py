#실습2
radius=input('반지름을 입력하시오 : ')
radius=int(radius)

print('반지름 : ', radius)
area=3.141592*radius*radius #area=3.141592*pow(radius,2)
perimeter=2*3.141592*radius

print('원의 넓이 : %7.3f'%area)
print('원의 둘레 : %.3f'%perimeter)
