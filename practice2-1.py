#실습 1
working_hour=int(input('근무시간을 입력하시오 : '))
pay_per_hour=int(input('시간당 수당을 입력하시오 : '))

total_pay=working_hour*pay_per_hour
if working_hour>12:
    additional_pay=(working_hour-12)*pay_per_hour*0.3
    total_pay+=additional_pay
print()
print('총 급여는', total_pay, '원입니다.')
