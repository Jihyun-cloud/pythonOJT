# 실습 1
kor=int(input('국어 성적을 입력하시오 : '))
math=int(input('수학 성적을 입력하시오 : '))
eng=int(input('영어 성적을 입력하시오 : '))
print()
print('입력받은 성적')
print('----------') # print('-' * 15)
print('국어 성적 : ', kor)
print('수학 성적 : ', math)
print('영어 성적 : ', eng)
print()

total=kor+eng+math
average=total/3
print('총점 : ', total)
print('평균 : %.2f' %(average))
