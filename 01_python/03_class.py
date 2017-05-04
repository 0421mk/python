# 클래스 CLASS

# Article variables

title1 = "개발"
author1 = "yoonwoo"
content1 ="A"
view_count1 = 0

title2 = "코칭"
author2 = "yoonwoo"
content2 ="B"
view_count2 = 0

title3 = "창업"
author3 = "yoonwoo"
content3 ="C"
view_count3 = 0

# Article CLASS
#class Article:
#	title = "개발"
#	author = "yoonwoo"
#	content ="A"
#	view_count = 0

# 클래스 객체(인스턴스)를 만들다
#article1 = Article()
#
#print(article1.title)
#
#article2 = Article()
#article2.title = "코칭"
#
#print(article2.title)

# Article class with __init__

class Article:
	author = "마르코"
	view_count = 0

#init 과 self는 클래스안에 변수에 접근하기위해 사용하는 약속체계이다.
# 클래스안에 함수는 클래스 변수에 접근하기위해 반드시 파라미터에 self를 추가해야한다.
	def __init__(self, title, content):
		self.title = title
		self.content = content

	def read(self):
		self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

# print(article1.view_count)
# article1.read()
# print(article1.view_count)
# article2.read()
# article2.read()
# print(article2.view_count)

 # Article class inheitance 상속 (클래스가 중요한 진짜 이유)

# class BrunchArticle:
# 		author = "마르코"
# 		view_count = 0
#
# 	#init 과 self는 클래스안에 변수에 접근하기위해 사용하는 약속체계이다.
# 	# 클래스안에 함수는 클래스 변수에 접근하기위해 반드시 파라미터에 self를 추가해야한다.
# 		def __init__(self, title, content):
# 			self.title = title
# 			self.content = content
#
# 		def read(self):
# 			self.view_count = self.view_count + 1
# 	# 개발자들은 했던 일을 다시 하고싶지않아한다. 똑똑하고 게으른 개발자가 돼자.

class BrunchArticle(Article):
	source = "브런치"

	def read(self):
		self.view_count = self.view_count + 2
		# 오버라이드라고 한다. 부모 클래스의 함수를 상속받은 자식 클래스가 덮어 쓴다.

brunch_article = BrunchArticle("개발","개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
brunch_article.read()
brunch_article.read()
print(brunch_article.view_count)

# 이런식으로 클래스는 상속을 이용해서 이미 사용한 클래스를 굳이 다시
# 쓰지 않고도 간단하게 다시 재현할 수 있다. 상속을 받으려면 클래스 마라미터값에
# 부모클래스 네임을 넣어주면 됀다.
