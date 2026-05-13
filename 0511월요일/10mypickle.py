# 10mypickle.py
import pickle

fileName = './data/my.pckl'
print("1.write  2.read ")
num=input(">>> ")
if num=='1':
    try:
        file=open(fileName, 'wb')  
        memo=input("내용입력>>> ")
        pickle.dump(memo, file) 
        file.close()
        print("pickle 저장성공 ok") 
    except Exception as ex: 
        print("파일저장 에러이유" ,ex ) 
elif num=='2':
    try:
        file=open(fileName, 'rb')
        print('피클로 저장된 내용 출력됩니다 ')
        a=pickle.load(file)
        print(a)
        file.close()
    except:
        print("파일이없습니다")
else:
    print('작업번호를 잘못 선택하셨군요!!')

