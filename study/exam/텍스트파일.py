import os
print('\n현재경로:C:\pythonProject\study ')

try :
    ftest1 = open('C:/Users/user/Documents/ftest.txt', mode='r')
    print(ftest1.read())
    ftest1.close()

    ftest2 = open('C:/Users/user/Documents/ftest.txt', mode='w')
    ftest2.write('my first text~~~')
    ftest2.close()

    ftest3 = open('C:/Users/user/Documents/ftest.txt', mode='a')
    ftest3.write('\nmy second text~~~')
    ftest3.close()

except Exception as e:
    print('Error 발생: ',e)

try :
    ftest = open('C:/Users/user/Documents/ftest.txt', mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    ftest = open('C:/Users/user/Documents/ftest.txt', mode='r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단 수: ', len(lines))

    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())

    print(docs)

    ftest = open('C:/Users/user/Documents/ftest.txt', mode='r')
    line = ftest.readline()
    print(line)
    print(type(line))

except Exception as e:
    print('Error 발생: ',e)

finally:
    ftest.close()