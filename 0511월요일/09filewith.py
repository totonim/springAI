# 08filewith.py
# 파일처리 2가지 접근 일반/with 
import time

path = './data/two.txt' 
with open(path ,'a', encoding='utf-8')  as file:
    file.write('spring화려한봄날\n')
    file.write('summer시원한수박\n')
    file.write('skyblue밤하늘\n')

print(path,'파일로 저장성공했습니다\n2초후에 내용 출력됩니다')
time.sleep(2)
path = './data/two.txt'
with open(path ,'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

