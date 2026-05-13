# 05dict.py
mysite = { } 
# 딕트이름['key'] = value값
mysite['naver'] = 'http://www.naver.com'
mysite['kakao'] = 'http://www.kakao.net'
mysite['googe'] = 'http://www.googl.org'
# print(mysite)

print('for k,v in mysite.items()')
for k,v in mysite.items():
    print(k, ':', v)

print('\nfor k in mysite')
for k in mysite:
    print(k, ':', mysite[k])

print('\nfor n, key in enumerate(mysite)')
for n, key in enumerate(mysite):
    print(n, '', mysite[key])

print()

print()
print(mysite.keys())
print()
print(mysite.values())
print()

# dict딕트 키:value 쌍으로 구성 
# dict는 LLM/랭체인/랭에이전트 이해하는데 필수 
# kor, eng = 90, 85
# student = { } 
# student['kor'] = 90  
# student['eng'] = 85  

# 프로젝트, 고급내용은 list & dict 혼합구조 