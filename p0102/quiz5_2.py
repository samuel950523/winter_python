
# 퀴즈 1
# 'data/coding.txt' 문서를 읽고 코딩이라는 단어가 들어간 어구를 리스트화 한 후
# 총 갯수를 출력하는 함수를 코딩하여라.
#

'''
파일명 :  data/coding.txt
코딩이라는 글자가 들어간 어구 출력 : ['코딩을', '코딩을', '코딩에', '코딩을', '코딩을', '코딩을', '코딩도', '코딩에', '코딩은', '코딩을', '코딩도', '코딩', '코딩도', '코딩을', '코딩을']
총 갯수는? 15
'''





# 퀴즈 2
# 퀴즈1에서 작성한 코딩소스를 이용하여 문서경로, 단어, 인코딩 값을 함수로 전달한 후
# 다음과 같은 결과가 출력되도록  함수를 변경하여라

# # 함수 호출
# fileread2('data/coding.txt', '습관', 'utf-8')
# fileread2('data/color.txt', '주황', 'utf-8')

'''
퀴즈2  
******************************
파일명 :  data/coding.txt
습관 글자가 들어간 어구 출력 : ['습관', '습관을', '습관을', '습관이', '습관을']
총 갯수는? 5


******************************
파일명 :  data/color.txt
주황 글자가 들어간 어구 출력 : ['주황을', '주황을', '주황은', '주황을']
총 갯수는? 4
'''





# 퀴즈 3
# readlines()를 이용하여 문서에서 첫줄만 출력하고 아래와 같이
# 첫줄의 공백과 공백 사이, 앞과 뒤에 특정 문자열을 삽입하여라
'''
퀴즈3 >> 
******************************
파일명 :  data/coding.txt

 첫줄만 출력 : 
 코딩을 잘하는 사람의 특징


 첫줄을 변경하여 출력 : 
 **코딩을 / 잘하는 / 사람의 / 특징**
'''






# 퀴즈 4
# readlines()를 이용하여 문서에서 특정 행부터 행까지를 출력하도록
# 함수를 코딩하여라

'''
# readFirstLines('data/color.txt', 'utf-8', 12, 15) 함수 호출시 

파일명 :  data/color.txt
총 행 수 :  61

 13행부터 15행 까지 출력
******************************
13 행 : ORANGE를 좋아하는 사람

14 행 : * 심성이 착하고, 다른 사람들과 함께 있기를 좋아하고, 귀가 엷고 충성심이 강하며 솔선 수범형.

15 행 : * 인정이 많다. 유쾌한 성격.

'''

'''
# readFirstLines('data/Yesterday.txt', 'cp949', 7, 12) 함수 호출시

파일명 :  data/Yesterday.txt
총 행 수 :  30

 8행부터 12행 까지 출력
******************************
8 행 : There's a shadow hanging over me

9 행 : Oh, yesterday came suddenly

10 행 : 

11 행 : Why she had to go,

12 행 : I don't know She wouldn't say

'''







# 퀴즈 5
# n개의 단어를 입력받은 후 output.txt 파일로 저장하여라
'''
# inputWriteFile(5, 'data/output.txt', 'utf-8') 함수 호출시 결과

단어를 입력하세요 ... 장발장
단어를 입력하세요 ... 신데렐라
단어를 입력하세요 ... 콩쥐팥쥐
단어를 입력하세요 ... 라푼젤
단어를 입력하세요 ... 선녀와 나뭇꾼
입력된 단어 리스트는 ['장발장', '신데렐라', '콩쥐팥쥐', '라푼젤', '선녀와 나뭇꾼'] 입니다.
5 개의 단어가 모두 저장되었습니다.
'''
'''
# inputWriteFile(2, 'data/output.txt', 'utf-8') 함수 호출시 결과물 
단어를 입력하세요 ... 오늘도 좋은 하루 
단어를 입력하세요 ... 꽃길만 걷자
입력된 단어 리스트는 ['오늘도 좋은 하루 ', '꽃길만 걷자'] 입니다.
2 개의 단어가 모두 저장되었습니다
'''



# 퀴즈 6
# black.txt 파일에 white.txt 파일의 내용을 추가하여라




# 퀴즈7 파일읽기, 쓰기, 추가 기능을 이용하여 다음과 같은 프로그램을 작성하여라.
# 파일에 추가되는 단어의 글자수는 2글자로 제한한다.

'''
** 퀴즈7 **

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   1

[단어 추가]
두 글자로 구성된 단어를 입력하세요송아지
두글자가 아닙니다.
두 글자로 구성된 단어를 입력하세요사과
단어가 입력되었습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   1

[단어 추가]
두 글자로 구성된 단어를 입력하세요자두
단어가 입력되었습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   2

[단어 모두 출력]


추가된 단어는 총 2 입니다.
사과

자두



메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   3

[파일 내용 모두 삭제]
단어 목록을 모두 삭제하였습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   2

[단어 모두 출력]


추가된 단어는 총 0 입니다.


메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   4


프로그램을 종료합니다.
'''









# 퀴즈8
# 위의 퀴즈7에서 단어를 추가할때 입력에 따라 여러개 단어를 추가할 수 있도록 프로그램을 수정하여라.
'''
** 퀴즈8 **

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...  1

[단어 추가]
두 글자로 구성된 단어를 입력하세요... 호랑이
두글자가 아닙니다.
두 글자로 구성된 단어를 입력하세요... 호박
단어가 입력되었습니다.

단어를 계속 추가하시겠습니까? (y/n)... y
두 글자로 구성된 단어를 입력하세요... 사탕
단어가 입력되었습니다.

단어를 계속 추가하시겠습니까? (y/n)... 네
잘못된 입력입니다.
단어를 계속 추가하시겠습니까? (y/n)... n
단어 추가를 종료를 합니다. 


메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ... 4


프로그램을 종료합니다.

'''
