from tkinter import *
from PIL import Image , ImageTk
from random import randint

MOVE_INCREMENT = 20
moves_per_sec = 10
GAME_SPEED = 1000 // moves_per_sec

class Snake(Canvas) :
    def __init__(self) :
        super().__init__(width=600 , height=620 , background='black' , highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_food_position()
        self.direction = "Right"
        self.bind_all('<Key>' , self.on_key_press)

        self.score = 0

        self.load_assets()
        self.create_objects()

        self.after(75 , self.perform_action)

    def load_assets(self) :
        try :
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("./assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)

        except IOError as error :
            print(error)
            root.destroy()

    def create_objects(self) :
        
        self.create_text(
            45 , 12 , text = f'Score : {self.score}' , tag ='score' ,fill='#fff' , font = ('consolas' , 14)
        )
        for x_pos , y_pos in self.snake_positions :
            self.create_image(x_pos , y_pos , image = self.snake_body , tag="snake")

        self.create_image(*self.food_position , image = self.food , tag = 'food')

    def move_snake(self) :
        head_x_pos , head_y_pos = self.snake_positions[0]

        if self.direction == 'Right' :
            new_head_position = (head_x_pos + MOVE_INCREMENT , head_y_pos)
        elif self.direction == 'Left' :
            new_head_position = (head_x_pos - MOVE_INCREMENT , head_y_pos)
        elif self.direction == 'Down' :
            new_head_position = (head_x_pos , head_y_pos + MOVE_INCREMENT)
        elif self.direction == 'Up' :
            new_head_position = (head_x_pos , head_y_pos - MOVE_INCREMENT)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    def perform_action(self) :
        if self.check_collisions() :
            self.endgame()
            return

        self.check_food_eaten()
        self.move_snake()
        self.after(GAME_SPEED , self.perform_action)

    def check_collisions(self) :
        head_x_pos , head_y_pos = self.snake_positions[0]

        return (
            head_x_pos in (0 , 600) or
            head_y_pos in (20 , 620) or
            (head_x_pos , head_y_pos) in self.snake_positions[1:]
        )

    def on_key_press(self , e) :
        new_direction = e.keysym 
        all_directions = ('Up' , 'Down' , 'Left' , 'Right')
        opposites = ({'Up' , 'Down'} , {'Left' , 'Right'})

        if new_direction in all_directions and {new_direction , self.direction} not in opposites :
            self.direction = new_direction

    def check_food_eaten(self) :
        if self.snake_positions[0] == self.food_position :
            self.score = self.score + 1
            self.snake_positions.append(self.snake_positions[-1])

            self.create_image(
                *self.snake_positions[-1] , image = self.snake_body , tag = 'snake'
            )
            score = self.find_withtag('score')
            self.itemconfigure(score , text = f'Score : {self.score}' , tag = 'score')

            self.food_position = self.set_food_position()
            self.coords(self.find_withtag('food') , self.food_position)

    def set_food_position(self) :
        while True :
            x_pos = randint(1 , 29) * MOVE_INCREMENT
            y_pos = randint(3 , 30) * MOVE_INCREMENT

            food_position = (x_pos , y_pos)
            if food_position not in self.snake_positions :
                return food_position

    def endgame(self) :
        self.delete(ALL)
        self.create_text(
            self.winfo_width() / 2 ,
            self.winfo_height() / 2,
            text = f'Game Over! Your score : {self.score}' ,
            fill = '#fff' , 
            font = ('consolas' , 24)
        )
                 

root = Tk()
root.title('Snake Game')
root.resizable(0 , 0)

board = Snake()
board.pack()

root.mainloop()