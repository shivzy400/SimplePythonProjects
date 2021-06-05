from tkinter import *
from tkinter import messagebox
from GameFunctions import *

def play_turn(buttons , num) :
    global positions
    place_character(buttons[num] , num)

    if is_win(buttons) :
        messagebox.showinfo("Game Over","Player Wins")
        reset_game(buttons)

    elif is_draw(buttons) :
        messagebox.showinfo("Game Over","Draw")
        reset_game(buttons)

def main_window(root) :
    root_title = Label(root , text = 'Welcome to Tic Tac Toe' , font = ('consolas' , 26))
    root_title.pack(padx=10 , pady=10)
    root_subtitle = Label(root , text = "Click 'Start Game' to Start" , font = ('consolas' , 14))
    root_subtitle.pack(padx=10 , pady=10)
    root_btn = Button(root , text = 'Start Game' , font=('consolas' , 15) , relief=GROOVE , bg='orange', command=lambda:game_window(root))
    root_btn.pack(padx=10 , pady=10 , ipadx=5 , ipady=5)

    root.mainloop()  

def game_window(root) :

    root.destroy()

    game = Tk()
    game.title('Tic Tac Toe')
    game.resizable(0,0)
    game_subtitle = Label(game , text = 'TicTacToe' , font = ('consolas' , 18))
    game_subtitle.grid(row=0 , column=0 , columnspan=3,padx=10 , pady=20)
    buttons = {
        i : Button(
            game , 
            font = ('consolas' , 24) , 
            relief=RIDGE , 
            width=7 , 
            height=3 , 
            bg = '#f1f2f6' ,
            command=lambda x = i:play_turn(buttons , x)
        ) for i in range(1,10) 
    }

    buttons[7].grid(row=1 , column=0 , padx=1 , pady=1)
    buttons[8].grid(row=1 , column=1 , padx=1 , pady=1)
    buttons[9].grid(row=1 , column=2 , padx=1 , pady=1)
    buttons[4].grid(row=2 , column=0 , padx=1 , pady=1)
    buttons[5].grid(row=2 , column=1 , padx=1 , pady=1)
    buttons[6].grid(row=2 , column=2 , padx=1 , pady=1)
    buttons[1].grid(row=3 , column=0 , padx=1 , pady=1)
    buttons[2].grid(row=3 , column=1 , padx=1 , pady=1)
    buttons[3].grid(row=3 , column=2 , padx=1 , pady=1)