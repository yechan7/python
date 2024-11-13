#예외처리
'''
str = "89점"
score = int(str)
print(score)



#=>예외처리
str = "89점"
try:
    score = int(str)
    print(score)
except:
    print("예외가 발생했습니다")
print("작업완료")


while True:
    str = input('점수를 입력하세요')
    try:
        score = int(str)
        print('입력한 점수: ',score)
    except:
        print("점수형식이 잘못되었습니다.")
        print("작업완료")
    break
'''

str = "89"
try:
    score = int(str)
    print(score)
    a = str[3]
except NameError:
    print("변수명을 확인하세요")
except IndexError:
    print("리스트변수의 첨자범위를 확인하세요")