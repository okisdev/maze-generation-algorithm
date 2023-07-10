import random
import matplotlib.pyplot as plt


def create_maze(width=50, height=50):
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)  # Only odd shapes
    complexity = 0.75
    density = 0.75
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))  # Number of components
    density = int(density * ((shape[0] // 2) * (shape[1] // 2)))  # Size of components
    # Build actual maze
    Z = [[0] * shape[1] for _ in range(shape[0])]
    # Fill borders
    for x in range(shape[1]):
        Z[0][x] = Z[-1][x] = 1
    for y in range(shape[0]):
        Z[y][0] = Z[y][-1] = 1
    # Make aisles
    for _ in range(density):
        x, y = (
            random.randint(0, shape[1] // 2) * 2,
            random.randint(0, shape[0] // 2) * 2,
        )
        Z[y][x] = 1
        for _ in range(complexity):
            neighbours = []
            if x > 1:
                neighbours.append((y, x - 2))
            if x < shape[1] - 2:
                neighbours.append((y, x + 2))
            if y > 1:
                neighbours.append((y - 2, x))
            if y < shape[0] - 2:
                neighbours.append((y + 2, x))
            if len(neighbours):
                y_, x_ = neighbours[random.randint(0, len(neighbours) - 1)]
                if Z[y_][x_] == 0:
                    Z[y_][x_] = 1
                    Z[y_ + (y - y_) // 2][x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    return Z


def print_maze(Z):
    for row in Z:
        print(''.join(['#' if cell else ' ' for cell in row]))


def plot_maze_visualisation(Z):
    plt.figure(figsize=(10, 5))
    plt.imshow(Z, cmap=plt.cm.binary, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    width = int(input('Enter maze width: '))
    height = int(input('Enter maze height: '))

    maze = create_maze(width, height)

    print_maze(maze)
    plot_maze_visualisation(maze)
