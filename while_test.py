#while 반복문
#100까지 출력
'''
i = 1
while i <= 100:
    print(i)
    i += 1

j = 3
while j <= 5:
    print(j)
    j += 1

a = 1
while a <= 13:
    print(f'{a}번째 파이썬 최고!!')
    a += 1

i = 1
while i <= 100:
    if i %10 == 0:
        print(i)
    else:
        print(i, end= ' ')
    i += 1


# 두개의 정수를 입력을 받아 더하여 출력하는 프로그램

while True:
    num1 = int(input('첫번째 정수 값: '))
    num2 = int(input('두번째 정수 값: '))
    print(f'두수의 합은 {num1+num2} 입니다.')
    if num1 + num2 == 0: #무한 반복문 탈출 조건
        break
'''
x = 3
while x < 6:
    print(x)
    x += 1

echo = input('입력')

while echo != "exit":
    print(echo)
    echo = input('입력')

echo = input('입력')
while True:
    if echo == "exit":
        break
    print(echo)
    echo = input('입력')