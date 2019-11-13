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
	
	def post(self, text):
		self.posts.append(text)
		print(self.name + " has posted " + text)

	def get_userInfo(self):
		print ("Name:" + [self.name] / "Email:" + [self.email] / "Password:" + [self.password] / "Friends:" +str[self.friends_list] / "Posts:" + str[self.posts])

user1 = user("kai","kai.assraf@gmail.com","kaiassraf123")
user2 = user("lani","lani.assraf@gmail.com","laniassraf123")
user1.add_friend('lani')
user1.post("heyy how r u?")
