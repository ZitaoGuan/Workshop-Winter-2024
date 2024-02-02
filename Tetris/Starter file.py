import pygame
import random
 
# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height
 
 
# SHAPE FORMATS
 
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape
 
 
class Piece(object):
    #Initialize piece properties: x, y, shape, color, rotation
    pass
 
def create_grid(locked_positions={}):
    #Create a 2D grid with empty cells and locked positions filled
    pass
 
def convert_shape_format(shape):
    #Convert the shape format to a list of positions
    pass
 
def valid_space(shape, grid):
    #Check if the current piece can be placed in the grid
    pass
 
def check_lost(positions):
    #Check if any piece is above the visible area
    pass
 
def get_shape():
    #Create a new random piece
    pass
 
 
def draw_text_middle(text, size, color, surface):
    #Draw text in the middle of the screen
    pass
   
def draw_grid(surface, row, col):
    #Draw the grid lines on the game window
    pass
 
def clear_rows(grid, locked):
    #Draw the grid lines on the game window
    pass
 
def draw_next_shape(shape, surface):
    #Draw the next shape preview on the screen
    pass
 
def draw_window(surface):
    #Draw the entire game window
    pass
 
def main():
    #Initialize game variables and enter the game loop
    # while the game is running:
    #     Update fall speed, handle user input, and move the current piece
    #     Check for collisions and update the grid
    #     Draw the game window and the next shape preview
    #     Check if the game is over
    pass

def main_menu():
    #Display the main menu and wait for user input to start the game
    pass
 
main_menu()  # start game