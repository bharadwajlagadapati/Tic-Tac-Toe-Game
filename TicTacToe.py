import tkinter as tk
from tkinter import messagebox,simpledialog
PLAYER='X'
COMP='O'
def initialize():
    global board
    board=[[' ' for _ in range(3)]for _ in range(3)]
    for i in range(3):
        for j in range(3):
            button[i][j].config(text=" ",state=tk.NORMAL,background='yellow')

def check_win(board,player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)):
            return True
    for j in range(3):
        if all(board[i][j]==player for i in range(3)):
            return True
    if all(board[i][i]==player for i in range(3)) or all(board[i][2-i]==player for i in range(3)):
        return True
    return False

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                return False
    return True

def minimax(board,depth,is_maxi,alpha,beta):
    if check_win(board,PLAYER):
        return -10+depth
    elif check_win(board,COMP):
        return 10-depth
    elif is_board_full(board):
        return 0
    if is_maxi:
        best_score=-float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]=COMP
                    score=minimax(board,depth+1,False,alpha,beta)
                    board[i][j]=' '
                    best_score=max(best_score,score)
                    alpha=max(alpha,best_score)
                    if beta<=alpha:
                        return best_score
    else:
        best_score=float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]=PLAYER
                    score=minimax(board,depth+1,True,alpha,beta)
                    board[i][j]=' '
                    best_score=min(best_score,score)
                    beta=min(beta,best_score)
                    if beta<=alpha:
                        return best_score
    return best_score
def get_optimal_move(board):
    best_score=-float('inf')
    best_move=(0,0)
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]=COMP
                score=minimax(board,0,False,-float('inf'),float('inf'))
                board[i][j]=' '
                if score>best_score:
                    best_score=score
                    best_move=(i,j)
    return best_move

def button_click(row,col,who):
    global board
    global PLAYER
    global COMP
    if board[row][col]==' ':
        button[row][col].config(text=PLAYER,state=tk.DISABLED,font=('Arial',9,'bold'),background='pink')
        board[row][col]=PLAYER
        if check_win(board,PLAYER):
            messagebox.showinfo("Tic Tac Toe","YOU WON!!")
            initialize()
            return
        elif is_board_full(board):
            messagebox.showinfo("Tic Tac Toe","IT'S A TIE!!")
            initialize()
            return
        if who!='p':
            row,col=get_optimal_move(board)
            button[row][col].config(text=COMP,state=tk.DISABLED,font=('Arial',9,'bold'),background='Light Green')
            board[row][col]=COMP
            if check_win(board,COMP):
                messagebox.showinfo("Tic Tac Toe","COMPUTER WON THE GAME!!")
                initialize()
                return
            elif is_board_full(board):
                messagebox.showinfo("Tic Tac Toe","IT'S A TIE!!")
                initialize()
                return
        else:
            PLAYER,COMP=COMP,PLAYER

r=tk.Tk()
r.title('Tic Tac Toe')
button=[[None for _ in range(3)]for _ in range(3)]
who=simpledialog.askstring("Input","Player(p) / Computer(c)") or 'c'
for i in range(3):
    for j in range(3):
        button[i][j]=tk.Button(r,text='  ',width=20,height=8,command=lambda i=i , j=j, who = who:button_click(i,j,who))
        button[i][j].grid(row=i,column=j,padx=1,pady=1)
initialize()
r.mainloop()