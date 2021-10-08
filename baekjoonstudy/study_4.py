# # 1978 소수 찾기
# N = int(input())              # 판별받을 숫자 개수 (사용X)
# M = map(int,input().split())  # 판별 할 숫자
# cnt = 0                       # 소수로 판별 된 숫자
# for x in M:                   # 숫자를 한개씩 
#     error = 0                 # 소수X
#     if x>1:                   # 1은 소수 제외
#         for i in range(2,x):  # 2 ~ 해당 숫자-1까지 반복문
#             if x % i == 0:    # x보다 작은 수에 의해 나누어진다면
#                 error+=1      
#         if error == 0:        # 나눠지지 않으면
#             cnt +=1
# print(cnt)

# # 2581 소수
# M = int(input())           # M 최소 범위
# N = int(input())           # N 최대 범위
# sosu=[]                    # sosu 리스트
# cnt = 0                    # 계산
# for x in range(M,N+1):     # M~N까지 
#     error = 0 
#     if x>1:
#         for i in range(2,x): 
#             if x%i ==0:
#                 error+=1
#         if error == 0:
#             cnt+=x         # 소수들 더하기
#             sosu.append(x) # 리스트에 추가
# if cnt == 0:               # 해당 범위에 소수가 없다면
#     print(-1)
# else:                     
#     print(cnt)
#     print(min(sosu), sosu) # 심심해서 리스트 전부 출력해봤다.

# # 11653 소인수 분해
# N = int(input())
# while N != 1:               # 1이 될때까지
#     for i in range(2, N+1): # 2~N까지
#         if N % i == 0:      # 나눠지면
#             print(i)        # i출력
#             N = N//i        
#             break

# # 1929 소수 구하기
# M,N = map(int, input().split())
# sosu=[]                    # sosu 리스트
# cnt = 0                    # 계산
# for x in range(M,N+1):     # M~N까지 
#     error = 0 
#     if x>1:
#         for i in range(2,x): 
#             if x%i ==0:
#                 error+=1
#         if error == 0:
#             cnt += x
#             sosu.append(x) # 리스트에 추가
# if cnt == 0:               # 해당 범위에 소수가 없다면
#     print(-1)
# else:          
#     for k in sosu:          
#         print(k) 

# # 4948 베르트랑 공준
# while(True):
#     M = int(input())
#     if M==0:
#         break
#     N = 2*M
#     sosu=[]                    # sosu 리스트
#     cnt = 0                    # 계산
#     for x in range(M,N+1):     # M~N까지 
#         error = 0 
#         if x>1:
#             for i in range(2,x): 
#                 if x%i ==0:
#                     error+=1
#             if error == 0:
#                 cnt += x
#                 sosu.append(x) # 리스트에 추가
#     if cnt == 0:               # 해당 범위에 소수가 없다면
#         print(-1)
#     else:          
#         print(len(sosu))

# import math

# # 소수의 집합을 구함
# nums = {x for x in range(2, 246_913) if x == 2 or x % 2 ==1}
# # nums = 2와 홀수로 이루어진 집합
# for odd_num in range(3, int(math.sqrt(246_912))+1, 2):  # 3부터 최대값의 제곱근까지 홀수만
#     nums -= {i for i in range(2 * odd_num, 246_913, odd_num) if i in nums}
#     # 홀수의 배수로 이루어진 집합을 생성해서 빼줌

# # 반복문 만들기
# while True:
#     n = int(input())
#     if n == 0:
#         break  # n == 0 이면 반복문을 끝냄
#     sosu_list = [i for i in range(n+1, 2*n+1) if i in nums]
#     # 소수 집합(nums)안에서 n보다 크고 2*n보다 작거나 같은 수의 리스트를 생성
#     print(len(sosu_list))

# # 9020 골드바흐의 추측

# # 소수 집합 만들기
# nums = {x for x in range(2, 10_001) if x == 2 or x % 2 == 1}
# # nums = 2와 홀수로 이루어진 집합
# for odd in range(3, 101, 2): # 101 == int(math.sqrt(10_000)) + 1
#     nums -= {i for i in range(2 * odd, 10_001, odd) if i in nums}
#     # 홀수의 배수로 이루어진 집합을 빼줌

# # 골드바흐 수를 출력
# t = int(input())
# for _ in range(t):
#     even = int(input())
#     half = even//2  # 입력받은 짝수를 2로 나눈 몫을 구함. / 기호를 쓰면 실수가 됨.
#     for x in range(half, 1, -1):  # 차이가 적은 두 수를 구하기 위해서 큰수부터 꺼냄
#         if (even-x in nums) and (x in nums):  # even-x 와 x가 소수 집합에 포함 되었는지 확인
#             print(x, even-x)  # 작은수부터 출력
#             break

# # 1085 직사각형에서 탈출
# x, y, w, h = map(int, input().split())
# print(min(x, y, w-x, h-y))

# # 3009 네 번째 점
# x_nums = []           # x좌표를 담을 리스트
# y_nums = []           # y좌표를 담을 리스트
# for _ in range(3):     
#     x,y = map(int,input().split()) # x,y좌표
#     x_nums.append(x)  
#     y_nums.append(y)

# for i in range(3):   
#     if x_nums.count(x_nums[i])==1: # 3개의 점 중 x좌표가 하나인 값
#         x4 =  x_nums[i]
#     if y_nums.count(y_nums[i])==1: # 3개의 점 중 y좌표가 하나인 값
#         y4 =  y_nums[i]
# print(x4,y4)

# # 4153 직각삼각형
# import math

# while(True):
#     T = list(map(int,input().split()))
#     if T == [0, 0, 0] :     # 0,0,0 종료
#         break
#     else:
#         T.sort()            # 오름차순 정력
#         x1 = int(T[0])      # int로 변환
#         x2 = int(T[1])
#         x3 = int(T[2])
#         if math.pow(x1, 2) + math.pow(x2, 2) == math.pow(x3, 2): # 피타고라스 정리
#             print("right")
#         else:
#             print("wrong")
# print("종료")

# # 3053 택시 기하학
# import math

# r = int(input())
# print(r*r*math.pi)  # 원의 넓이
# print(2*r*r)  # 택시기하학 원의 넓이

# # 1002 터렛
# import math

# n = int(input())

# for _ in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
#     if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
#         print(-1)
#     elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
#         print(1)
#     elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
#         print(2)
#     else:
#         print(0)  # 그 외에