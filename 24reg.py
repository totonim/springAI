# 정규식 
import re

# substitution(치환)을 담당하는 가장 핵심적인 함수는 re.sub()입니다.
#첫번째  re.sub(변경전, 변경후, 대상문자열) 비슷한 문자열 replace()
#두번째  ret = re.search('검색어' 대상문자열)   ret.group()
# re.findall('[a-zA-Z0-9]+', 대상문자열)

message = 'My best 7 * color 커피 (blue) Fru_it&$ is Blue 3456 Day'
ret = re.findall('[a-zA-Z0-9]+', message)  # Fru  it
print(ret)
ret = re.findall(r'[\w]+', message)     # Fru_it 한글도 포함 r=raw
# ret = re.findall('[\\w]+', message)   # Fru_it 한글도 포함 \\ = \
# ret = re.findall('[\w]+', message)    # SyntaxWarning: invalid escape sequence '\w'
print(ret)
print()
print()

message = 'My best 7 * color (blue) Fru_it&$ is Blue 3456 Day'
ret = re.findall('[^a-zA-Z0-9]+', message) #숫자제외,대소영문제외 특수문자출력
print(ret)
ret = re.findall(r'[^\w]+', message)       #숫자제외,대소영문제외 특수문자출력
print(ret)
print()



