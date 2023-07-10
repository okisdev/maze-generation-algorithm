import random
import numpy as np
import matplotlib.pyplot as plt


def create_maze(width, height):
    maze = np.ones((width, height))
    divide(maze, 0, 0, width, height)
    return maze


def divide(maze, x, y, width, height):
    if width < 3 or height < 3:
        return

    if width > height:
        divide_vertically(maze, x, y, width, height)
    else:
        divide_horizontally(maze, x, y, width, height)


def divide_vertically(maze, x, y, width, height):
    dx = random.randint(x + 1, x + width - 2)
    maze[dx, y : y + height] = 0
    dy = random.randint(y, y + height - 1)
    maze[dx, dy] = 1
    divide(maze, x, y, dx - x, height)
    divide(maze, dx + 1, y, x + width - dx - 1, height)


def divide_horizontally(maze, x, y, width, height):
    dy = random.randint(y + 1, y + height - 2)
    maze[x : x + width, dy] = 0
    dx = random.randint(x, x + width - 1)
    maze[dx, dy] = 1
    divide(maze, x, y, width, dy - y)
    divide(maze, x, dy + 1, width, y + height - dy - 1)


def print_maze(maze):
    for row in maze:
        print(''.join(['#' if cell else ' ' for cell in row]))


def plot_maze_visualisation(maze):
    plt.imshow(maze, cmap='binary')
    plt.show()


if __name__ == '__main__':
    width = int(input('Enter maze width: '))
    height = int(input('Enter maze height: '))

    maze = create_maze(width, height)

    print_maze(maze)
    plot_maze_visualisation(maze)
