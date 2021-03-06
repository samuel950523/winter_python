# 1. a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과 마지막 번째 튜플값을 출력하세요.

print('---quiz1---')
tuple1 = ('a', 'b', 'c', 'd', 'e')
print(tuple1[0], tuple1[-1])

# 2. 다음 코드를 작성해서 실행해보고 에러가 나는 이유를 설명하세요.
# tupledata = ('dave', 'fun-coding', 'endless')
# tupledata[0] = 'david'

print('---quiz2---')
# tupledata = ('dave', 'fun-coding', 'endless')
# tupledata[0] = 'david'
print('튜플은 값을 수정(update) 할 수 없다.')

# 3. 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding4' 데이터를 마지막에 추가하고,
#    다시 튜플 데이터로 변환하세요.
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')

print('---quiz3---')
tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
tuple2list = list(tupledata)
tuple2list.append('fun-coding4')
tupledata = tuple(tuple2list)
print(f'tupledata = {tupledata}')

# 4. 비어 있는 튜플, 리스트, 딕셔너리 변수를 하나씩 각각 만드세요.
print('---quiz4---')
emptyTuple = ()
emptyList = []
emptyDict = {}
print(
    f'emptyTuple = {emptyTuple}\nemptyList = {emptyList}\nemptyDict = {emptyDict}')

# 5. 다음 actor_info 딕셔너리 변수를 만들고, 홈페이지, 배우 이름, 최근 출연 영화 갯수를 다음과 같이 출력하세요

actor_info = {'actor_details': {'생년월일': '1971-03-01',
                                '성별': '남',
                                '직업': '배우',
                                '홈페이지': 'https://www.instagram.com/madongseok'},
              'actor_name': '마동석',
              'actor_rate': 59361,
              'date': '2017-10',
              'movie_list': ['범죄도시', '부라더', '부산행']}

# 배우 이름: 마동석
# 홈페이지: https://www.instagram.com/madongseok
# 출연 영화 갯수: 3

print('---quiz5---')
actor_info = {'actor_details': {'생년월일': '1971-03-01',
                                '성별': '남',
                                '직업': '배우',
                                '홈페이지': 'https://www.instagram.com/madongseok'},
              'actor_name': '마동석',
              'actor_rate': 59361,
              'date': '2017-10',
              'movie_list': ['범죄도시', '부라더', '부산행']}
print(f'배우 이름 : {actor_info["actor_name"]}')
print(f'홈페이지 : {actor_info["actor_details"]["홈페이지"]}')
print(f'출연 영화 갯수 : {len(actor_info["movie_list"])}')

# 6. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
print('---quiz6---')
fruit = ["Banana", "Apple", "Orange"]
fruit.remove("Apple")
print(f'after remove Apple : {fruit}')

# 7. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
print('---quiz7---')
myTuple = (1, 2, 3, 4)
myList = list(myTuple)
print(myList)

# 8. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
print('---quiz8---')
myDict = {'성인': '100000', '청소년': '70000', '아동': '30000'}
print(myDict)

# 9. 8번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
print('---quiz9---')
myDict['소아'] = '0'
print(myDict)

# 10. 8번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print('---quiz10---')
print(myDict.keys())

# 11. 8번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print('---quiz11---')
print(myDict.values())
