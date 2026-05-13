def mysu(x):
    cal = 3*x+2
    return cal


print('일반식', mysu(8))
mylam = lambda x: 3*x+2
print('람다식', mylam(8))
print('람다식', (lambda x: 3*x+2)(8))
print()

print('람다식 if~else조건식')
def myExpress(x):
    if x%2==0:
        return "짝수"
    else:
        return "홀수"
    
print('일반식', myExpress(7))
mylam = lambda x: "짝수" if x%2==0 else "홀수"
print('람다식', mylam(7))
print('람다식', (lambda x: "짝수" if x%2==0 else "홀수")(7))
