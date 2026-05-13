class Emp:
    number = 0 #멤버변수=전역변수=속성=attribute
    name = ''  #멤버변수=전역변수=속성=attribute

    def inputMenu(self):
        #함수=메서드=method, 클래스안의 함수는 반드시 매개인자 있음
        self.number = int(input('번호입력>>>'))
        self.name = input('이름입력>>>')

    def displayMenu(self):
        print()
        print('입력받은 번호 =', self.number)
        print('입력받은 이름 =', self.name)

# 클래스안의 함수구현(첫번째인자 무조건 1개가 있어야함cls) 기술, 호출할때 cls무시 
# 클래스안의 함수호출은 반드시 클래스이름으로 객체화  변수 = 데이터 비슷
# 클래스의 객체화는 변수오브젝트객체명object = 클래스이름()  
ob = Emp()
ob.inputMenu()
ob.displayMenu()