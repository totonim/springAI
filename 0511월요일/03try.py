# 03try.py  try, except Exception~,  else  finally 

num = 0 #변수초기화 권장
try:
    num = int(input('숫자를 기술>>> '))
except Exception as ex:
    print('에러', ex)
else:
    print('결재금액 =', num*5 ,'원' )
finally:
    print()
    print('주차요금 정산 ~~~')
    print('신호대기 엄수 ~~~')