# class man:
# 	name = ""
# 	age = ""
# 	gender = ""
#
# class colleague(man):
# 	rank = "대리"
#
# name = input("이름을 입력하세요.")
# age = input("나이를 입력하세요.")
# gender = input("성별을 입력하세요.")
#
# man1 = man()
#
# man1.name = name
# man1.age = age
# man1.gender = gender
#
# print(man1.name)
# print(man1.age)
# print(man1.gender)

# 강의 답변

# 1 ) 사람 클래스

class Person:

# 이름, 나이, 성별
# 1-1 ) 새로 만들 때 입력

	def __init__(self, name,age,gender):
		self.name = name
		self.age = age
		self.gender = gender

# 2 ) 직장 동료 클래스

class Colleague(Person):

# 상속
# 2-1 ) 기본 직급 대리로

# 2-2 ) 새로 만들 때 입력하자.
	def __init__(self, name, age, gender, position):
		super().__init__(name, age, gender)
		# super().__init__(name, age, gender) 가 없으면 position만 출력됨
		# 부모클래스의 함수를 그대로 가져와야함. 그때 super() 사용함
		#super는 부모 클래스가 가지고 있는 함수를 호출, 혹은 변수를 호출하는 역할을 한다.
		# colleague 안에서 perosn의 init을 호출한다.
		self.position = position

colleague = Colleague("Marco",20,"male","boss")
# print(colleague.name)
print(colleague.__dict__)
# __dict__는 클래스를 딕셔너리 형태로 보여준다 {'name' : 'Marco'} 이런식으로
