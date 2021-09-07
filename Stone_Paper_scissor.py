import random
import time


def nTimes():
	print('How many times you want to play?')
	xTimes = int(input())
	return xTimes

def selectPlayerMove():
	playerMove = ''
	while not (playerMove == 'S' or playerMove == 'X' or playerMove == 'P'):
		print('Please Press S-Stone P-Paper X-Scissor')
		playerMove = input().upper()

	if (playerMove == 'S'):
		playerMove = 'Stone'
	elif (playerMove == 'X'):
		playerMove = 'Scissor'
	else:
		playerMove = 'Paper'
	return playerMove



def computerMove():
	moveList = ['Scissor', 'Paper', 'Scissor']
	computerMove = random.choice(moveList)
	return computerMove



def whoWon(pMove, cMove):


	if (pMove == cMove):
		return "It's a draw"

	elif (pMove == 'Stone' and cMove == 'Paper'):
		return "Computer Won! 'Paper Wraps Stone'"

	elif (pMove == 'Paper' and cMove == 'Stone'):

		return "You Won! 'Paper Wraps Stone'"
	
	elif (pMove == 'Stone' and cMove == 'Scissor'):

		return "You Won! 'Stone breaks Scissor'"

	elif (pMove == 'Scissor' and cMove == 'Stone'):

		return "Computer Won! 'Stone breaks Scissor'"

	elif (pMove == 'Scissor' and cMove == 'Paper'):
		return "You won! Scissor Cuts Paper"

	elif (pMove == 'Paper' and cMove == 'Scissor'):
		
		return "Computer won! Scissor Cuts Paper"

	else:
		return "invalid move"


while True:

	print('STONE-PAPER-SCISSOR')
	print('Please Enter Your Name')
	playerName = input()
	print('Welcome ' + playerName + ' in STONE-PAPER-SCISSOR game!')

	playNTimes = nTimes()
	c_won = ''
	p_won = ''

	for x in range(playNTimes):
		print('Round ' + str(x+1))
		pMove = selectPlayerMove()
		cMove = computerMove()

		if (pMove == 'Stone' or pMove == 'Paper' or pMove == 'Scissor'):

			print('Your Move:- ' + pMove)
			#print('1')
			time.sleep(2)
			#print('2')
			#time.sleep(1)
			#print('3')
			#time.sleep(1)
			print('Computer Move:- ' + cMove)
			time.sleep(1)
			winner = whoWon(pMove,cMove)
			print(winner)

			
			#print('Score:- Computer ' + str(c_won) + ' ,' + ' Player ' + str(p_won) )

	print('Do you want to play again (yes|no)')
	if not input().lower().startswith('y'):
		break



