hap, gob, mok = 0, 0, 0
num1, num2 = 0, 0

try:
    num1 = int(input('첫번째숫자 num1 >>> ')) #input()숫자입력해도 문자로인식
    num2 = int(input('두번째숫자 num2 >>> ')) #input()숫자입력해도 문자로인식
    hap = num1 + num2
    gob = num1 * num2
    mok = num1 / num2 
except Exception as ex: 
    print(ex, '에러가 발생했습니다\n메인화면으로 이동하세요\n')


print(f'{num1} + {num2} = {hap}')
print(f'{num1} * {num2} = {gob}')
print(f'{num1} / {num2} = {mok}')

# 안전장치 try~except예외
# 서버 연결 에러
# 계산연산,입력에서만 에러가 아니라 
# 파일처리에서 경로를 잘못지정, 파일명 잘못기술한다던지 