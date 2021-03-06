from player import Player
from enemy import Enemy
from enemy import Elf
from enemy import Orc
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

	position_list[p1.position_y][p1.position_x] = "웃"
	
	for enemy in enemy_list:
		position_list[enemy.position_y][enemy.position_x] = enemy.symbol

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
			enemy.play(p1.position_x, p1.position_y, p1)	

		update_game()

		gameover_check()
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
	print("vida do player:", p1.hp*"♥ ")
	print("mana do player:", p1.mana*"✰ ")
	print("vida do inimigo:", enemy_list[0].hp, "HP")
	print("")

def spawn_enemies():
	global enemy_list
	global p1
	if len(enemy_list) == 0:
		choice = random.randint(1,2)
		if choice == 1:
			enemy = Elf(p1.position_x, p1.position_y)
		elif choice == 2:
			enemy = Orc(p1.position_x, p1.position_y)

		enemy_list.append(enemy)

def gameover_check():
	global p1
	global gameover
	if p1.hp <= 0:
		gameover = True
		coin = input("gameover insert a coin to continue . . .\n")
		if coin == "coin":
			gameover = False
			reset()

def reset():
	global p1
	global e1
	global enemy_list

	p1 = Player()
	e1 = Enemy(p1.position_x, p1.position_y)

	enemy_list = []
	enemy_list.append(e1)


update_grid()
print_game()
game()

# COMENTARIO TESTE DO GIT
#gluglu



