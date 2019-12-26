# 리스트[] 튜플() 딕셔너리{} 집합{}

# 리스트[]
fruits = ['사과', '바나나', '포도']
print(fruits)

# 빈 리스트
movieList = []
print(movieList)

# 서로 다른 데이터형으로 리스트 정의
myList = [True, 100, '홍길동']
print(f'myList = {myList}')

# 리스트 인덱싱 / 슬라이싱
print(fruits[0], fruits[-1])
# 리스트이름[start:end:step])
numList = [0, 1, 2, 3, 4, 5, 6, 7]
print(f'numList = {numList}')
print(f'numList[0:3] = {numList[0:3]}')
print(f'numList[3:] = {numList[3:]}')
print(f'numList[::2] = {numList[::2]}')
print(f'numList[:4] = {numList[:4]}')
print(f'numList[::] = {numList[::]}')
print(f'짝수번째만 출력하기 = {numList[1::2]}')

'''
numList = [0, 1, 2, 3, 4, 5, 6, 7]
numList[0:3] = [0, 1, 2]
numList[3:] = [3, 4, 5, 6, 7]
numList[::2] = [0, 2, 4, 6]
numList[:4] = [0, 1, 2, 3]
numList[::] = [0, 1, 2, 3, 4, 5, 6, 7]
'''

# CRUD : Create Read Update Delete
# 리스트 값 변경하기
print(f'numList = {numList}')
numList[0] = 100
print(f'numList = {numList}')

# 리스트 연산
movie = ['알라딘', '엔드게임', '토이스토리']
drama = ['남자친구', '으라차차 와이키키2']
print(movie)
print(drama)
print(movie + drama)
print(drama + movie)
print(drama * 3)

print('movie = %s' % movie)
print('drama = %s' % drama)
print('drama + movie = %s' % (drama + movie))
print('drama*3 = %s' % (drama * 3))

# 리스트 함수
# 리스트변수.함수명(옵션)
# append insert remove pop clear
foods = ['라면']
print(f'foods = {foods}')
foods.append('김밥')
print(f'foods = {foods}')
foods.append('짬뽕')
print(f'foods = {foods}')
foods.insert(0, '냉면')
print(f'foods = {foods}')

# 리스트 삭제
# remove(값) : 값으로 삭제하기
# pop() : 마지막 요소가 삭제되면서 값이 반환
# pop(위치값) : 위치에 해당하는 요소가 삭제되면서 값이 반환
# clear() : 빈 리스트로
# del 리스트변수 : 리스트 자체가 삭제

numList2 = [1, 2, 3, 4, 5, 6, 7]
print(f'numList2 = {numList2}')
numList2.remove(3)
print(f'numList2 = {numList2}')
numList2.pop()
print(f'numList2 = {numList2}')
print(f'pop value = {numList2.pop(3)}')
print(f'numList2 = {numList2}')
numList2.clear()
print(f'numList2 = {numList2}')
# del numList2
# print(f'numList2 = {numList2}')
