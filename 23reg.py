# 정규식 
import re

# substitution(치환)을 담당하는 가장 핵심적인 함수는 re.sub()입니다.
#첫번째  re.sub(변경전, 변경후, 대상문자열) 비슷한 문자열 replace()
#두번째  ret = re.search('검색어' 대상문자열)   ret.group()
message = 'color Best blue 프로그래밍 bluemoon'
print(message)
msg = re.sub('blue', 'YELLO', message)
print(msg)
print()

message = 'color Best blue 초코파이 프로그래밍 bluemoon'
ret = re.search('초코파이', message)
# print(ret) 비권장 <re.Match object; span=(18, 20), match='초코파이'>
if ret :
    print(ret.group(), '데이터가 있습니다')
else:
    print('초코파이 문자열이 없습니다')
print()



