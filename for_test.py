# 반복문 for~in

# 1. 문자열 이용 반복
'''
count = 0
for ch in "서예찬":
    print(ch, end='')
    count =count + 1

print(f"이 for문은 {count}번 실행되었습니다")
'''

# 2. 리스트변수를 이용한 반복

food_list = ['치킨', '피자', '햄버거', '찐계란', '떡볶이', '자장면']
'''
print(food_list[0])
print(food_list[1])
print(food_list[2])
print(food_list[3])
print(food_list[4])
print(food_list[5])

for food in food_list: #6번 실행
    print(food)


i = [1,2,3,4,5]

for n in i:
    print(n, end='   ')

for n in [1,2,3,4,5]:
    print('AI 화이팅')

for item in ['힙합', '발라드']:
    print(item + ' 즐겨 듣는다')

# 3. range()함수를 이용한 반복

count = 0
for n in range(100):
    count = count + 1
    print(f"{count}번 사랑합니다")
    print('미워도 다시한번')

for n in range(1,10,2):
    print(n)

for n in range(3,31,3):
    print(n)

for n in range(21):
    print(n)
'''
for n in range(97,76,-1):
    print(n)