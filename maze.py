import pgzrun

WIDTH = 700
HEIGHT = 490

map_data = [[1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 0 ,1, 0, 1],
            [0, 1, 1, 0, 0 ,0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0]]


floor = Actor('floor', topleft = (0,0))
player = Actor('player', topleft = (70,0))
box = Actor('box', topleft = (0,0))

def draw():
    screen.clear()
    
    # background
    for y in range(7):
        for x in range(10):
            # floor
            floor.topleft = (70*x, 70*y)
            floor.draw()
            #box
            if map_data[y][x] == 1:
                box.topleft = (70*x, 70*y)
                box.draw()


    player.draw()

pgzrun.go()