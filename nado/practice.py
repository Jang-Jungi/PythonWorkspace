# 숫자형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+4)
print(5*4)
print(3*(3+1))

# 문자열
print('풍선')
print("풍선")
print("ㅋ"*9)

# boolean

print(5>20)
print(5<20)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>20))

# 변수

animal = "강아지"
name = "연탄"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal +"의 이름은 "+ name +"이다.")
print(name + "는" + str(age) +" 살이며," + hobby +"을 좋아한다.")
print(name + "이는 어른일까요?" + str(is_adult))

print("우리집" , animal ,"의 이름은 ", name,"이다.")
print(name, "는" ,age, "살이며," , hobby ,"을 좋아한다.")
print(name, "이는 어른일까요?" , is_adult)

# 주석
# 한 줄 주석
''' 여러줄 주석
'''
# 방법은 
# Ctrl+/

# 연산자
print(5//3) # 몫
print(5%3)  # 나머지
print(5/3)  # 나누기
print(3==3) # 같다
print(3+4==7) 
print(1 != 3) # 같지 않다
print(not(1!=3)) # 같지 않다
print((3>0) and (3<5))
print((3>0) and (3>5)) # &
print((3>0) or (3>5)) # |
