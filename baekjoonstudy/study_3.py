'''8단계 기본 수학 1단계 '''
# # 1712 손익분기점
# A,B,C = map(int,input().split())
# # A 고정비용 B 가변비용 C 노트북 가격 n 대수
# # 총 비용 : A+B*n //  판매비용 : C*n 판매비용이 더 커야한다.
# if B>=C:
#     print(-1)
# else:
#     print(A/(C-B)+1)

# # 2292 벌집
# # 1번 방은 무조건 지나야하고
# # 2~7 1번을 둘러싼 육각형 6개
# # 8~19 2~7 둘러싼 육각형 12개
# # 20~37 8~19를 둘러싼 육각형 18개
# N = int(input())
# count = 1             # N까지 지나는 방의 개수 count
# home = 1              # 초기값 1
# while N > home:       # N이 포함되는 범위를 찾을 때까지 반복문 실행 // N보다 커지면 반복문 종료
#     home += 6*count   # 범위는 위와 같이 6*count로 증가함
#     count +=1         # count +1
# print(count)
    
# # 1193 분수찾기
# N = int(input())
# line = 0    # N이 속하는 line
# max_num = 0 # N이 속하는 line 중 사선 라인의 가장 큰 숫자
# while N > max_num:
#     line+=1
#     max_num+=line

# gap = max_num - N
# if line % 2 == 0:       # 사선 line이 짝수
#     top = line - gap    # 분자
#     under = gap + 1     # 분모
# else:                   # 사선 line이 홀수
#     top = gap + 1       # 분자
#     under = line - gap  # 분모
# print(f'{top}/{under}')

# # 2869 달팽이는 올라가고 싶다.
# # A : 낮에 올라감 
# # B : 밤에 미끄러짐
# # V : 나무 막대 길이
# A,B,V = map(int,input().split())
# distance = A        # 초기값 A로 설정 마지막날 올라가는 높이
# date_cnt = 1        # 날짜 계산
# while V > distance: 
#     date_cnt+=1
#     distance+=(A-B) # 정상적으로 1일이 지났을 때 올라가는 높이

# print(date_cnt)

# # 2869 시간 제한 X
# import math

# a, b, v = map(int, input().split())
# # a= 올라가는 길이, b= 떨어지는길이, v= 나무높이 

# day = math.ceil((v-a)/(a-b)) + 1
# print(day)

# # 10250 ACM 호텔
# n = int(input())
# for i in range(n):
#     H,W,N = map(int,input().split())
#     num = N//H +1                # 몫 1:101호 // H+1:201호 // 2H+1:301호
#     floor = N % H                # 나머지 1:101호 // 2:102호 // 3:103호
#     if N % H == 0:               # 나누어 떨어질때는 별도
#         num = N//H               # 몫 1,2,3...증가
#         floor = H                # 나머지 10(H)호 20(H)호
#     print(f'{floor*100+num}')

# # 2775 부녀회장이 될테야
# t = int(input())           # 반복횟수
# for _ in range(t):
#     floor = int(input())                  # 층 입력
#     num   = int(input())                  # 호수 입력
#     floor_0 = [x for x in range(1,num+1)] # 0층 사는 사람
#     for k in range(floor):                # 층 
#         for i in range(1,num):            # 호수
#             floor_0[i] += floor_0[i-1]    # 수 계산
#     print(floor_0[-1])

# # 2839 설탕 배달
# N = int(input()) # 총 무게
# bag = 0
# while N >= 0 :
#     if N % 5 == 0 :      # 5의 배수이면
#         bag += (N // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     else:                # 5의 배수가 아닐경우
#         N -= 3  
#         bag += 1         # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)

# # 10757 큰 수 A+B
# A,B = map(int,input().split())
# print(A+B)

#1011 Fly me to the Alpha Centauri
t = int(input())

# for _ in range(t):
#     x, y = map(int,input().split())
#     distance = y - x
#     count = 0  # 이동 횟수
#     move = 1  # count별 이동 가능한 거리
#     move_plus = 0  # 이동한 거리의 합
#     while move_plus < distance :
#         count += 1
#         move_plus += move  # count 수에 해당하는 move를 더함
#         if count % 2 == 0 :  # count가 2의 배수일 때, 
#             move += 1  
#     print(count)