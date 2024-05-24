# if문 연습

'''
today = input("요일을 입력하세요")


if today == "일요일":
    print('게임 세 판합시다.')
print("공부 시작")

# 2. if~else문

if today =='일요일':
    print('게임 세판 합시다.')
    
else:
    print('게임 한판 합시다.')

# 3. if~elif~else문

if today =='일요일':
    print('게임 열판 합시다.')
elif today == '토요일':
    print('게임 세판 합시다.')
else:
    print('물 한잔 먹고 공부 시작.')
'''

total = int(input('손님은 몇명?'))

if total <= 4:
    print('추가비용없습니다.')
elif total > 4 and total <= 8:
    print(f'추가비용은 {total - 4}만원 입니다')
else:
    print('최대 입장인원은 8명입니다.')
