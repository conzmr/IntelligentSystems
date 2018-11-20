__author__ = 'misbah'
from Tkinter import *
import time
import random

#print(random.randint(0,9))
window = Tk()
window.title("Misbah")

size = 5
Walls = [(0, 5), (1, 0), (1, 1), (1, 5), (2, 3),
     (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1)]
rows = size
cols = size
player = (0,0)
end = (5,5)

for i in range(cols):
    for j in range(1,rows):
        Walls.append((i,j))


Width = 600/rows


platform = Canvas(window, width = cols*Width, height = rows*Width)
platform.pack()

def render_grid():
    global rows, cols, Width, player, end
    for i in range(cols):
        for j in range(rows):
            platform.create_rectangle(i*Width, j*Width,(i+1)*Width, (j+1)*Width, fill="black", width = 1)

    platform.create_rectangle(player[0]*Width, player[1]*Width,(player[0]+1)*Width, (player[1]+1)*Width, fill="blue", width = 1)
    platform.create_rectangle(end[0]*Width, end[1]*Width,(end[0]+1)*Width, (end[1]+1)*Width, fill="red", width = 1)

    for (i,j) in Walls:
        platform.create_rectangle(i*Width, j*Width,(i+1)*Width, (j+1)*Width, fill="black", width = 1)

render_grid()

def render_path(path):
    global Width
    for (i,j) in path:
        platform.create_rectangle(i*Width, j*Width,(i+1)*Width, (j+1)*Width, fill="blue", width = 1)
        time.sleep(0.1)

def render_block(block, color):
    global Width
    #print (str(block)+" color = "+color)
    platform.create_rectangle(block[0]*Width, block[1]*Width,(block[0]+1)*Width, (block[1]+1)*Width, fill=color, width = 1)


def start_game():
    window.mainloop()
