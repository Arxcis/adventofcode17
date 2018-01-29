#!python
# -*- coding:utf-8 -*-


def exercise():
    SIZE = 1000
    grid = [[0 for y in range(SIZE)] for x in range(SIZE)]

    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3
    direction = RIGHT

    target = 347991
    value = 1
    step = 1
    x = SIZE / 2
    y = SIZE / 2
     
    while True:
        for i in (0,1):
            for i in range(step):
                if value > target:
                    return value
                
                grid[x][y] = value

                if   direction is RIGHT: x += 1
                elif direction is UP:    y += 1
                elif direction is LEFT:  x -= 1
                elif direction is DOWN:  y -= 1

                value = grid[x+1][y]+\
                        grid[x-1][y]+\
                        grid[x+1][y+1]+\
                        grid[x-1][y+1]+\
                        grid[x][y+1]+\
                        grid[x+1][y-1]+\
                        grid[x-1][y-1]+\
                        grid[x][y-1]

            direction = (direction + 1) % 4
        step += 1

if __name__ == "__main__":
    print(exercise())
