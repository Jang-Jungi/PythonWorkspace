''' 연산자 '''
# num=1
# print(num) #1
# num+=2
# print(num) #3
# num*=2
# print(num) #6
# num/=3
# print(num) #2
# num-=-2
# print(num) #4
# num%=3
# print(num) #1

# ## 숫자처리함수 ##
# print(abs(-5))  # 절대값 5
# print(pow(4,2)) # 4^2 = 16
# print(max(5,1,2)) # 최대값 5
# print(min(5,1,2)) # 최소값 1
# print(round(3.14)) # 반올림 3

# from math import *
# print(floor(4.99)) # 내림 4
# print(ceil(3.14))  # 올림 4
# print(sqrt(16))    # 제곱근 4

# ##랜덤 함수 ##
# from random import *

# print(random())         # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*3)       # 0.0 ~ 3.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성

# # 랜덤 번호 추출 예시 1
# print(int(random()*45)+1) #1~45 이하의 임의의 값 생성
# # 랜덤 번호 추출 예시 2
# print(randrange(1,46))    # 1~46 미만의 임의의 값 생성
# # 랜덤 번호 추출 예시 3
# print(randint(1,45))      # 1~ 45 이하의 임의의 값 생성

''' Quiz 2 '''
# from random import *
# x = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 "+str(x)+" 일로 선정되었습니다.")

''' 문자열 '''
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = '''
# 나는 소년이고,
# 파이썬은 쉬워요
# '''
# print(sentence3)

''' 슬라이싱 '''
# jumin = "951101-1234567"
# sung = ''
# if (jumin[7]=='1' or jumin[7]=='3'):
#     print("성별 : 남자")
# elif(jumin[7]=='2' or jumin[7]=='4'):
#     print("성별 : 여자")
# print("연 : " + jumin[0:2]) # 0:2 --> 0,1
# print("월 : " + jumin[2:4]) # 2:4 --> 2,3
# print("일 : " + jumin[4:6]) # 4:6 --> 4,5
# print("생년월일 : " + jumin[:6]) # :6 --> 처음부터~5까지
# print("주민번호 뒷자리 : " + jumin[7:]) # 7: --> 7부터 끝까지
# print("주민번호 뒷자리 : " + jumin[-7:])# -7: --> -7부터 끝까지

''' 문자열 처리함수 '''
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) # 해당 문자가 대문자일 경우 True 출력
# print(len(python))         # 문자열 길이 출력
# print(python.replace("Python", "Java")) # 문자열 교체

# index = python.index("n")
# print(index) # n이라는 글자가 몇번째 위치에 존재하는 지 출력
# index = python.index("m", index +1) 
# print(index) # 첫 n 글자 다음의 n을 검색

# print(python.find("n"))
# print(python.find("java")) # 해당 글자가 없으면 -1 변환
# #print(python.index("java"))# 에러 메세지 출력
# print(python.count("n")) # 해당 글자가 몇번 사용됐는지 출력

''' 문자열 포맷 ''' 
# print("a"+'b')
# print('a','b')

# # 방법 1
# print("나는 %d살 입니다." % 20)          # 정수
# print("나는 %s을 좋아해요" % "python")   # 문자열
# a = 'A'
# print("Apple 은 %c로 시작해요" % a)      # 문자
# print('나는 %s살 입니다.' %20)           # 그냥 문자열로도 가능함
# print("나는 %s색과 %s색을 좋아해요" %('파란','빨강')) # 두 개 이상부터는 %(,)

# # 방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age =20, color="빨간"))

# # 방법 4(v3.6 이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

''' 탈출 문자 '''
# print("백문이 불여일견 \n 백견이 불여일타") # \n : 문장 내에서 줄 바꿈

# # 저는 "나도코딩" 입니다.
# print('저는 "나도코딩" 입니다.')
# print('저는 \"나도코딩\" 입니다.')         # \" \' : 문장 내에서 따옴표

# # \\ : 문장 내에서 \ -> \하나만 쓰면 오류남
# print("C:\\Users\\jjgwe_t9klr6g\\OneDrive")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple \rPine")

# # \b : 백스페이스(한 글자 삭제)
# print("Redd\bApple")

# # \t : tab
# print("Red\tApple")

''' Quiz 3 '''
# # 사이트 별로 비밀번호를 만들어 주는 프로그램 작성
# # 예) http://naver.com
# # 규칙1 : http:// 부분 제외
# # 규칙2 : 처음 만나는 점. 이후 내용 제외 -> naver
# # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수 + "!"로 구성
# # 생성된 비밀번호 : nav51!

# # 내 풀이
# addr= "http://naver.com"
# index_1=addr.index("//")       # 규칙 1 // 이후
# index_2=addr.count('e')        # 규칙 3 'e' count  
# index_3=addr.index(".")        # 규칙 3 .이후 삭제 
# index =addr[index_1+2:index_3] # 규칙 2까지 완료   
# index_len = len(index)
# print("생성된 비밀번호는 %s%s%s%s" %(index[0:3],str(index_len),index_2,'!'))

# # 풀이 
# my_str = addr.replace("http://","")  # 규칙 1
# my_str = my_str[:my_str.index('.')]  # 규칙 2
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) +'!'
# print("{0}의 비밀번호는 {1} 입니다.".format(addr,password))

''''''''''''''''''''''''''''''''

''' 리스트 '''

# # 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석","조세호","박명수"]

# # index
# print(subway.index("조세호"))

# # append
# subway.append("하하")  # append 맨 뒤에 추가
# print(subway)

# # insert
# subway.insert(1,"정형돈")
# print(subway)

# # pop
# print(subway.pop())
# print(subway)

# # count
# subway.append("유재석")
# print(subway.count("유재석"))

# # sort
# num_list = [5,2,3,1,4]
# num_list.sort()
# print(num_list)
# # reverse
# num_list.reverse()
# print(num_list)

# # clear
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용가능
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]

# # extend
# num_list.extend(mix_list)
# print(num_list)

''' 사전 '''
cabinet = {3:"유재석",100:"김태호"}
# print(cabinet[3],cabinet[100])

# print(cabinet.get(3))
# #print(cabinet[5])     # key 값이 없으면 오류 메세지 출력 및 프로그램 종료
# print(cabinet.get(5))  # key 값이 없으면 None 반환
# print(cabinet.get(5,'사용 가능')) # None 대신 ''로 반환

# print (3 in cabinet)   # dict에 해당 key가 있는 지 bool 형태로 반환
# print ("유재석" in cabinet) 

# cabinet = {"A-3":"유재석","B-100":"김태호"} # str 형태로도 key 지정가능
# print(cabinet["A-3"],cabinet["B-100"])

# # 변경 및 추가
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 삭제
# del cabinet["C-20"]
# print(cabinet)

# # key만 출력
# print(cabinet.keys())

# # value 만 출력
# print(cabinet.values())

# # key value 쌍으로 출력
# print(cabinet.items())

# # 전체 삭제
# cabinet.clear()
# print(cabinet)

''' 튜플 '''
# menu = ("돈까스", "치즈까스")
# print(menu[0],menu[1])

# #menu.add("생선까스") # 튜플은 값을 추가하거나 변경 불가
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

# name,age,hobby = ("김족국",20,"코딩")
# print(name,age,hobby)

''' 집합(set) '''
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set) # {1,2,3} 중복 허용X

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 출력(java & python)
# print(java & python)
# print(java.intersection(python))

# # 합집합 출력(java | python)
# print(java | python)
# print(java.union(python))

# # 차집합 출력(java O, python X)
# print(java - python)
# print(java.difference(python))

# # python 집합에 추가
# python.add("김태호")
# print(python)

# # java 집합에서 빼기
# java.remove("김태호")
# print(java)

''' 자료구조의 변경 '''
# menu = {"커피","우유","주스"} # set 집합
# print(menu,type(menu))

# menu = list(menu)
# print(menu,type(menu)) # list로 변환

# menu = tuple(menu)
# print(menu,type(menu)) # tuple로 변환

# menu = set(menu)
# print(menu,type(menu)) # set로 변환

''' Quiz 4 '''
# # 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받는다.
# # 추첨 프로그램을 작성하라.

# # 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20
# # 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# # 조건 3 : random 모듈의 shuffle과 sample 활용

# from random import *
# member = list(range(1,21)) # 1~20 숫자를 list로 생성
# shuffle(member)
# winner=sample(member,4)
# print(winner)
# print(f"치킨 당첨자는 {winner[0]} 입니다.")
# print(f"커피 당첨자는 {winner[1:]} 입니다.")

''' if문 '''
# weather = input("오늘 날씨는 어때요?")

# if weather =="비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없음")

# temp = int(input("기온은 어때요?"))

# if 30<=temp:
#     print("더워요 나가지 마세요")
# elif 10<=temp<30:
#     print("날씨가 좋아요")
# elif 0<= temp<10:
#     print("외투를 챙기세요")
# else:
#     print("추워요")

''' for문 '''
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for i in range(1,10):
#     print(f"대기번호 : {i}")

# starbucks=["아이언맨","토르","그루트"]
# for customer in starbucks:
#     print(f"{customer}님, 커피가 준비되었습니다.")

''' while문 '''
# customer = "토르"
# index = 5
# while index>=1:
#     print(f"{customer}, 커피가 준비 되었습니다. {index} 번 남았어요.")
#     index -=1
#     if index ==0: # 5번 호출 후에
#         print("커피는 제가 마십니다.")

# customer = "아이언맨"
# index = 5
# while True:
#     print(f"{customer}, 커피가 준비 되었습니다. 호출 {index}")
#     index-=1
#     if index == 0: # 5번 호출 후에
#         print("커피는 제가 마십니다.")
#         break

# customer = "토르"
# person = "Unknown"

# while person != customer: # 내가 부른 손님이 올때까지 반복
#     print(f"{customer}, 커피가 준비 되었습니다.")
#     person = input("이름이 어떻게 되세요?")
#     if person == customer:
#         break
#     else:
#         print("너꺼 아니에용")
# print("커피를 받으세요")

''' continue / break '''
# absent = [2,5] # 결석
# no_book = [7]
# for student in range(1,11): #1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"오늘 수업 여기까지, {student}는 교무실로 와")
#         break
#     print(f"{student},책을 읽어봐")

''' 한 줄 for문 '''
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am Groot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am Groot"]
# print(students)
# students = [i.upper() for i in students]
# print(students)

''' Quiz 5 '''
# # 50 명의 승객과 매칭기회가 있다. 총 탑승 승객 수를 구하는 프로그램
# # 조건 1 : 승객별 운행 소요 시간은 5~50 분
# # 조건 2 : 당신은 소요 시간 5~15 사이의 승객만 매칭

# from random import *

# cust=[i for i in range(1,51)]
# count = 0
# for t in cust:
#     time=randint(5,50)
#     if 5<=time<=15:
#         print(f"[O] {t} 손님 (소요시간 : {time})")
#         count+=1
#     else:
#         print(f"[X] {t} 손님 (소요시간 : {time})")

# print(f"총 탑승 승객 : {count}분")

''' 함수 '''
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()
# # 입금 함수
# def deposit(balance, money): 
#     print(f"입금이 완료되었습니다. 잔액은 {balance + money}입니다.")
#     return balance + money
# # 출금 함수
# def withdraw(balance, money): 
#     if balance>= money:
#         print(f"출금이 완료되었습니다. 잔액은 {balance - money}입니다.")
#     else:
#         print(f"잔액 부족. 잔액은 {balance}입니다.")
#     return balance
# # 수수료 있는 출금
# def withdraw_night(balance,money): 
#     commission = 100 # 수수료
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance,1000)
# balance = withdraw(balance,500)
# commission,balance = withdraw_night(balance, 500)
# print(f"수수료는 {commission}이고, 잔액은 {balance}입니다.")

''' 기본값 '''
# def profile(name, age, main_lang):
#     print(f"이름 : {name}\t 나이 : {age}\t 사용 언어 : {main_lang}")
# profile("유재석",20,"Python")
# profile("김태호",25,"Java")

# def profile1(name, age=17, main_lang="Python"): # 기본값 설정
#     print(f"이름 : {name}\t 나이 : {age}\t 사용 언어 : {main_lang}")
# profile1("유재석",20,"Python")
# profile1("김태호",25,"Java")
# profile1("장준기") # 안 적은 항목은 기본값으로 출력

''' 키워드 값 '''
# def profile(name, age, main_lang):
#     print(f"이름 : {name} 나이 : {age} 사용 언어 : {main_lang}")
# profile(age=20,main_lang="Python",name="유재석") # 키워드 지정 후 함수 호출하면 알아서 들어감

''' 가변인자 '''
# def profile(name, age, *language): # 가변인자 *language
#      print(f"이름 : {name} 나이 : {age} ",end =" ")
#      for lang in language:
#          print(lang,end=" ")
#      print()

# profile("유재석", 20, "Python", "Java", "C", "C++","C#") 
# # 5개로 설정했을 때 6개 입력하면 에러
# profile("김태호", 25, "Kotlin", "Swift") 
# # 부족하면 빈 값을 넣어줘야함

''' 지역변수와 전역변수 '''
gun = 10                  # 지역 변수
def checkpoint(soldiers): # 경계근무
    global gun            # 전역 공간에 있는 gun 사용 (코드 관리가 어려워짐)
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")

print(f"전체 총 : {gun}")
checkpoint(2)             # 2명이 경계 근무에 나감
print(f"남은 총 : {gun}")

### 이 방법을 더 많이 사용한다. ###
gun = 10                          # 지역 변수
def checkpoint_ret(gun,soldiers): # 경계근무
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
gun = checkpoint_ret(gun,2)       # 2명이 경계 근무에 나감
print(f"남은 총 : {gun}")

''' Quiz 6 '''
# # 표준 체중을 구하는 프로그램을 작성하라

# # (성별에 따른 공식)
# # 남자 : 키(m) x 키(m) x 22
# # 여자 : 키(m) x 키(m) x 21

# # 조건 1: 표준 체중은 별도의 함수 내에서 계산
# # 함수명 : std_weight, 전달값 : 키(height), 성별(gender)
# # 조건 2: 표준 체중은 소수점 둘째자리까지 표시

# def std_weight(height, gender):
#     if gender == "여자":
#         weight=height*height*21
#     elif gender == "남자":
#         weight=height*height*22
#     else :
#         print("입력 오류")
#     return weight

# height =int(input())
# gender =str(input())
# weight=round(std_weight(height/100,gender),2)
# print(f"키 {height} {gender}의 표준 체중은 {weight}kg 입니다.")

''' 표준 입출력 '''
# print("Python","Java") # 띄어쓰기 포함으로 출력
# print("Python"+"Java") # 붙어서 출력

# # sep = "" -> ,부분에 "" 내용을 넣음
# print("Pyhton","Java","JavaScript", sep="") 
# print("Pyhton","Java","JavaScript", sep=" vs ") # Pyhton vs Java vs JavaScript

# # end = "" -> 다음 문장이 바로 붙음
# print("Pyhton","Java","JavaScript", sep=" vs ", end ="?")
# print("무엇이 더 재밌을까요?") 

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력으로 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러로 출력

# scores = {"수학":0, "영어":50, "코딩": 100}
# for subject,score in scores.items(): # dictionary 가져올때는 변수명.items
#     # print(subject,score)
#     print(subject.ljust(4),str(score).rjust(4),sep=":")
#     # ljust 왼쪽 정렬, rjust 오른쪽 정렬

# # 은행 대기순번 표
# # 001 002 003 ....
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # 값이 없는 부분은 0으로 채워라

# answer = input("아무 값이나 입력하세요 : ") # 항상 문자열로 들어온다.
# print("입력하신 값은 "+ answer + "입니다.")

''' 다양한 출력포맷 '''
# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))

# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기 +부호도 찍기
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기, 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(100000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시
# print("{0:.2f}".format(5/3)) # 2째 자리까지 표시

''' 파일 입출력 '''
# score_file = open("score.txt", "w", encoding="utf8") # 쓰기 목적으로 열기
# # 내용
# print("수학 : 0", file=score_file) 
# print("영어 : 50", file=score_file)
# score_file.close() # 닫기

# score_file = open("score.txt", "a", encoding="utf8") # 고치기..?
# # 내용
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") 
# # 줄바꿈이 자동이 아님
# score_file.close() # 닫기

# score_file = open("score.txt", "r", encoding="utf8") # 읽기
# # 내용
# print(score_file.read()) # 파일 전체 읽기
# # 줄바꿈이 자동이 아님
# score_file.close() # 닫기

# score_file = open("score.txt", "r", encoding="utf8") # 읽기
# # 내용
# print(score_file.readline(), end="") # 한 줄씩 읽기
# print(score_file.readline(), end="") # 한 줄씩 읽기
# print(score_file.readline(), end="") # 한 줄씩 읽기
# print(score_file.readline(), end="") # 한 줄씩 읽기
# score_file.close() # 닫기

# # 해당 파일이 몇 줄인지 모를 때 한줄씩 출력 방법 1
# score_file = open("score.txt", "r", encoding="utf8") # 읽기
# # 내용
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close() # 닫기

# # 해당 파일이 몇 줄인지 모를 때 한줄씩 출력 방법 2
# score_file = open("score.txt", "r", encoding="utf8") # 읽기
# # 내용
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close() # 닫기

''' pickle '''
# import pickle
# profile_file = open("profile.pickle", "wb") # binary 파일
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 불러오기
# print(profile)
# profile_file.close()

''' with '''
# import pickle
# # 종료문이 필요 없음
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# # 파일 쓰기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부하는 중")
# # 파일 읽기
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

''' Quiz7 '''
# # 매주 1회 작성해야 하는 보고서
# # - X 주차 주간보고 -
# # 부서 :
# # 이름 :
# # 업무 요약 :
# # 1~50주차까지의 보고서 파일을 만드는 프로그램을 작성하라

# x= [i for i in range(1,51)] 
# for i in x:
#     with open(f"{i}주차.txt","w",encoding="utf8") as file:
#         file.write(f"- {i} 주차 주간보고 -")
#         file.write("\n부서 :")
#         file.write("\n이름 :")
#         file.write("\n업무 요약 :")

''' 클래스 '''
# # 마린 : 공격 유닛, 군인, 총을 쏜다.
# name = "마린" 
# hp = 40       
# damage = 5

# print(f"{name}유닛이 생성되었습니다.")
# print(f"체력:{hp}, 공격력:{damage}")

# # 탱크 : 공격 유닛, 탱크, 포를 쏜다. 일반 모드/시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# # 탱크 한대가 더 추가됐을때
# tank_name2 = "탱크2"
# tank_hp2 = 150
# tank_damage2 = 35

# print(f"{tank_name}유닛이 생성되었습니다.")
# print(f"체력:{tank_hp}, 공격력:{tank_damage}")

# # 공격하는 함수
# def attack(name, location, damage):
#     print(f"{name} : {location}방향으로 적군을 공격합니다.[공격력 {damage}]")

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# # 탱크 한대가 더 추가됐을때 공격 표시  ==> Class로 생성
# attack(tank_name2,"1시",tank_damage2)

# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name}유닛이 생성되었습니다.")
#         print(f"체력:{self.hp}, 공격력:{self.damage}")

# marine1 = Unit("마린",40, 5)
# marine2 = Unit("마린",40, 5)
# tank = Unit("탱크",150,35)

'''__init__'''
# # marine이나 tank와 같이 클래스로 만들어지는 객체
# # 객체가 만들어질때 자동으로 호출되는 함수
# # marine, tank : Unit 함수의 인스턴스
# # name, hp, damage : 멤버 변수

# # 레이스 : 공중 유닛, 비행기, 클로킹
# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}") 
# # 멤버 변수는 클래스 외부에서 사용이 가능하다

# # 마인드 컨트롤로 뺏음
# wraith2 = Unit("레이스",80,5)
# # 클로킹 멤버 변수를 추가
# wraith2.clocking = True # 클로킹 업그레이드 완료
# if wraith2.clocking == True:
#     print(f"{wraith2.name}은 클로킹 상태입니다.")

''' 메소드 '''
# # 위에서 만든 클래스 가져옴
# # 일반 유닛
# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{self.name}유닛이 생성되었습니다.")
#         print(f"체력:{self.hp}, 공격력:{self.damage}")
    
# class AttackUnit:
#     def __init__(self,name,hp,damage):
#         self.name = name # name:전달받은 인자
#         self.hp = hp
#         self.damage = damage

#     def attack(self,location): # 메소드 앞에는 무조건 self가 들어간다.
#         print(f"{self.name} : {location}방향으로 적군을 공격합니다.[공격력 {self.damage}]")
#         # location은 전달받은 값을 출력

#     def damaged (self,damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp<=0:
#             print(f"{self.name} : 파괴되었습니다.")

# # 파이어뱃으로 공격
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# # 공격 두번
# firebat1.damaged(25)
# firebat1.damaged(25)

''' 상속 '''
# class Unit:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit): # name,hp는 중복되기 때문에 Unit에서 상속
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp) # 이렇게 하면 가져올 수 있다.
#         self.damage = damage
#     def attack(self,location): # 메소드 앞에는 무조건 self가 들어간다.
#         print(f"{self.name} : {location}방향으로 적군을 공격합니다.[공격력 {self.damage}]")
#         # location은 전달받은 값을 출력

#     def damaged (self,damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp<=0:
#             print(f"{self.name} : 파괴되었습니다.")


# # 파이어뱃으로 공격
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# # 공격 두번
# firebat1.damaged(25)
# firebat1.damaged(25)

''' 다중 상속 '''
# class Unit:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit): # name,hp는 중복되기 때문에 Unit에서 상속
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp) # 이렇게 하면 가져올 수 있다.
#         self.damage = damage
#     def attack(self,location): # 메소드 앞에는 무조건 self가 들어간다.
#         print(f"{self.name} : {location}방향으로 적군을 공격합니다.[공격력 {self.damage}]")
#         # location은 전달받은 값을 출력

#     def damaged (self,damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp<=0:
#             print(f"{self.name} : 파괴되었습니다.")

# # 드랍쉽 : 공중 유닛, 수송기, 공격X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도{self.flying_speed}]")
    
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit,Flyable): # 공중 유닛, 공격 가능 다중 상속
#     def __init__(self, name, hp, damage, flying_speed): # 초기화
#         AttackUnit.__init__(self,name,hp,damage)
#         Flyable.__init__(self,flying_speed)

# # 발키리 : 공중 공격 유닛,
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

''' 연산자 오버로딩, 메서도 오버라이딩 '''
# # 부모 클래스에서 정의한 메소드 말고 자식 클래스에서 정의한 메소드를 사용하고 싶을 때
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self,location):
#         print("[지상 유닛 이동]")
#         print(f"{self.name} : {location}방향으로 이동합니다. [속도 {self.speed}]")

# class AttackUnit(Unit): # name,hp는 중복되기 때문에 Unit에서 상속
#     def __init__(self,name,hp,damage,speed):
#         Unit.__init__(self,name,hp,speed) # 이렇게 하면 가져올 수 있다.
#         self.damage = damage
#     def attack(self,location): # 메소드 앞에는 무조건 self가 들어간다.
#         print(f"{self.name} : {location}방향으로 적군을 공격합니다.[공격력 {self.damage}]")
#         # location은 전달받은 값을 출력

#     def damaged (self,damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
#         if self.hp<=0:
#             print(f"{self.name} : 파괴되었습니다.")

# # 드랍쉽 : 공중 유닛, 수송기, 공격X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도{self.flying_speed}]")
    
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit,Flyable): # 공중 유닛, 공격 가능 다중 상속
#     def __init__(self, name, hp, damage, flying_speed): # 초기화
#         AttackUnit.__init__(self,name,hp,0,damage) # 지상 speed 0
#         Flyable.__init__(self,flying_speed)

#     # 공중 유닛도 move 메소드로 처리함 (연산자 오버로딩)
#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name,location)

# # 벌쳐 : 지상 공격 유닛,
# vulture = AttackUnit("벌쳐",80,10,20)
# # 배틀크루져 : 공중 유닛, 체력 높음
# battlecrusier = FlyableAttackUnit("배틀크루져",500,25,3)


# vulture.move("11시")       # 지상은 move
# # battlecrusier.fly(battlecrusier.name,"9시") # 공중은 fly 나눠주는게 귀찮음
# battlecrusier.move("9시")  # 공중은 fly

''' pass '''
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 함수가 완성되지 않았지만 일단 진행

# # 서플라이 디폿
# suply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("game start")
# def game_over():
#     pass

# game_start()
# game_over() # pass 됐다고 하는데 잘 모르겠음

''' super '''
# class Unit:
#     def __init__(self,name,hp,speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self,name,hp,0)
#         super().__init__(name,hp,0) # self만 빼고 받는다.
#         self.location = location

''' Quiz 8 클래스 '''
# # 주어진 코드를 활용하여 부동산 프로그램을 작성하라.
# # 총 3대의 매물이 있다.
# # 강남 아파트 매매 10억 2010년
# # 마포 오피스텔 전세 5억 2007년
# # 송파 빌라 월세 500/50 2000년

# # 코드
# class House:
#     # 매물 초기화
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         # 매개변수 설정
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
    
#     # 매물 정보 표시
#     def show_detail(self):
#         print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")
    
# houses = []

# house1=House("강남","아파트","매매","10억",2010)
# house2=House("마포","오피스텔","전세","5억",2007)
# house3=House("송파","빌라","월세","500/50",2000)

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print(f"총 {len(houses)}개의 매물이 있습니다.")

# for house in houses:
#     house.show_detail()

''' 예외처리 '''
# try:
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 :")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 :")))
#     #nums.append(int(nums[0]/nums[1]))
#     print(f"{nums[0]}/{nums[1]}={nums[2]}")

# # 잘못된 입력 값 예외 처리
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")

# # 0으로 나눌 때 에러처리
# except ZeroDivisionError as err:
#     print(err)

# # 알 수없는 에러 처리
# except Exception as err:
#     print("알 수 없는 에러가 발생했습니다.")
#     print(err)


''' 에러 발생시키기 '''
# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1=(int(input("첫 번째 숫자를 입력하세요 :")))
#     num2=(int(input("두 번째 숫자를 입력하세요 :")))

#     if num1 >= 10 or num2 >=10:
#         raise ValueError
#     print(f"{num1}/{num2}={int(num1/num2)}")

# # 잘못된 입력 값 예외 처리
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")

''' 사용자 정의 에러처리 '''
# class BigNumberError(Exception):
#     def __init__(self, msg) :
#         self.msg = msg
#     def __str__(self):
#         return self.msg
        
# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1=(int(input("첫 번째 숫자를 입력하세요 :")))
#     num2=(int(input("두 번째 숫자를 입력하세요 :")))

#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1}/{num2}={int(num1/num2)}")

# # 잘못된 입력 값 예외 처리
# except BigNumberError as err:
#     print("에러! 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)

''' finally '''
# #에러가 뜨던 성공하던 무조건 실행된다.
# class BigNumberError(Exception):
#     def __init__(self, msg) :
#         self.msg = msg
#     def __str__(self):
#         return self.msg
        
# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1=(int(input("첫 번째 숫자를 입력하세요 :")))
#     num2=(int(input("두 번째 숫자를 입력하세요 :")))

#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError(f"입력값 : {num1}, {num2}")
#     print(f"{num1}/{num2}={int(num1/num2)}")

# # 잘못된 입력 값 예외 처리
# except BigNumberError as err:
#     print("에러! 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("사용해주셔서 감사합니다.") # 무조건 실행된다.

''' Quiz 9 예외처리 구문 '''
# # 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작
# # 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
# # 출력 메시지 : "잘못된 값을 입력하였습니다."
# # 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
# # 치킨 소진 시 사용자 정의 에러 SoldOutError를 발생시키고 프로그램 종료
# # 출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# class SoldOutError(Exception):
#     def __init__(self,msg):
#         self.msg =msg

#     def __str__(self):
#         return self.msg

# chicken = 10 # 재고량
# waiting = 1  # 대기 번호 시작 

# while(True):
#     try:
#         print(f"[ 남은 치킨 : {chicken} ]")
#         # 남은 재고가 0일 때 
#         if chicken <= 0:
#             raise SoldOutError("재고가 없다.")
#         # 주문 받기
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        
#         # 입력 값이 str이거나 1보다 작은 숫자일 경우
#         if type(order) == str or order<1:
#             raise ValueError

#         if order > chicken: #재고량 보다 많을 경우
#             print("재료가 부족합니다.")
        
#         # 대기번호 +1, 재고에서 주문량만큼 감소
#         else:
#             print(f"[ 대기번호 {waiting} ] {order} 마리 주문이 완료되었습니다.")
#             waiting+=1
#             chicken-=order

#     except ValueError as err: # 입력값 예외처리
#         print("잘못된 값을 입력하였습니다.")
#         print(err)

#     except SoldOutError as err : # 재고량 예외처리
#         print(err)
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

#https://www.youtube.com/watch?v=kWiCuklohdY 5:14:50