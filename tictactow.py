from random import randrange
import time

board=[[1,2,3],[4,5,6],[7,8,9]]


def rows():
    for i in range (0,3):
        print("+-------", sep="", end="")
    print("+",sep="",end="")

def body():
    print("\n")
    for i in range(0,3):
        print("|       ",sep="",end="")
    print("|\n")


def display_board(board):
    rows()
    for i in range(0,3):
        body()
        print("|",end="")
        for j in range(0,3):
            print("   ",board[i][j],"   |", sep="",end="")
        body()
        rows()
    print("\n")

def enter_move(board):
    counter=0
    print("please enter a move by choosing a number!     ",end="")
    while(True):
        number=int(input())
        number-=1
        x=number//3
        y=number%3
        if (number>9) or (number< 1):
            print("\n***you have enterd an ivalid number.***\n")
        while((board[x][y] == "O") or (board[x][y] == "X")):
        	number=int(input("slot already taken, try again.   "))
        	number-=1
        	x=number//3
        	y=number%3
        board[x][y]="O"
        display_board(board)
        break

def pc_move(board):
    while(True):
    	x=randrange(0,3)
    	y=randrange(0,3)
    	while((board[x][y] == "O") or (board[x][y] == "X")):
    		x=randrange(0,2)
    		y=randrange(0,2)
    	board[x][y]="X"
    	display_board(board)
    	break


def victory(board):
	### checking row
	for i in range(0,3):
		if(board[i]==["X","X","X"]): 
			print("                       ding ding dig! X won!")
			return 1
		elif(board[i]==['O','O','O']): 
			print("                       ding ding dig! O won!")
			return 1
	#### checking cross
	if(board[0][0] == board[1][1] and board[1][1] == board [2][2]):
		if(board[0][0]=="X"): 
			print("                       ding ding dig! X won!")
			return 1
		else: 
			print("                       ding ding dig! X won!")
			return 1
	if(board[0][2] == board[1][1] and board[1][1] == board [2][0]):
		if(board[1][1]=="X"): 
			print("                       ding ding dig! X won!")
			return 1
		else: 
			print("                       ding ding dig! O won!")
			return 1
	###checking column
	if(board[0][0]==board[1][0] and board[1][0]==board[2][0] or board[0][1]==board[1][1] and board[1][1]==board[2][1] or board[0][2]==board[1][2] and board[1][2]==board[2][2]):
		if(board[0][0] == "X" or board[0][1] == "X" or board[0][2] == "X"):
			print("                       ding ding dig! X won!")
			return 1
		else:
			("                       ding ding dig! O won!")
			return 1

	return 0

    
display_board(board)
print("hello! welcome to my Tic-Tac-Toe game. You will be playing as O against a pc playing as X. Let's begin!\n")
time.sleep(3)
pc_move(board)
print("looks like your opponent made the first move!")
time.sleep(2)

while(True):
	enter_move(board)
	if(victory(board)): break
	print("nice move! now its your opponent's turn!\n")
	time.sleep(2)
	pc_move(board)
	if(victory(board)): break
	time.sleep(1)
input()