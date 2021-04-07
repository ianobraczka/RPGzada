from player import Player
from enemy import Enemy
import random

p1 = Player()
e1 = Enemy(p1.position_x, p1.position_y)

enemy_list = []
enemy_list.append(e1)

gameover = False
position_list = [["_", "_", "_","_", "_"], 
				["_", "_", "_", "_", "_"], 
				["_", "_", "_", "_", "_"], 
				["_", "_", "_", "_", "_"],
				["_", "_", "_", "_", "_"]]

def update_grid():
	global position_list
	position_list = [["_", "_", "_","_", "_"], 
				["_", "_", "_", "_", "_"], 
				["_", "_", "_", "_", "_"], 
				["_", "_", "_", "_", "_"],
				["_", "_", "_", "_", "_"]]

	position_list[p1.position_y][p1.position_x] = "0"
	
	for enemy in enemy_list:
		position_list[enemy.position_y][enemy.position_x] = "!"

def update_game():
	update_grid()
	kill_enemies()
	spawn_enemies()
	print_game()

def game():
	global position_list

	while(not gameover):

		# RODADA DO PLAYER
		while(p1.mana > 0):
			update_game()
			jogada = input('diga a sua jogada\n')
			p1.play(jogada, enemy_list)


		# RODADA DOS INIMIGOS
		update_game()
		for enemy in enemy_list:
			enemy.walk(p1.position_x, p1.position_y)

		p1.mana = 2

def kill_enemies():
	for enemy in enemy_list:
		if enemy.hp <= 0: 
			enemy_list.remove(enemy)


def print_game():
	for i in range(50):
		print("")
	print(position_list[0])
	print(position_list[1])
	print(position_list[2])
	print(position_list[3])
	print(position_list[4])
	print("")
	print("vida do player:", p1.hp, "HP")
	print("mana do player:", p1.mana)
	print("vida do inimigo:", enemy_list[0].hp, "HP")
	print("")

def spawn_enemies():
	global enemy_list
	global p1
	if len(enemy_list) == 0:
		enemy = Enemy(p1.position_x, p1.position_y)
		enemy_list.append(enemy)


update_grid()
print_game()
game()

# COMENTARIO TESTE DO GIT
#gluglu



