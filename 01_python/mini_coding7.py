# while 1:
#
# 	a = int(input("몇 단을 출력하시겠습니까?"))
#
# 	if(a == int(a)):
# 		if(a == 0):
# 			print("0을 입력할 순 없습니다.")
# 		elif(a == 1):
# 			print("1을 입력할 순 없습니다.")
# 		else:
# 			for num in range(1,10):
# 				print("{} * {} = {}".format(a,num,a*num))
# 				break
# 	else:
# 		print("숫자만 입력해주세요.")


# 학습 답변

def gugudan():
	try:
		dan = int(input("2에서 9사이의 숫자를 입력해주세요."))

		for num in range(1,10):
			print("{} * {} = {}".format(dan, num, dan*num))
	except ValueError:
		# 현재 gugudan 함수는 인풋값을 받자마자 int로 변환한다. 여기서 이 값이 문자일경우
		# (숫자로된 문자열이 아닐경우) int에서 값의 에러가 발생한다. 이 에러가 발생했을 때
		# print로 에러메시지를 구체적으로 전달하고, gugudan() 함수를 다시 사용할수있도록
		# 예외처리를 하는 것이다.
		print("숫자만 입력해주세요.")
		gugudan()
	except:
		print("알 수 없는 엘가 발생 했습니다.")
		gugudan()

gugudan()
