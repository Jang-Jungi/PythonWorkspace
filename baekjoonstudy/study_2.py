''' 4단계 While 문 '''

# 10952 A+B-5
while(True):
    A,B = map(int, input().split())
    if A == 0 & B == 0:
        break
    print(A+B)
print("0이 입력되었으므로 프로그램 종료")

# 10952 A+B-4
while(True):
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        KeyboardInterrupt
        break

# 1110 더하기 사이클
N = int(input()) # 입력 값
check = N        # 검증 값
temp = 0         # 몫 + 나머지 더한 값
new_N = 0        # 일의 자리*10 + 나머지 값
count = 0        # 사이클 수
while True:
    temp = N//10 + N%10  
    new_N = (N%10)*10 + temp%10
    count += 1
    N = new_N
    if new_N == check: # 검증
        break
print(count)       # 출력

''' 5단계 1차원 배열 '''

# 10818 최소 최대
N = int(input()) # 입력 받을 정수 개수
Num = list(map(int, input().split()))
print("최대 :",max(Num),"최소 :", min(Num))

# 2562 최댓값
Num = list(map(int, input().split()))
k = max(Num)
print("최댓값 :",k)
for i in range(0,9):
    if Num[i] == k:
        print("최댓값의 위치는", i+1 ,"번.")
    i+=1

# 2577 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
Num = list(str(A*B*C))
for i in range(0,10): # 0~9까지 숫자 돌기
    print(str(i)+"은 " + str(Num.count(str(i)))+"번 사용")

# 3052 나머지
Num = set()          # 중복 제거 : set
for i in range(10):  # 10번 반복
    A = int(input()) # 입력
    B = A%42         # 나머지
    Num.add(B)       # 추가
print("서로 다른 나머지의 수는 :", len(Num)) # 리스트 개수

# 1546 나머지
N = int(input())                            # 시험 본 과목 개수
old_score = list(map(int, input().split())) # 변환 전 과목별 점수
max_score = max(old_score)                  # 변환 할 최대값 점수
new_score = 0                               # 변환 될 점수
avg = 0                                     # 평균값
for i in range(0,len(old_score)):           # 리스트 개수만큼 for문
    new_score = int(old_score[i])/max_score*100 # 변환 식
    avg += new_score                        # avg에 더함
print( avg / N )                            # 과목 수로 나눠줌

# 8958 OX 퀴즈
N = int(input())              # Case 수

for _ in range(N):            # Case 입력
    sum = 0                   # sum 
    count = 0                 # count 
    OX_answer = list(input()) # OX 리스트 입력
    for k in OX_answer:       # OX 리스트 검색
        if k == 'O':          # O 검색
            count+=1          # +1
            sum = sum+count   # sum에 추가
        else:              
            count=0           # X가 나오면 count 초기화
    print(sum)                # sum 출력

# 4344 평균은 넘겠지
C = int(input())                           # Case 수
for _ in range(C):                         # Case 입력
    nums = list(map(int, input().split())) # 학생 수, 점수를 동시에 입력받음
    avg = sum(nums[1:])/nums[0]            # num[1:]-> 점수 num[0]-> 학생 수 // 평균값을 구함
    cnt = 0
    for score in nums[1:]:                 # 평균 이상 점수 찾기
        if score > avg:
            cnt +=1                        # 평균 이상 학생을 카운트
    rate = cnt/nums[0] * 100               # 비율을 구함
    print(f'{rate:3f}%')                   # 소수점 3째자리까지 표현

''' 6단계 함수 '''
# 15596 정수 N개의 합
def solve(a):
    return sum(a)

# 4673 셀프 넘버

# list를 활용한 코드
numbers = list(range(1, 10001))     # 리스트 범위 설정
remove_list = []                    # 식제할 숫자 리스트
for num in numbers:                  
    for n in str(num):               
        num +=int(n)                # 생성자가 있는 숫자
    if num <= 10000:                # 10000보다 작거나 같을 때만
        remove_list.append(num)     # append 리스트에 요소 추가

for remove_num in set(remove_list): # set으로 중복값 제거
    numbers.remove(remove_num)      
for self_num in numbers:            # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)                 

# set을 사용한 코드
numbers = set(range(1, 10001))      # 범위 설정
remove_set = set()                  # 생성자가 있는 숫자 set
for num in numbers:
    for n in str(num):
        num += int(n)
    remove_set.add(num)             # add로 집합에 추가

self_numbers = numbers - remove_set # set의 - 연산자로 차집합을 구함
for self_num in sorted(self_numbers): # sorted로 정렬
    print(self_num)

# 1065 한수
num = int(input())
hansu = 0

for n in range(1, num+1):
    if n <= 99: # 1~99까지 모두 한수
        hansu += 1

    else:
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1]- nums[2]: # 등차수열 확인
            hansu+=1
print(hansu)

''' 7단계 문자열 '''

# 11654 아스키 코드
Ascii = str(input())   # input
print(ord(Ascii))      # ord string -> ascii 
print(chr(ord(Ascii))) # ascii -> string

#11720 숫자의 합
str = input()
sum = 0
for x in str:
    sum +=int(x)
print(sum)

n = int(input())
nums = input()
total = 0
for i in range(n) :  # 0부터 n-1까지
    total += int(nums[i])
print(total)

print(sum(map(int,input())))

# 10809 알파벳 찾기
S = str(input())
alphabet = list(range(97,123)) # a~z ascii numbers
for x in alphabet:
    print(S.find(chr(x)))

# 2675 문자열 반복
R = int(input())
for i in range(R):
    count, word = input().split()
    for x in word:
        print(x*int(count), end='') 
    print() 
        
# 1157 단어 공부
word = input().upper()
unique_words = list(set(word)) # 중복값 제거
count = 0
count_list = []
for x in unique_words:
    count = word.count(x)
    count_list.append(count)
if count_list.count(max(count_list))>1: # count 최대값이 여러개라면
    print('?')
else:
    max_index = count_list.index(max(count_list)) # count 최대값 숫자 index
    print(unique_words[max_index])

# 1152 단어의 개수
word = list(map(str,input().split()))
print("단어의 개수는",len(word))

# 2908 상수
num1, num2 = input().split()
num1 = int(num1[::-1]) # [::-1] 역순
num2 = int(num2[::-1])

if num1>num2:
    print(num1)
elif num1<num2:
    print(num2)
else :
    print("error")

# 5622 다이얼
dial_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input().upper()
time = 0
for unit in dial_list:  # 다이얼 리스트를 분리
    for i in unit:      # 알파벳 하나씩 분리
        for x in word:  # 입력한 문자를 한글자씩 분리
            if i ==x:   # 같으면
                time += dial_list.index(unit)+3 # index+3한 값을 더함
print(time)

# 2941 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i,'*') # input 변수와 동일한 이름의 변수
print(len(word))

# 1316 그룹 단어 체크
N = int(input())    # 반복 횟수
group_word = 0      # 그룹 단어 체크 숫자
for _ in range(N):  
    word = input()  # 입력값
    error = 0       # 에러 단어 체크 숫자
    for index in range(len(word)-1):          # index의 수는 length-1이다.
        if word[index] != word[index+1]:      # 특정 index의 값이 다음 문자와 다를 때
            new_word = word[index+1:]         # 다음 문자를 새로운 단어로 생성
            if new_word.count(word[index])>0: # 남은 문자열에 새로운 단어가 있다면
                error += 1                    # 에러 단어
    if error ==0:                             # 에러 단어가 없다면
        group_word += 1                       # 그룹 단어에 +1
print(group_word)                             # 그룹 단어 출력