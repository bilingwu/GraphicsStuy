import random

picture = "P3 500 500 255 "
for RESY in range(500):
    for RESX in range(500):
    	r = random.randrange( 0, 256)
	g = random.randrange( 0, 256)
	b = random.randrange( 0, 256)
	picture += "%d %d %d "%(r,g,b)

f = open("pic.ppm", "w")
f.write(picture)
f.close()
