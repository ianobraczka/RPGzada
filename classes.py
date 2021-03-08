class Player():

	def __init__(self):
		self.hp = 10
		self.cooldown = 0.5
		self.speed = 7
		self.damage = 5
		self.position_x = 2
		self.position_y = 2

	def walk(self, jogada):
		if jogada == 'w':
			self.position_y -= 1   # position_y = position_y - 1
		elif jogada == 's':
			self.position_y += 1
		elif jogada == 'd':
			self.position_x += 1
		elif jogada == 'a':
			self.position_x -= 1

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
		self.position_x = 0
		self.position_y = 4

	def walk(self, player_x, player_y):
		if self.position_x > player_x:
			self.position_x -= 1
		elif self.position_x < player_x:
			self.position_x += 1
		else:
			if self.position_y > player_y:
				self.position_y -= 1
			elif self.position_y < player_y:
				self.position_y += 1

	def hit(self):
		pass

	def die(self):
		pass


