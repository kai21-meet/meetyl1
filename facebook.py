class user(object):
	def __init__ (self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friend_list=[]
		self.posts=[]
	def add_friend(self, email):
		self.friend_list.append(email)
		print(self.name + " has added " + email + " as a friend")

	def remove_friend(self, email):
		self.friend_list.remove(email)
		print(self.name + " has removed " + email + " as a friend")
	
	def posting(self, post_text):
		self.post_text = post_text
		post1=Post(post_text)
		self.posts.append(post1)
		print(self.name + " has posted " + post_text)

	def get_userInfo(self):
		print("Name:" + self.name)
		print("Email:" + self.email)
		print("Password:" + self.password)sers=[]

		print("Friends:" +str(self.friend_list))
		print("Posts:" + str(self.posts))


class Post():
	def __init__(self,post_text):
		self.comments = []
		self.post_text = post_text


user1 = user("kai","kai.assraf@gmail.com","kaiassraf123")
user2 = user("lani","lani.assraf@gmail.com","laniassraf123")
user1.add_friend('lani')
user1.posting("heyy how r u?")
user1.get_userInfo()
user1.remove_friend('lani')




		