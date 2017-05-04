# 정수로 받아오는 input, 문자열로 받아오는 raw_input

# input에 문자열을 입력하면 변수로 인식한다.
# test = 'hello'
# val = input("입력 : ")
# 입력 : test
# 'hello'

# 입력받을때 원하는 값으로 항상 치환을 해줘야한다. -> type 변경이 필수적으로 필요하다.
val1 = input("입력 : ")

print(type(int(val1)))
