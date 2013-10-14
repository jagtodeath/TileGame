import Tkinter as tk
import itertools as IT
import collections
import copy
from random import choice

cols, rows = 6, 6
board = [[None] * cols for _ in range(rows)]
computerBoard = [['grey'] * cols for _ in range(rows)]
computerDone = True
bluePermanents = set()
redPermanents = set()

other = {'blue':'red','red':'blue'}
turns = 0
player = 'blue'

def on_click(event, i, j):
    if board[i][j]['bg'] != 'grey':
        return
    global player, turns, bluePermaments, redPermanents
    print player, cols*i + j + 1, '({0},{1})'.format(i+1,j+1)
    board[i][j]['bg'] = player
    computerBoard[i][j] = player
    for ii, jj in IT.product(range(i - 1, i + 2), range(j - 1, j + 2)):
        if ii<0 or ii>=rows or jj<0 or jj>=cols: continue
        neighbor = board[ii][jj]
        if neighbor['bg'] != 'grey' and (ii, jj) != (i, j):
            neighbor['bg'] = player
            computerBoard[ii][jj] = player
    check_for_winner()
    turns += 1
    for i,j in IT.product(range(rows),range(cols)):
        if isPermanent(i,j):
            if board[i][j]['bg'] == 'blue':
                if (i,j) not in bluePermanents:
                    bluePermanents.add((i,j))
            elif (i,j) not in redPermanents:
                redPermanents.add((i,j))
    if turns%2 == 0:
        player = other[player]
    if player == 'red' and computerDone:
        root.after(300,computerPlay)

def scored():
    return collections.Counter(
        board[i][j]['bg'] for i, j in IT.product(range(rows), range(cols)))

def check_for_winner():
    s = scored()
    if sum(s.values()) - s['grey']== cols*rows:
        for key in s:
            print 'Total {0}: {1}'.format(key, s[key])

def begin(event = None):
    global turns, board, computerBoard, player, redPermanents, bluePermanents
    bluePermanents = set()
    redPermanents = set()
    turns = 0
    player = choice(['red','blue'])
    for i, j in IT.product(range(rows), range(cols)):
        board[i][j] = L = tk.Label(root, text='    ', bg='grey')
        L.grid(row=i, column=j, padx=3, pady=3)
        L.bind('<Button-1>', lambda e, i=i, j=j: on_click(e, i, j))
    computerBoard = [['grey'] * cols for _ in range(rows)]
    print player, 'goes first.'
    if player == 'red':
        computerPlay()
        
def computerPlay():
    global computerBoard, computerDone, secondTime
    if scored()['grey'] == 1:
        for i,lst in enumerate(computerBoard):
            for j, bg in enumerate(lst):
                if bg == 'grey':
                    index = (i,j)
        on_click(None,index[0],index[1])
        return
    computerDone = False
    positionScore = [(0,0),(0,0),0]
    oldBoard = copy.deepcopy(computerBoard)
    for ii, jj in IT.product(range(0,rows), range(0,cols)):
        score = 0
        if computerBoard[ii][jj] == 'grey':
            move1 = (ii,jj)
            computerTestMove(ii,jj)
            oldBoard2 = copy.deepcopy(computerBoard)
            for iii, jjj in IT.product(range(0,rows), range(0,cols)):
                computerBoard = copy.deepcopy(oldBoard2)
                if computerBoard[iii][jjj] == 'grey':
                    move2 = (iii,jjj)
                    if move2 == move1: continue
                    computerTestMove(iii,jjj)
                    score = max(scoreSquare(move1,move2),scoreSquare(move2,move1))
                    if score > positionScore[2]:
                        positionScore = [move1,move2,score]
        computerBoard = copy.deepcopy(oldBoard)
    computerBoard = copy.deepcopy(oldBoard)
    on_click(None,positionScore[0][0],positionScore[0][1])
    computerDone = True
    on_click(None,positionScore[1][0],positionScore[1][1])
                
def scoreSquare(move1,move2):
    score = 0
    checked = []
    for i,j in IT.product(range(rows),range(cols)):
        if (i,j) not in bluePermanents and (i,j) not in redPermanents and isPermanent(i,j):
            if computerBoard[i][j] == 'red':
                score += 15
            if computerBoard[i][j] == 'blue':
                score -= 10
    for ii, jj in IT.product(range(move1[0] - 1, move1[0] + 2), range(move1[1] - 1, move1[1] + 2)):
        if ii != move1[0] or jj != move1[1]:
            score += scoreMetric(ii,jj)
            checked.append((ii,jj))
    for ii, jj in IT.product(range(move2[0] - 1, move2[0] + 2), range(move2[1] - 1, move2[1] + 2)):
        if ii != move2[0] or jj != move2[1]:
            score += scoreMetric(ii,jj)
    return score

def scoreMetric(i,j):
    global turns
    if i<0 or i>=rows or j<0 or j>=cols: #bordering an edge
        return 1.5
    if computerBoard[i][j] == 'grey': #bordering a grey tile
        if turns < 1:
            return 0
        return -2
    if board[i][j]['bg'] != player and board[i][j]['bg'] != 'grey':
        return 8
    if computerBoard[i][j] == player:
#         if isPermanent(i,j):
#             return 2
#         return 3
        return 5
    return 0
 
def isPermanent(i,j):
    for ii, jj in IT.product(range(i - 1, i + 2), range(j - 1, j + 2)):
        if ii<0 or ii>=rows or jj<0 or jj>=cols: continue
        if computerBoard[ii][jj] == 'grey':
            return False
    return True       

def computerTestMove(i, j):
    global computerBoard
    computerBoard[i][j] = player
    for ii, jj in IT.product(range(i - 1, i + 2), range(j - 1, j + 2)):
        if ii<0 or ii>=rows or jj<0 or jj>=cols: continue
        neighbor = computerBoard[ii][jj]
        if neighbor != 'grey' and (ii, jj) != (i, j):
            computerBoard[ii][jj] = player

root = tk.Tk()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label='New Game',command=begin,accelerator = "Command-N")
menubar.add_cascade(label="File",menu = filemenu)
root.config(menu=menubar)
root.bind_all("<Command-n>", begin)
begin()
root.mainloop()
