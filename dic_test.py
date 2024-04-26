#컨테이너 변수 - 리스트[] 튜플() 딕셔너리{} 셋{}
#딕셔너리{} 키:값
person = {
    '이름':'서예찬',
    '나이':17 ,
    '키':170,
    '집주소':'북한'}
print(person)
person["몸무게"] = 60
print(person)
person['키'] = 180
print(person)
del person['나이']
print(person)

print(person.get('집주소'))

print("이름" in person)
print("서예찬" in person.values())

