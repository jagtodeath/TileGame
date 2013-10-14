"""
Rules:
	Number of moves per turn
	Number of players
	Toggle swap corners
	Chain flipping:
		All non corner connected tiles of opponent are flipped
	Inverse placement:
		Placing a tile puts it as the opponent color but flips all
		surrounding opponent tiles to your color
	Edge hopping: placing a tile flips the bording tiles on the opposite edge

	Ways to win:
		Most tiles
		Least tiles

"""
cols, rows = 7, 7

board = [[None] * cols for _ in range(rows)]

playerOneScore = 0
playerTwoScore = 0

class Button():
	def __init__(self,i,j):
		self.color = 'grey'
		self.i = i
		self.j = j

	def click(i,j,rule = 'default'):
		if rule == 'default':
			curButton = board[i][j]
			if curButton.color != 'grey':
				print 'Choose and empyt space'
				return

for i in range(cols):
	for j in range(rows):
		board[i][j] = Button(i,j)

"""
Remember matrix - increasingly more to remember each round
Touch speed - increasingly fast squares come up until there are 4? at same time. tap to flip
Count - count the number of flipped tiles

Verses - Tile game 1v1 

Least flips - flip all tiles in least number of moves

Chain flips:
	Remembers every space you have moved
	Each time you choose a spacs:
		Flips all adjacent pieces to your color
		Swaps with previous move and swaps all to opponents color
		Swaps the move previous to that and swaps all to your color
		Continues chaining back to first move alternating which colors it flips every time

Game of life predicitions:
	Random selection of tiles shown in blue
	Predict the next generation according to game of life rules

	Punch in tiles and watch game of life take place
	Change game of life rules and watch what happens





"""







