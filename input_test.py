#기본입출력 input() print() 
'''
name = input("이름을 입력하세요.") #키보드로부터 값을 입력 
age = input("나이는?")
print("나의 이름은 " + name + "이고, 내 나이는 " + age + "살 입니다.")
'''

#숫자 두 개를 입력 받아(변수명 a=5,b=7) 두수를 더하세요
'''a = int(input("첫번째 숫자를 입력하세요")) #5
b = int(input("두번째 숫자를 입력하세요")) #7

print(a + b) #12?
#input()함수는 모두 문자로 입력
'''

#비만도 구하기공식: 비만도 = 몸무게*(키의제곱)*10000
weight = float(input("몸무게"))
height = float(input('키'))
BMI = weight*(height**2)*10000
print (BMI)