import random

class Enemy:

	def __init__(self, player_x, player_y):
		self.hp = 4
		self.cooldown = 2
		self.speed = 1
		self.damage = 3
		self.position_x = random.randint(0,4)
		self.position_y = random.randint(0,4)
		if self.position_x == player_x and self.position_y == player_y:
			self.position_x = random.randint(0,4)
			self.position_y = random.randint(0,4)

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