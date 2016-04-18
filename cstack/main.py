from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
temp = new_matrix()
ident(temp)
transform = [temp]
if len(sys.argv) == 2:
    f = open(sys.argv[1])

parse_file( f, edges, transform, screen, color )
f.close()
