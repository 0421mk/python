def hello_friends(name):
	print("Hi, {}".format(name))

name1 = "marco"
name2 = "john"
name3 = "jane"
name4 = "tom"

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)

#return할 수 있다는 뜻은 변수에 담을 수 있다는 뜻이다.

#함수의 4가지 특징
# 1 ) 입력값 O , 반환값 O
def sum_result(a , b):
	return int(a+b)

sum_result(1,2)

# 2 ) 입력값 O , 반환값 X
def print_function(name):
	print("hello, {}".format(name))

print_function("wolrd")

# 3 ) 입력값 X , 반환값 O
def return1():
	return 1

return1()

# 4 ) 입력값 X , 반환값 X
def returnX():
	print("X")

returnX()
