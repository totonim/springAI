# 15return.py
# 함수리턴값 
# 구현처리후 결과값을 돌려줄때 마지막기술 권장

def mydata():
    name = 'kim'
    kor,eng,total,avg = 90,85,0,0
    total = kor+eng
    avg = total//2
    return name,total,avg

a,b,c = mydata()
print(f"이름={a} 총점={b} 평균={c}")
print()

def myscore(kor, eng):
    total,avg, result = 0,0,''
    total = kor+eng
    avg = total//2
    if avg >= 70 :
        result = 'OK pass 합격'
    else:
        result = '재시험 불합격'

    return result

score = myscore(90,85)
print(f"당신의 시험결과는 {score} 입니다")

