def search_bsf(maze, destination):
    start_cell = (maze.rows, maze.cols)
    border = [start_cell]

    explorado = {start_cell: None}

    while border:
        actual_cell = border.pop(0)

        if actual_cell == destination:
            break

        for direction in 'ESNW':
            if maze.maze_map[actual_cell][direction]:
                if direction == 'E':
                    neighbor = (actual_cell[0], actual_cell[1] + 1)
                elif direction == 'W':
                    neighbor = (actual_cell[0], actual_cell[1] - 1)
                elif direction == 'N':
                    neighbor = (actual_cell[0] - 1, actual_cell[1])
                elif direction == 'S':
                    neighbor = (actual_cell[0] + 1, actual_cell[1])
                else:
                    print("Error")
                    break

                if neighbor not in explorado:
                    border.append(neighbor)
                    explorado[neighbor] = actual_cell

    path = {}
    actual_cell = destination
    while actual_cell != start_cell:
        path[explorado[actual_cell]] = actual_cell
        actual_cell = explorado[actual_cell]

    return path
