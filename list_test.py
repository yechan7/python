#연산자  산술 대입 논리 관계
#변수 자료형(str int float)
#문자열다루기
#리스트  []
'''
singer_list = ["뉴진스", "트와이스"]
print(type(singer_list))
print(singer_list[0])
singer_list.append("아이유")
print(singer_list)
singer_list.insert(1,"르세라핌")
singer_list.insert(0,"서예찬")
singer_list.insert(2,"차은우")
print(singer_list)
print(singer_list[1:3])

sports = ["야구", "축구", "농구"]
print("농구" in sports)
print("배구" in sports)
sports.remove("축구")
print(sports)
print(len(sports))
sports[0] = "배드민턴"
print(sports)

#list변수 요소값을 제거하는 방법
#값으로 제거 remove

#번지로 제거 del pop
sports = ["야구", "축구", "농구"]
sports.remove("축구")
sports.append("족구")
print(sports)

#번지로 제거 del pop
del sports[0]
print(sports)
sports.pop()
print(sports)
sports.append("족구")
sports.append("축구")
sports.append("배구")
print(sports)
sports.pop(1)
print(sports)

sports.clear() #모든값 삭제
print(sports)
'''

fruit = ["apple", "banana", "mango"]
food = ["떡볶이", "치킨", "국밥"]

fruit.append("strawberry")
food.append("햄버거")
fruit.remove("apple")
food.remove("치킨")
fruit.insert(1,"melon")
print(fruit)
print(food)
fruit.extend(food)
print(fruit)
