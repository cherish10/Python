import pymysql
print(pymysql.version_info)

config ={
    'host' : '127.0.0.1',
    'user' : 'dda',
    'password' : '0258',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()

    print(tables)

    if tables:
        print('table 있음')
    else :
        print('table 없음')

except Exception as e :
    print('db error :',e)

finally:
    cursor.close()
    conn.close()

import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'dda',
    'password' : '0258',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
}
try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    code = int(input('삭제할 코드 입력: '))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if rows :
        print('레코드 삭제')
    else :
        print('해당 code 없음')

    sql = "select * from goods"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for r in rows :
        print('%d %s %d %d'%r)

    print('검색 레코드 수 :',len(rows))

    name = input('\n조회할 상품명 입력:')
    sql = f"select * from goods where name likee '%{name}'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        for r in rows:
            print(r[0],r[1],r[2],r[3])

    else :
        print('해당 상품 없음')
except Exception as e:
    print('db 연동 오류 :',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()


