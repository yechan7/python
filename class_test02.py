#예외처리
#클래스
#파일처리
'''
balance = 8000 #통장잔고

def deposit(money): #예금
    global balance
    balance += money

def inquire():
    print("잔액은 %d원 입니다." %balance)

deposit(2000)
inquire()

#클래스로 변환
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, money):
        self.balance += money
        print(money,"%d원 입금 완료되었습니다.")
    def inquire(self,): #잔액조회
        print("잔액은 %d원 입니다." %self.balance)

kakao = Account(8000) #객체생성
kakao.deposit(3000) #입금 3000원
kakao.inquire()

toss = Account(100000) #계좌개설 잔액 10만원
toss.deposit(50000)#5만원입금
toss.inquire()
'''
#예외처리
arr = [1,2,3]
try:
    print(arr[2]/0)
    print(arr[3])
except ZeroDivisionError:
    print("숫자를 0으로 나눌 수 없습니다.")
except IndexError:
    print("리스트의 요소에 접근하지 못했습니다.")

'''
i = 9
try:
    div = i/0
    print(div) #ZeroDivisionError발생 예외처리하시오
except:
    print("숫자를 0으로 나눌 수 없습니다.")
'''