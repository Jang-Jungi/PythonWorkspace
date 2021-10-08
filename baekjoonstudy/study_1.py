''' 1단계 사칙연산 '''
print("Hello World")
print("강한친구 대한육군")
print("강한친구 대한육군")
a,b = 1,2
print(a+b)
c,d = 3,2
print(c-d)
print(a*b)
print(a/c)
e,f = 7,3
print(e+f)
print(e-f)
print(e*f)
print(e/f)
print(e%f)
print(e//f)

A,B,C = 5,8,4
print((A+B)%C)
print((A%C+(B+C)%C))
print((A*B)%C)
print((A%C)*(B%C)%C)

print("-------")
D = 472
E = '385'
print(D*int(E[2]))
print(D*int(E[1]))
print(D*int(E[0]))
print(D*int(E))

''' 2단계 if문 '''

# 1330 문제
a,b = 2,1
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')
# 3항 연산자
print('>') if a>b else print('<') if a<b else print('==')

# 9498 문제
input=100
print('A') if input>=90 else print('B') if(80<=input<90) else print('C') if(70<=input<80) else print('D') if(60<=input<70) else print('E')

# 2753 문제
year = 2000
if ((year%4 == 0) & (year%100 != 0)) | (year%400 == 0):
    print('1')
else:
    print('0')

# 14681 문제
x = 12
y = 5
print('1사분면')if(x>0 and y>0) else print('2사분면')if(x<0 and y>0) else print('3사분면')if(x<0 and y<0)else print('4사분면')if(x>0 and y<0)else print('예외')

# 2884 문제
H,M = 10,10

if M>45:
    print(H,M-45)
elif H >1 and M<45:
    print(H-1, M+15)
else:
    print(23,M+15)

''' 3단계 for문 '''

# 2739 구구단
N = int(input())
for i in range(1,10):
    print(N, "*",i,"=", N*(i))

# 10950 A+B-3
t = int(input())  # 테스트 케이스 개수 t를 입력받음

for _ in range(t):  # t 만큼 반복
    a,b = map(int,input().split())
    print(a+b)

# 8393 합
n = int(input())
sum = 0
for i in range(n+1):
    sum = sum+i
print(sum)

# 15552 빠른 A+B
import sys  # sys모듈 읽어들이기

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)

# 2741 N 찍기
k = int(input())

for i in range(1,k+1):
    print(i)

# 2742 기찍 N
k = int(input())
# 시작값,최종값,증감값
for i in range(k,0,-1):
    print(i)

# 11021 A+B -7
T = int(input())
for x in range(1,T+1):
    a,b = map(int, input().split())
    print("Case #",x,":", a+b)

# 11021 A+B -7
T = int(input())
for x in range(1,T+1):
    a,b = map(int, input().split())
    print("Case #",x,":", a,"+",b,"=", a+b)

# 2438 별 찍기 1
T = int(input())
for x in range(1,T+1):
    print("*"*x)

# 2439 별찍기 2
T = int(input())
for x in range(T-1,-1,-1):
    print(" "*x+"*"*(T-x))

# 10871 X보다 작은 수
N,X = map(int,input().split())
num = list(map(int,input().split()))
for x in range(N):
    if num[x] < X:
        print(num[x], end = " ")
