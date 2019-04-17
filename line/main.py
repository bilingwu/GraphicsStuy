from display import *
from draw import *

screen = new_screen()
color = [255, 255, 255]

x = 0
y = 0

while y < YRES:
    draw_line(screen, 0, y, x, YRES, color)
    draw_line(screen, x, 0, XRES, y, color)
    y += 3
    x += 3
    color[RED] = (color[RED] + 1) % MAX_COLOR
    color[GREEN] = (color[GREEN] + 3) % MAX_COLOR
    color[BLUE] = (color[BLUE] + 8) % MAX_COLOR

display(screen)
