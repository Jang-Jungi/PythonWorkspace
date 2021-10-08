''' Quiz 2 랜덤 함수 '''
# from random import *
# x = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 "+str(x)+" 일로 선정되었습니다.")

''' Quiz 3 문자열 '''
# # 사이트 별로 비밀번호를 만들어 주는 프로그램 작성
# # 예) http://naver.com
# # 규칙1 : http:// 부분 제외
# # 규칙2 : 처음 만나는 점. 이후 내용 제외 -> naver
# # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수 + "!"로 구성
# # 생성된 비밀번호 : nav51!

''' Quiz 4 리스트 랜덤 함수 '''
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

''' Quiz 5 for + if 문 '''
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

''' Quiz 6 함수 '''
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