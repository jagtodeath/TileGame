import Tkinter as tk
import itertools as IT
import collections
from time import sleep
from random import randint

cols, rows = 6,6

board = [[None] * cols for _ in range(rows)]
matrix = [[0 for i in range(rows)] for j in range(cols)]

score = 0
played = 0

n = 3

def empty():
    return [[0 for i in range(rows)] for j in range(cols)]

def generateBoard(n):
    for num in range(n):
        i = randint(0, 5)
        j = randint(0, 5)
        while (board[i][j]['bg'] != 'grey'):
            i = randint(0, 5)
            j = randint(0, 5)
        board[i][j]['bg'] = 'red'
        matrix[i][j] = 1

def clearBoard():
    for i,j in IT.product(range(rows),range(cols)):
        board[i][j]['bg'] = 'grey'

def game(event):
    global played, matrix
    played = 0
    matrix = empty()
    clearBoard()
    root.update_idletasks()
    sleep(0.5)
    generateBoard(n)
    root.update_idletasks()
    sleep(2)
    clearBoard()
    root.update_idletasks()


def on_click(event, i, j):
    if board[i][j]['bg'] == 'red': return
    global played, score, n
    if not matrix[i][j]:
        print 'fail'
        print 'Final Score =', score
        for i,j in IT.product(range(rows),range(cols)):
            if matrix[i][j]: board[i][j]['bg'] = 'blue'
        root.update_idletasks()
    else:
        board[i][j]['bg'] = 'red'
        root.update_idletasks()
        played += 1
        score += 1
        if played == n:
            print 'success'
            score += n
            n += 1
            print 'Score =', score
            sleep(1)

def begin(event = None):
    for i, j in IT.product(range(rows), range(cols)):
        board[i][j] = L = tk.Label(root, text='    ', bg='grey')
        L.grid(row=i, column=j, padx=3, pady=3)
        L.bind('<Button-1>', lambda e, i=i, j=j: on_click(e, i, j))

root = tk.Tk()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label='New Game',command=begin,accelerator = "Command-N")
menubar.add_cascade(label="File",menu = filemenu)
root.config(menu=menubar)
root.bind_all("<Command-n>", begin)
root.bind_all("<space>",game)
begin()
root.mainloop()
