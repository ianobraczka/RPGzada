from classes import Player
from classes import Enemy

p1 = Player()
e1 = Enemy()

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
	position_list[e1.position_y][e1.position_x] = "!"		

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

		for enemy in enemy_list:
			enemy.walk(p1.position_x, p1.position_y)


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
	print("")

game()

# COMENTARIO TESTE DO GIT
#gluglu