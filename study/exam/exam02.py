def StarCount(height):

    h=s=0

    while h<height:
        h+=1
        print('*'*h)
        s+=h

    return s

height = int(input('height : '))
print('start 개수 : %d'%StarCount(height))

def bank_account(bal):
    balance = bal
    def getBalance():
        return balance
    def deposit(money):
        nonlocal balance
        balance += money
        print('%d원 입금후 잔액은 %d원입니다'%(money,balance))

    def withdraw(money):
        nonlocal balance

        if withdraw>balance :
            print('잔액이 부족합니다')
        else:
            balance -= money
            print('%d원 출금후 잔액은 %d원 입니다'%(money,balance))
    return getBalance, deposit, withdraw

bal = int(input('최초 계좌의 잔액을 입력하세요:'))

blance,deposit,withdraw = bank_account(bal)
print("현재 계좌 잔액은 %d원 입니다"%balance())

money = int(input('입금액을 입력하세요:'))
deposit(money)
money = int(input('출금액을 입력하세요:'))
withdraw(money)






