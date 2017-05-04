# import random
#
# count = 0
#
# while count < 3:
#
# 	val = input("가위(1), 바위(2), 보(3)중 하나를 선택하시오.")
#
# 	if(int(val) == 1):
# 		me = random.randrange(1,4)
# 		if(me == 1):
# 			print("draw")
# 			count = count+1
# 		if(me == 2):
# 			print("win")
# 			count = count+1
# 		if(me == 3):
# 			print("lose")
# 			count = count+1
#
# 	elif(int(val) == 2):
# 		me = random.randrange(1,4)
# 		if(me == 1):
# 			print("lose")
# 			count = count+1
# 		if(me == 2):
# 			print("draw")
# 			count = count+1
# 		if(me == 3):
# 			print("win")
# 			count = count+1
#
# 	elif(int(val) == 3):
# 		me = random.randrange(1,4)
# 		if(me == 1):
# 			print("win")
# 			count = count+1
# 		if(me == 2):
# 			print("lose")
# 			count = count+1
# 		if(me == 3):
# 			print("draw")
# 			count = count+1
#
# 	else:
# 		print("잘못 입력하셨습니다.")


# 강의 답변

import random

ROCK = "바위"
SCISSOR = "가위"
PAPER = "보"

RSP_LIST = (
	ROCK,
	SCISSOR,
	PAPER
)

win_count = 0
lose_count = 0

while win_count < 3 and lose_count < 3:

# 1) 사용자 입력
	user_choice = input("{}, {}, {} :".format(
		SCISSOR, ROCK, PAPER
	))
# 2) 컴퓨터 임의 선택
	computer_choice = random.choice(RSP_LIST)
# 3) 3번 지거나 이기면 승패 확정
	if user_choice == computer_choice:
		print("비겼습니다.")
	elif user_choice not in RSP_LIST:
		print("가위 바위 보 중 하나만 선택하세요.")
	elif (user_choice == ROCK and computer_choice == SCISSOR) or (user_choice == SCISSOR and computer_choice == PAPER) or (user_choice == PAPER and computer_choice == ROCK):
		win_count = win_count + 1
		print("이겼습니다.")
	else:
		lose_count = lose_count + 1
		print("졌습니다.")

if win_count == 3:
	print('사용자가 최종 승리하였습니다.')
else:
	print("컴퓨터가 최종 승리하였습니다.")
