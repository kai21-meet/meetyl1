users=[]
posts_list=[]

class User(object):
	def __init__ (self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friend_list=[]

	def add_friend(self, email):
		self.friend_list.append(email)
		print(self.name + " has added " + email + " as a friend")

	def remove_friend(self, email):
		self.friend_list.remove(email)
		print(self.name + " has removed " + email + " as a friend")
	
	def posting(self, text):
		post1=Post(0, text, self.email)
		posts_list.append(post1)
		print(self.name + " has posted " + text)

	def get_userInfo(self):
		print("Name:" + self.name)
		print("Email:" + self.email)
		print("Password:" + self.password)
		print("Friends:" +str(self.friend_list))


class Post():
	def __init__(self,text,likes,author):
		self.text=text
		self.likes=0
		self.comments=[]
		self.author=author

	def like_post (self, email):
		self.like=+1
		print(email+ " liked your post ")

	def comment_post(self, text):
		self.comments.append(text)
		print(email+ " commented your post " + text)

class Comment(Post):
	def __init__(self, like):
		self.like = 0
		self.reply=[]

	def like_comments(self, likes):
		self.like=+1
		print(email+ " liked your comment ")

	def reply_to(self, text):
		self.reply.append(text)
		print(email+ " replyed your comment " + text)


'''
user1 = User("kai","kai.assraf@gmail.com","kaiassraf123")
user2 = User("lani","lani.assraf@gmail.com","laniassraf123")
user1.add_friend('lani')
user1.posting("heyy how r u?")
user1.get_userInfo()
user1.remove_friend('lani')
'''

print("log in")
email=input('your email')	
password=input('your password')
for user in users():
	if email==self.email:
		if password==self.password:
			log_in=user

