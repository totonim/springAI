# 08file.py

# 파일처리 2가지 접근 일반/with 
# 파일처리 함수는 읽기/쓰기 제어할때 open()
# 파이썬의 일반 파일처리는 import문장 기술안해도 됩니다
#   ㄴopen(파일경로및파일명, 모드w/a/r, 인코딩)
    #   w=기록저장 단점은 라인개행이 안됩니다
# 피클은 import pickle, json도 마찬가지로 import json

import time

path = './data/hello.txt' 
# file = open(path ,'w', encoding='utf-8') #내용 덮어씌우기
file = open(path ,'a', encoding='utf-8') #내용 추가
file.write('blue\n')
file.write('sky\n')
file.close()


print(path,'파일로 저장성공했습니다\n2초후에 내용 출력됩니다')
print('- ' * 50)
time.sleep(2)
path = './data/hello.txt'
file = open(path ,'r', encoding='utf-8')
content = file.read()
print(content)
file.close()
