jumin = "971204-2614816"
# 문제해결1] 주번 쪼개서 자릿수체크  len() 앞자릿수6  뒷자리수7
# 문제해결2] 12월 04일 생일입니다 
# 문제해결3] 성별구별  코드 구현 

gender = jumin[7]
print('gender =',gender)
if gender == '1' or gender == '3' :
    print('당신의 성별은 남자입니다')
elif gender == '2' or gender == '4' :
    print('당신의 성별은 여자입니다')
else:
    print('당신의 성별은 잘못 표기 되었습니다')


