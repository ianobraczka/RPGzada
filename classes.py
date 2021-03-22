class Player():

	def __init__(self):
		self.hp = 10
		self.cooldown = 0.5
		self.speed = 2
		self.damage = 5
		self.position_x = 2
		self.position_y = 2

	def play(self, jogada, position_list):
		if jogada == 'w' or jogada == 's' or jogada == 'd' or jogada == 'a':
			self.walk(jogada, position_list)
			return True
		elif jogada == 'i' or jogada == 'k' or jogada == 'j' or jogada == 'l':
			self.hit(jogada, position_list)
			return True
		else:
			return False

	def walk(self, jogada, position_list):
		if jogada == 'w':
			if position_list[self.position_y-1][self.position_x] == "!":
				pass
			elif self.position_y == 0:
				self.position_y = 4
			else:
				self.position_y -= 1
		elif jogada == 's':
			if position_list[self.position_y+1][self.position_x] == "!":
				pass
			elif self.position_y == 4:
				self.position_y = 0
			else:
				self.position_y += 1
		elif jogada == 'd':
			if position_list[self.position_y][self.position_x+1] == "!":
				pass
			elif self.position_x == 4:
				self.position_x = 0
			else:
				self.position_x += 1
		elif jogada == 'a':
			if position_list[self.position_y][self.position_x-1] == "!":
				pass
			elif self.position_x == 0:
				self.position_x = 4
			else:
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
		self.speed = 1
		self.damage = 3
		self.position_x = 0
		self.position_y = 4

	def walk(self, player_x, player_y):
		if self.position_x > player_x:
			if self.position_x-1 == player_x and self.position_y == player_y:
				pass
			else:
				self.position_x -= 1
		elif self.position_x < player_x:
			if self.position_x+1 == player_x and self.position_y == player_y:
				pass
			else:
				self.position_x += 1
		else:
			if self.position_y > player_y:
				if self.position_x == player_x and self.position_y-1 == player_y:
					pass
				else:
					self.position_y -= 1
			elif self.position_y < player_y:
				if self.position_x == player_x and self.position_y+1 == player_y:
					pass
				else:
					self.position_y += 1

	def hit(self):
		pass

	def die(self):
		pass


