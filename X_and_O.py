import string

board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

def display_board():
	print ("   0   1   2")
	print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
	print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
	print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
	print ("   6   7   8")

def handle_turn(player):
	if (player == 1):
		char = "O"
	else:
		char = "X"
	alert = "%s \n Choose a position to play in between 0 & 8: "
	player1 = "PLAYER 1's TURN AN \'O\' WILL BE PLACED"
	player2 = "PLAYER 2's TURN AN \'X\' WILL BE PLACED"
	try:
		if (player == 1):
			position = int(raw_input(alert%player1))
		else:
			position = int(raw_input(alert%player2))
	except:
		print("INVALID INPUT PLEASE RETRY PLEASE ENTER A NUMBER BETWEEN 0 & 8")
		return (-1)
	if (position < 0 or position > 8 or board[position] != "-"):
			print("INVALID INPUT PLEASE RETRY")
			return (-1)
	else:
		board[position] = char
	return (1)

def check_possible():
	i = 0
	cnt = 0
	while (i < 9):
		if (board[i] == "-"):
			cnt += 1
		i += 1
	return (cnt)

def check_diag(char):
	if (board[0] == char and board[4] == char and board[8] == char):
		return (1)
	if (board[2] == char and board[4] == char and board[6] == char):
		return (1)

def check_collum(char):
	if (board[0] == char and board[3] == char and board[6] == char):
		return (1)
	if (board[1] == char and board[4] == char and board[7] == char):
		return (1)
	if (board[2] == char and board[5] == char and board[8] == char):
		return (1)
	return (0)

def check_rows(char):
	if (board[0] == char and board[1] == char and board[2] == char):
		return (1)
	if (board[3] == char and board[4] == char and board[5] == char):
		return (1)
	if (board[6] == char and board[7] == char and board[8] == char):
		return (1)
	return (0)

def check_victor(player):
	char = 'O'
	if (player == 2):
		char = 'X'
	if (check_rows(char) == 1 or check_collum(char) == 1 or check_diag(char) == 1):
		display_board()
		print("The winner is " + char + "!")
		return (1)
	if (check_possible() == 0):
		display_board()
		print("The board is full, the game is a draw, game over.")
		return (1)
	return (0)

def play_game():
	player = 0
	print ("YOU ARE ABOUT TO PLAY NAUGHTS AND CROSSES, \n PRESS 'CTRL' + 'Z' TO EXIT AT ANY POINT")
	while (check_victor(player) == 0):
		player += 1
		if (player == 3):
			player = 1
		display_board()
		if (handle_turn(player) == -1):
			player -= 1

play_game()