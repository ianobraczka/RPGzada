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

	position_list[p1.position_y][p1.position_x] = "@"		

def game():
	while(not gameover):

		update_grid()
		print_grid()

		jogada = input('diga a sua jogada\n')

		if jogada == 'w':
			p1.position_y -= 1   # position_y = position_y - 1
		elif jogada == 's':
			p1.position_y += 1
		elif jogada == 'd':
			p1.position_x += 1
		elif jogada == 'a':
			p1.position_x -:= 1


def print_grid():
	print(position_list[0])
	print(position_list[1])
	print(position_list[2])
	print(position_list[3])
	print(position_list[4])

game()

# COMENTARIO TESTE DO GIT