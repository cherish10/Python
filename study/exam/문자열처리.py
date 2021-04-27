import re
from re import findall

st1 = '1234 abc홍길동 ABC_555_6 이사도시'

print(findall('1234',st1))
print(findall('[0-9]',st1))
print(findall('[0-9]{3}',st1))
print(findall('[0-9]{3,}',st1))
print(findall('\\d{3,}',st1))

print(findall('[가-힣]{3,}',st1))
print(findall('[a-z]{3}',st1))
print(findall('[a-z][A-Z]{3}',st1))

st2 = 'test1abcABC 123mbc 45test'

print(findall('^test',st2))
print(findall('st$',st2))

print(findall('.bc',st2))

print(findall('t.',st2))

st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\\w{3,}',st3)
print(words)

print(findall('[^^*$]+',st3))

from re import match

jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}',jumin)
print(result)

if result :
    print('주민번호 일치')
else:
    print('잘못된 주민번호')

jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4][0-9]{6}',jumin)
print(result)

if result :
    print('주민번호 일치')
else:
    print('잘못된 주민번호')


from re import sub

st3 = 'test홍길동 abc 대한민국 tbc'
text3 = sub('[a-zA-Z]','',st3)

from re import split,match,compile

multi_line= """http://www.naver.com
http://www.daum.net
www.hongkildong.com"""

web_site = split("\n", multi_line)
print(web_site)

pat = compile("http://")

sel_site = [site for site in web_site if match(pat,site)]
print(sel_site)

from re import findall, sub

texts = ['우리나라 대한민국, 우리나라%$ 만세','비아그$라 500GRAM 정력최고!','나는 대한민국 사람','보험료 15000원에 평생 보장 마감 임박','나는 홍길동']

texts_re1 = [t.lower() for t in texts]
print('texts_re1 : ', texts_re1)

texts_re2 = [sub("[0-9]",'',text)for text in texts_re1]
print('texts_re2 :',texts_re2)

texts_re3 = [sub("[,.?!:;]",'',text)for text in texts_re2]
print('texts_re3 :',texts_re3)

spec_str = '[@#$%^&*()]'
texts_re4 = [sub(spec_str,'',text)for text in texts_re3]
print('texts_re4 :',texts_re4)

texts_re5 = [''.join(findall("[^a-z]",text))for text in texts_re4]
print('texts_re5 :',texts_re5)

texts_re6 = [''.join(text.split())for text in texts_re5]
print('texts_re6 :',texts_re6)

