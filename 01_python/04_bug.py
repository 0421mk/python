# exceptions -> 파이썬은 버그대신 예외라고 한다.
# 즉, 예외처리는 버그와 동일하다.

# ZeroDivisionError : division by zero
# 1/0

# def divide_by(first, second):
# 	return first / second
#
# # 4 / 2 = 2
#
# print(divide_by(4,2))

#\ 사용자는 예상치 못한 에러를 일으킨다. 예외처리를 공부해보자.

def divide_by(first, second):
	try:
		return first / second
	#except:
	except ZeroDivisionError:
		return "0으로는 나눌 수 없습니다."

print(divide_by(4,2))
print(divide_by(4,0))

# 예외 만들기
# 파이썬에는 Exception 이라는 클래스가 있는데 DivisionError같은 것들이
# Exeception이라는 클래스를 상속을 받아 사용된다.
class EvenNumberDivisionError(Exception):
	pass
	# pass라는 것을 특정한 클래스나 def를 정의할 때 한줄의 메소드는 정의를 내려야 한다.
	# 예를 들어 print(), try:, return 등등 말이다. 하지만 굳이 안써도 돼는 상황이면 pass를 사용한다.

def divide_by_odd_number (first, second):
	if second % 2 == 0:
		# raise 는 일으키다 라는 명령어이다. 파이썬은 raise라는 명령어를 이용해
		# 오류를 강제로 발생시킬 수 있다.
		raise EvenNumberDivisionError
	else:
		return first / second

print(divide_by_odd_number(6,3))

# 밑줄을 실행하면 에러가 발생할 수 있다.
# print(divide_by_odd_number(6,2))
