import tkinter as tk
import random

GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30

class Snake(tk.Canvas):

    def __init__(self):
        super().__init__(width=GRID_WIDTH * GRID_SIZE, 
                         height=GRID_HEIGHT * GRID_SIZE)
        self.snake_positions = [(14, 7), (15, 7)] 
        self.food_position = self.set_new_food_position()
        self.direction = 'Right'

        self.create_objects()
        self.bind_all('<Key>', self.on_key_press)

        self.pack()
        self.start_game()

    def set_new_food_position(self):
       while True:
           x = random.randint(0, GRID_WIDTH - 1)
           y = random.randint(0, GRID_HEIGHT - 1)
           if (x, y) not in self.snake_positions:
               return (x, y)

    def create_objects(self):
        self.delete(tk.ALL)
        for x, y in self.snake_positions:
            self.create_rectangle(x*GRID_SIZE, y*GRID_SIZE,
                                  (x+1)*GRID_SIZE, (y+1)*GRID_SIZE, 
                                  fill='green')
        self.create_oval(self.food_position[0]*GRID_SIZE, 
                         self.food_position[1]*GRID_SIZE,
                         (self.food_position[0]+1)*GRID_SIZE,
                         (self.food_position[1]+1)*GRID_SIZE,
                         fill='red')

    def move_snake(self):
        head_x, head_y = self.snake_positions[0]
        
        if self.direction == 'Right':
            new_head = (head_x + 1, head_y)
        elif self.direction == 'Left':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'Up':
            new_head = (head_x, head_y - 1)
            
        self.snake_positions.insert(0, new_head)
        
    def on_key_press(self, e):
        new_direction = e.keysym
        all_directions = ('Up', 'Down', 'Left', 'Right')
        opposites = ({'Up', 'Down'}, {'Left', 'Right'})

        if (new_direction in all_directions and
            {new_direction, self.direction} not in opposites):
            self.direction = new_direction

    def game_loop(self):
        self.move_snake()
        self.create_objects()
        self.after(100, self.game_loop)

    def start_game(self):
        self.after(100, self.game_loop)
        self.mainloop()
        
gui = Snake()