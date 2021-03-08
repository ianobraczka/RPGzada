
class Player():

	def __init__(self):
		self.hp = 10
		self.cooldown = 0.5
		self.speed = 7
		self.damage = 5
		self.position_x = 2
		self.position_y = 2

	def walk(self):
		pass

	def hit(self):
		pass
	
	def block(self):
		pass

	def die(self):
		pass

	def spawn(self):
		pass





class Enemy:

	def __init__(self):
		self.hp = 4
		self.cooldown = 2
		self.speed = 3.5
		self.damage = 3


	def walk(self):
		pass

	def hit(self):
		pass

	def die(self):
		pass


