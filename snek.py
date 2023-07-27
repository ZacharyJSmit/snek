import tkinter as tk 
import random

GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30

class Snake(tk.Canvas):

    def __init__(self):
        super().__init__(width=GRID_WIDTH * GRID_SIZE, 
                         height=GRID_HEIGHT * GRID_SIZE)
        self.snake_positions = [(14, 7), (15, 7), (16, 7)]
        self.food_position = self.generate_food()
        self.direction = 'Right'
        self.snake_length = 3
        self.score = 0

        self.create_objects()
        self.bind_all('<Key>', self.on_key_press)

        self.pack()
        self.after_id = self.after(100, self.game_loop)

    def generate_food(self):
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
                         
    def check_collisions(self):
        head = self.snake_positions[0]
        
        if head in self.snake_positions[1:]:
            self.game_over()
        
        if (head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT):
            self.game_over()

    def game_over(self):
        self.delete(tk.ALL)
        self.create_text(self.winfo_width()/2, self.winfo_height()/2,
                         text=f"Game Over! Length: {self.snake_length}", fill="red")
        self.after_cancel(self.after_id)
        
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
        
        if len(self.snake_positions) > self.snake_length:
            self.snake_positions.pop()

    def on_key_press(self, e):
        new_direction = e.keysym
        all_directions = ('Up', 'Down', 'Left', 'Right')
        opposites = ({'Up', 'Down'}, {'Left', 'Right'})

        if (new_direction in all_directions and 
            {new_direction, self.direction} not in opposites):
            self.direction = new_direction

    def game_loop(self):
        self.move_snake()
        self.check_collisions()
        self.create_objects()
        self.after_id = self.after(100, self.game_loop)
        
gui = Snake()
gui.pack()
gui.after_id = gui.after(100, gui.game_loop) 
gui.mainloop()