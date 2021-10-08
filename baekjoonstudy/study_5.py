'''10 단계 재귀 함수'''

# # 10872 팩토리얼          
# def factorial(N):        # 함수 선언
#     result = 1           # 초기 값 1 >> 0! = 1이다
#     if N > 0 :           # 1보다 클 경우
#         result = N * factorial(N-1) # 재귀함수 호출
#     return result        # 결과값 반환

# N = int(input()) 
# if(0<=N<=12):
#     print(factorial(N))  # 결과 출력
# else:
#     print("0~12 숫자만 입력")

# # 10870 피보나치 수 5         
# def fibonacci(n):
#     if n <= 1:            # 초기값 셋팅
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n = int(input())
# if (0<=n<=20):
#     print(fibonacci(n))
# else :
#     print("0~20 숫자만 입력")

# # 2447 별 찍기 -10

# def star(i):
#     global arr
#     idx = [i for i in range(n) if (i//3 ** cnt_)%3==1]
#     for i in idx:
#         for j in idx:
#             arr[i][j]= " "
# n=int(input())
# v=n; cnt=0
# while v!=1:
#     v/=3
#     cnt+=1

# arr = [["*"]*n for _ in range(n)]
# for cnt_ in range(cnt):
#     star(cnt_)

# print('\n'.join([''.join([str(i)for i in row])for row in arr]))

# # 11729 하노이 탑 이동 순서
# n = int(input())
# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, c)
#     else:
#         hanoi(n - 1, a, c, b)
#         print(a, c)
#         hanoi(n - 1, b, a, c)
# sum = 1
# for i in range(n - 1):
#     sum = sum * 2 + 1
# print(sum)
# hanoi(n, 1, 2, 3)

'''11단계 브루트 포스'''  #어려워서 패스
# # 2798 블랙잭
# N,M = map(int,input().split()) # 카드 개수, 지정 값
# K = list(map(int,input().split())) # 카드 숫자 N개 만큼
# result = 0
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1,N):
#             if K[i] + K[j] + K[k] > M:
#                 continue
#             else:
#                 result = max(result,K[i] + K[j] + K[k])
# print(result)

''' 12단계 정렬 '''

# # 2750 수 정렬하기
# N = int(input())           # 입력할 수 
# P = []       
# for i in range(N):
#     P.append(int(input())) # 정렬할 숫자
# P.sort()                   # 정렬
# for x in range(len(P)):    # list 수만큼 반복
#     print(P[x])

# # 2751 수 정렬하기2

# import sys
 
# num = int(sys.stdin.readline())
 
# num_list = []
 
# for i in range(num):
#     a = int(sys.stdin.readline())
#     num_list.append(a)
 
# num_list.sort()
 
# for i in num_list:
#     print(i)

# # 10989 수 정렬하기3
# N = int(input())           # 입력할 수 
# P = []       
# for i in range(N):
#     P.append(int(input())) # 정렬할 숫자
# P.sort()                   # 정렬
# for x in range(len(P)):    # list 수만큼 반복
#     print(P[x])

# # 2108 통계학
# import sys
# from collections import Counter

# N = int(sys.stdin.readline())
# K = []

# def sansul(K,N): # 산술 평균
#     result = round(sum(K)//N)
#     return result

# def jungang(K): # 중앙값
#     K.sort()
#     result = K[len(K)//2]
#     return result

# def choibin(K): # 최빈값
#     cnt_K = Counter(K).most_common()
#     if len(cnt_K) > 1 and cnt_K[0][1]==cnt_K[1][1]: #최빈값 2개 이상
#         return cnt_K[1][0]
#     else:
#         return cnt_K[0][0]

# def bumwee(K):
#     result = max(K)-min(K)
#     return result

# if N % 2 != 0: 
#         for x in range(N):
#             K.append(int(sys.stdin.readline()))

# print("산술 평균 :",sansul(K,N))
# print("중앙값 :", jungang(K))
# print("최빈값 :",choibin(K))
# print("범위 :", bumwee(K))

# # 1427 소트인사이드
# N = input()
# num = [int(n) for n in N] # 입력된 문자를 숫자로 리스트에 저장

# ordered_num = sorted(num, reverse=True) # 내림차순 정렬

# for n in ordered_num:
#     print(n,end="")

# # 11650 좌표 정렬하기
# import sys
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     so.append(list(map(int, sys.stdin.readline().split())))
# so.sort(key=lambda x: (x[0], x[1]))
# for i in so:
#     print(i[0], i[1])

# # 11651 좌표 정렬하기2
# import sys
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     so.append(list(map(int, sys.stdin.readline().split())))
# so.sort(key=lambda x: (x[1], x[0]))
# for i in so:
#     print(i[0], i[1])

# # 1181 단어 정렬
# import sys
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     so.append( sys.stdin.readline().strip())
# so.sort(key=len)

# for i in so:
#     print(i)

# # 10814 나이순 정렬
# import sys
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     age,name=map(str,input().split())
#     age = int(age)
#     so.append((age, name))
# so.sort(key=lambda so: (so[0]))
# for so in so:
#     print(so[0],so[1])

# # 18870 좌표 압축
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# arr2 = sorted(list(set(arr)))
# dic = {arr2[i] : i for i in range(len(arr2))}
# for i in arr:
#     print(dic[i], end = ' ')