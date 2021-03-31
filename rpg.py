from classes import Player
from classes import Enemy

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

def game():
	global position_list
	while(not gameover):

		update_grid()
		print_game()

		jogada = input('diga a sua 1ª jogada\n')
		if p1.play(jogada, enemy_list):
			pass
		else:
			print("jogada inválida")

		jogada = input('diga a sua 2ª jogada\n')
		if p1.play(jogada, enemy_list):
			pass
		else:
			print("jogada inválida")

		kill_enemies()
		spawn_enemies()

		for enemy in enemy_list:
			enemy.walk(p1.position_x, p1.position_y)

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
	print("vida do inimigo:", enemy_list[0].hp, "HP")
	print("")

def spawn_enemies():
	global enemy_list
	global p1
	if len(enemy_list) == 0:
		enemy = Enemy(p1.position_x, p1.position_y)
		enemy_list.append(enemy)


game()

# COMENTARIO TESTE DO GIT
#gluglu



