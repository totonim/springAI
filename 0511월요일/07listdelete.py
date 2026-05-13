data = [5, 4, 7, 1, 9, 2]
print(data)
data.clear() #전체삭제 
print(data)
print()

# 5교시 다시 설명하겠습니다. 점심시간입니다
# 부분삭제 [시작:끝-1] = []  [2:5]
data = [5, 4, 7, 1, 9, 2]
print(data)
data[2:5] = [] #17라인 같은처리
print(data)
print()

data = [5, 4, 7, 1, 9, 2]
print(data)
del data[2:5]  #11라인 같은처리 
print(data)
print()

data = [5, 4, 7, 1, 9, 2]
data.pop(3)
print(data)  #[5, 4, 7, 9, 2]
print()

#문제해결  맨끝에  6숫자추가 
data = [5, 4, 7, 1, 9, 2]
print(data)  #[5, 4, 7, 1, 9, 2]
data.append(6)
print(data)  #[5, 4, 7, 1, 9, 2, 6]
print()