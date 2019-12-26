# 캐스팅
# 문자열 -> 리스트
# 문자열변수.split() : 공백을 기준으로 해서 리스트화
# 문자열변수.split(구분문자) : 구분문자을 기준으로 해서 리스트화
# list(문자열변수)
# : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경
sampleTxt1 = '사과 포도 수박 딸기'
sampleTxt2 = '사과,포도,수박,딸기'
print(f'before split sampleTxt1 = {sampleTxt1}')
print(f'sampleTxt1의 데이터형은? = {type(sampleTxt1)}')

sampleTxt1 = sampleTxt1.split()
print(f'after split sampleTxt1 = {sampleTxt1}')
print(f'sampleTxt1의 데이터형은? = {type(sampleTxt1)}')

print(f'before split sampleTxt2 = {sampleTxt1}')
print(f'sampleTxt2의 데이터형은? = {type(sampleTxt2)}')

sampleTxt2 = sampleTxt2.split(',')
print(f'after split sampleTxt2 = {sampleTxt2}')
print(f'sampleTxt2의 데이터형은? = {type(sampleTxt2)}')

# 리스트 -> 문자열
# str(리스트이름)
# : [ ], 쉼표(,) 도 포함해서 모두 문자열화
# '구분자'.join(리스트이름)
# : 구분자가 아이템요소 사이에 모두 추가된 후 문자열화
jobList = ['Python', 'DB', 'Flask']
print(f'jobList = {jobList}')
result1 = str(jobList)
result2 = '/'.join(jobList)
print(result1)
print(result2)

# 중첩 리스트 구조
# 리스트 안에 리스트가 있다
# 중첩 리스트의 인덱싱은?
# 리스트이름[index1][index2]
# 초기값으로 중첩 리스트 생성
# 리스트 변수 = [ [값1, 값2...], [값1, 값2...]]
listMulti1 = [1, 2, ['a', 'b', 'c'], ['포도', '수박']]
print(f'listMulti1 = {listMulti1}')
print(f'listMulti1[0] = {listMulti1[0]}')
print(f'listMulti1[2] = {listMulti1[2]}')
print(f'listMulti1[2][0] = {listMulti1[2][0]}')
print(f'listMulti1[3][-1]= {listMulti1[3][-1]}')

# 중첩 리스트 생성 2
# 1차원 리스트 정의 후 1차워 리스트르르 다시 리스트로 구성
userName = ['홍길동', '박지민', '이미연']
userAge = [20, 25, 34]
userGender = ['남', '남', '여']
userAdder = [userName, userAge, userGender]
print(f'userAdder = {userAdder}')
print(f'userAdder[0] = {userAdder[0]}')
print(f'userAdder[2] = {userAdder[2]}')
print(f'userAdder[2][0] = {userAdder[2][0]}')
