# 퀴즈1 - 입력받은 값에 따라 양수와 음수를 출력하세요
print('---quiz1---')
a= int(input())
if a>0:
    print('양수입니다!')
elif a<0:
    print('음수입니다!')
else:
    print('0입니다!')

# 퀴즈2
# 입력받은 숫자 값이 짝수이면  '숫자 : 짝수'
# 홀수이면 '숫자 : 홀수' 를 출력하세요
# 숫자%2 == 0 짝수
# 숫자%2 != 0 홀수

print('---quiz2---')
a = int(input())
if a % 2 == 0:
    print("숫자 : 짝수")
if a % 2 != 0:
    print("숫자 : 홀수")

# 퀴즈 3 bmi 값에 따라 다음과 같은 메세지를 출력하세요
'''
bmi 값에 따라 출력한다.

k = 키(입력값) 단위 cm
w = 체중(입력값)

bmi = 체중(kg)/키(m)의제곱, 키의 단위는 미터(m)

bmi 값에 따라 다음과 출력한다.

고도 비만 : 35 보다 클 경우
중등도 비만  : 30 - 35 미만
경도 비만 : 25 - 30 미만
과체중 : 23 - 25 미만
정상 : 18.5 - 23 미만
저체중 : 18.5 미만
'''

'''
키를 입력해주세요... 단위 cm...180
체중을 입력해주세요... 단위 kg...95

bmi = 29.32
경도 비만
'''

print('---quiz3---')
h = int(input('키를 입력해주세요... 단위 cm...'))
w = int(input('체중울 입력해주세요... 단위 kg...'))
bmi = (w / (h / 100)*(h/100))
print(bmi)
if bmi >= 35:
    print('고도비만')
elif bmi >= 30 & bmi < 35:
    print('중등도 비만')
elif bmi >= 25 & bmi < 30:
    print('경도 비만')
elif bmi >= 23 & bmi < 25:
    print('과체중')
elif bmi >= 18.5 & bmi < 23:
    print('정상')
else:
    print('저체중')

# 퀴즈 4. 띠알아 맞추기
# 태어난 년도를 입력받아서 띠를 출력하세요
#
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
#
# 띠 = 태어난년도%12

'''
태어난 년도를 입력하세요? ....   
당신이 태어난 년도는 (  ) 이고 (  )띠 입니다. 
'''

print('---quiz4---')
ddi = ['원숭이', '닭', '개', '돼지', '쥐', '소', '범', '토끼', '용', '뱀', '말', '양']
y = int(input('태어난 년도를 입력하세요...'))
print(ddi[y%12]+'띠')

# 퀴즈 5
# 입력받은 나이에 따라 메세지를 출력하세요
#  age > 19 : 성인
#  17 <= age <= 19 : 고등학생
#  14 <= age < 17 : 중학생
#  8 <= age < 14 : 초등학생
#  age < 8  : 유치원생 또는 영유아

'''
당신의 나이를 입력해주세요 ... 12

당신은 초등학생 입니다.
'''
print('---quiz5---')
age = int(input('당신의 나이를 입력해주세요 ... '))
if age > 19:
    print('당신은 성인입니다.')
elif age >= 17:
    print('당신은 고등학생입니다.')
elif age >= 14:
    print('당신은 중학생입니다.')
elif age >= 8:
    print('당신은 초등학생입니다.')
else:
    print('당신은 유치원생 또는 영유아입니다.')

# 퀴즈 6
# 학점을 입력받아서 다음과 같은 메세지를 출력하세요
# score = float(input("학점 입력> "))
# if ~ elif ~ else 문 이용하여 메세지 출력
#
# 4.2 <= score <= 4.5 : 교수님의 사랑
# 3.5 <= score < 4.2 : 현 체제의 수호자
#  2.8 <= score < 3.5 : 일반인
# 2.3 <= score < 2.8  : 일탈을 꿈꾸는 소시민
# 2.3 미만 : 시대를 앞서가는 혁명의 씨앗

'''
학점 입력> 4.5

score = 4.5   : 교수님의 사랑 

'''
print('---quiz6---')
score = float(input("학점 입력> "))
if score >= 4.2 & score <= 4.5:
    print('교수님의 사랑')
elif score >= 3.5 & score < 4.2:
    print('현 체제의 수호자')
elif score >= 2.8 & score < 3.5:
    print('일반인')
elif score >= 2.3 & score < 3.8:
    print('일탈을 꿈꾸는 소시민')
elif score < 2.3:
    print('시대를 앞서가는 혁명의 씨앗')

# 퀴즈 7 영어, 숫자 중 한 글자만 입력받은 후
# 입력값에 따라 다음과 같은 메세지를 출력하세요
#  조건문과 in 연산자 이용
# 숫자, 알파벳 리스트 만들기

'''
영어, 숫자 중 한 글자만 입력하세요 ....A
입력한 데이타는 알파벳 입니다. 

영어, 숫자 중 한 글자만 입력하세요 ....1
입력한 데이타는 숫자 입니다. 

영어, 숫자 중 한 글자만 입력하세요 ....가 
입력한 데이타는 올바르지 않습니다. 영어, 숫자 중 한 글자만 입력하세요 
'''

print('---quiz7---')
from string import ascii_lowercase
from string import ascii_uppercase

numList = list(range(0, 10))
lowercaseList = list(ascii_lowercase)
uppercaseList = list(ascii_uppercase)

word = input('영어, 숫자 중 한 글자만 입력하세요... ')
if word in lowercaseList:
    print('입력한 데이타는 알파벳입니다.')
elif word in uppercaseList:
    print('입력한 데이타는 알파벳입니다.')
elif int(word) in numList:
    print('입력한 데이타는 숫자입니다.')
else:
    print('입력한 데이타는 옳바르지 않습니다. 영어, 숫자 중 한 글자만 입력하세요.')