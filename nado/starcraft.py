''' 스타크래프트 프로젝트 전반전 '''
from math import e
from random import *

class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    def move(self,location):
        print("[지상 유닛 이동]", end=" ")
        print(f"{self.name} : {location}방향으로 이동합니다. [속도 {self.speed}]")

    def damaged (self,damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp<=0:
            print(f"{self.name} : 파괴되었습니다.")

class AttackUnit(Unit): # name,hp는 중복되기 때문에 Unit에서 상속
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) # 이렇게 하면 가져올 수 있다.
        self.damage = damage
    
    def attack(self,location): # 메소드 앞에는 무조건 self가 들어간다.
        print(f"{self.name} : {location}방향으로 적군을 공격합니다.[공격력 {self.damage}]")
        # location은 전달받은 값을 출력



class AttackUnit(Unit): # name,hp는 중복되기 때문에 Unit에서 상속
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) # 이렇게 하면 가져올 수 있다.
        self.damage = damage

    def attack(self,location): # 메소드 앞에는 무조건 self가 들어간다.
        print(f"{self.name} : {location}방향으로 적군을 공격합니다.[공격력 {self.damage}]")
        # location은 전달받은 값을 출력

# 마린
class Marrine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    
    # 스팀팩
    def stimpack(self):
        if self.hp>10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다.(HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 사용 불가")

class Tank(AttackUnit):
    seize_developed = False # 초기 시즈모드 개발값

    def __init__(self):
        AttackUnit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False
    # 시즈모드
    def set_seize_mode(self):
        if Tank.seize_developed ==False:
            return
        # 시즈모드 X-> 시즈모드
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *=2
            self.seize_mode == True
        # 시즈모드 -> 시즈모드 X
        else:
            print(f"{self.name} : 시즈모드 해제합니다.")
            self.damage /=2
            self.seize_mode == False

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도{self.flying_speed}]")
    
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable): # 공중 유닛, 공격 가능 다중 상속
    def __init__(self, name, hp, damage, flying_speed): # 초기화
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,flying_speed)
    
    def move(self,location):
        print("[공중 유닛 이동]", end=" ")
        print(f"{self.name} : {location}방향으로 이동합니다. [속도 {self.flying_speed}]")
    

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스", 80, 20,5)
        self.clocked = False # 클로킹 모드

    def clocking(self):
        # 클로킹X -> 클로킹
        if self.clocked == False:
            print(f"{self.name} : 클로킹 모드 설정합니다.")
            self.clocked = True
        # 클로킹 -> 클로킹X
        else:
            print(f"{self.name} : 클로킹 모드 해제합니다.")
            self.clocked = False
        
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] has left the game")


# 게임 진행
game_start() # 시작

# 마린 3기
m1 = Marrine()
m2 = Marrine()
m3 = Marrine()

# 탱크 2기
t1 = Tank()
t2 = Tank()

# 레이스 1기
w1 = Wraith()

# 유닛 일괄 관리 ( 생성된 모든 유닛을 list에 append )
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시") # 레이스는 공중 이동인데? fly?

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린:스팀팩, 탱크:시즈모드, 레이스:클로킹)
for unit in attack_units:
    if isinstance(unit, Marrine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격을 5~20까지 랜덤으로 받음

# gg
game_over()