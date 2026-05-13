# 19faker.py 

from faker  import Faker

my = Faker()
print('faker연습')
for k in range(20):
    print(my.name())

print()
data = Faker('ko_KR')
for k in range(20):
    print(data.name())

print()
for k in range(20):
    print(data.address())    