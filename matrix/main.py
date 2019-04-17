from display import *
from draw import *
import math

screen = new_screen()
color = [ 255, 0, 0 ]
edge_matrix = new_matrix(0, 0)

add_edge(edge_matrix, 300, 300, 0, 300, 350, 0)
add_edge(edge_matrix, 300, 300, 0, 350, 300, 0)
add_edge(edge_matrix, 300, 350, 0, 350, 350, 0)
add_edge(edge_matrix, 350, 350, 0, 350, 300, 0)
draw_lines(edge_matrix, screen, color)

for x in range(100):
    translate_matrix = make_translate(5,0,0)
    rotX_matrix = make_rotX(2)
    rotY_matrix = make_rotY(2)
    #scale_matrix = make_scale(2,2,0)
    #matrix_mult(scale_matrix, edge_matrix)
    matrix_mult(rotX_matrix, edge_matrix)
    matrix_mult(rotY_matrix, edge_matrix)
    matrix_mult(translate_matrix, edge_matrix)
    draw_lines(edge_matrix, screen, color)

display(screen)
