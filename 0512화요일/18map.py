# 18def.py 

def square(a):
    cal = a**2 
    return cal  

print('일반식', square(7))
print('람다식', (lambda x: x**2)(7))
print()

numbers = [1,2,3,4,5] #데이터값을 3번라인 square함수 매개인자에 전달
print('일반식', list(map(square, numbers)) )
print('람다식', list(map(lambda x: x**2, numbers)))

#람다식할때 사용하는 함수 filter(), map(함수,데이터), reduce()


