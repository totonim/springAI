# 16def.py 
# 매개인자의 갯수를 다를때 사용하면 편해요 def 함수명(*)

def first(*data):
    hap = 0 
    print(data, end = ' ')
    for num in data:
        hap = hap +num
    return hap 

value =first(1,2,3,4,5,6,7)
print('최종 합계 =', value)

def two(x,y,z):
    print(x,y,z)

def three(su1,su2, su3, su4, su5, su6, su7):
    print(su1, su2, su3, su4, su5, su6, su7)
    
def last(*value):
    pass