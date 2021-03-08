from classes import Player
from classes import Enemy

p1 = Player()
e1 = Enemy()

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
	while(not gameover):

		update_grid()
		print_grid()

		jogada = input('diga a sua jogada\n')

		p1.walk(jogada)
		e1.walk(p1.position_x, p1.position_y)


def print_grid():
	print(position_list[0])
	print(position_list[1])
	print(position_list[2])
	print(position_list[3])
	print(position_list[4])

game()

# COMENTARIO TESTE DO GIT
#gluglu