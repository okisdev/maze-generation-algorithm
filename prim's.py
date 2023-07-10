import random
import numpy as np
import matplotlib.pyplot as plt


def create_maze(width=50, height=50):
    maze = [['WALL' for _ in range(width)] for _ in range(height)]
    start_x, start_y = (
        random.randint(0, width // 2) * 2,
        random.randint(0, height // 2) * 2,
    )
    maze[start_y][start_x] = 'EMPTY'

    wall_list = [
        (start_x, start_y, x, y)
        for (x, y) in [
            (start_x - 1, start_y),
            (start_x, start_y + 1),
            (start_x + 1, start_y),
            (start_x, start_y - 1),
        ]
    ]
    while wall_list:
        _, _, x, y = wall_list.pop(random.randint(0, len(wall_list) - 1))

        if (
            x > 0
            and x < width - 1
            and y > 0
            and y < height - 1
            and maze[y][x] == 'WALL'
        ):
            s = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            if sum(maze[y2][x2] == 'EMPTY' for x2, y2 in s) == 1:
                maze[y][x] = 'EMPTY'
                wall_list += [(x, y, x2, y2) for x2, y2 in s]

    return maze


def print_maze(maze):
    for row in maze:
        print(''.join(['#' if cell == 'WALL' else ' ' for cell in row]))


def plot_maze_visualisation(maze):
    # Convert the maze to a numpy array for easier plotting
    maze_array = np.array(
        [[0 if cell == 'WALL' else 1 for cell in row] for row in maze]
    )

    plt.figure(figsize=(10, 10))
    plt.imshow(maze_array, cmap='Greys', interpolation='nearest')
    plt.xticks([]), plt.yticks([])  # Hide the axes
    plt.show()


if __name__ == '__main__':
    width = int(input('Enter maze width: '))
    height = int(input('Enter maze height: '))

    maze = create_maze(width, height)

    print_maze(maze)
    plot_maze_visualisation(maze)
