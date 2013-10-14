import Tkinter as tk
import itertools as IT
import collections
from time import sleep

cols, rows = 7,7
board = [[None] * cols for _ in range(rows)]
computerBoard = [['grey'] * cols for _ in range(rows)]
computerDone = True

blueMoves = []
redMoves = []

#other = {'green': 'red', 'red': 'blue','blue' : 'black','black' : 'green'}
#other = {'blue':'red','red':'green','green':'blue'}

other = {'blue':'red','red':'blue'}
turns = 1
player = 'blue'

def on_click(event, i, j):
    if board[i][j]['bg'] != 'grey':
        print 'noooope'
        return
    global player, turns
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
    if turns%1 == 0:
        player = other[player]

def check_for_winner():
    s = score()
    if sum(s.values()) - s['grey']== cols*rows:
#         winner = max(s, key=s.get)
        for key in s:
            print 'Total {0}: {1}'.format(key, s[key])

def score():
    return collections.Counter(
        board[i][j]['bg'] for i, j in IT.product(range(rows), range(cols)))

def begin(event = None):
    global turns
    turns = 0
    for i, j in IT.product(range(rows), range(cols)):
        board[i][j] = L = tk.Label(root, text='    ', bg='grey')
        L.grid(row=i, column=j, padx=3, pady=3)
        L.bind('<Button-1>', lambda e, i=i, j=j: on_click(e, i, j))
    print player, 'goes first.'

root = tk.Tk()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label='New Game',command=begin,accelerator = "Command-N")
menubar.add_cascade(label="File",menu = filemenu)
root.config(menu=menubar)
root.bind_all("<Command-n>", begin)
begin()
root.mainloop()
