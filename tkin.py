import tkinter as tk
from tkinter import messagebox
  

def make_move(i, j):
    global current
    if grid[i][j]["text"] == "":
        grid[i][j]["text"] = current
        value=check_win(current)
        if value:
            messagebox.showinfo("Won the game","congratulations player "+current)
   
 
        if current == 'x':
            current = 'o'
        else:
            current = 'x'
def check_win(player):
    for i in range(3):
        if player==grid[i][0]["text"]==grid[i][1]["text"]==grid[i][2]["text"]:
            return True
        if player==grid[0][i]["text"]==grid[1][i]["text"]==grid[2][i]["text"]:
            return True      
    if player==grid[0][0]["text"]==grid[1][1]["text"]==grid[2][2]["text"]:
        return True
    if player==grid[2][0]["text"]==grid[1][1]["text"]==grid[0][2]["text"]:
        return True              
 
            

root = tk.Tk()
root.title("TicTacToe")

grid = []
current = 'x'

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", width=20, height=10, command=lambda i=i, j=j: make_move(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    grid.append(row)

root.mainloop()