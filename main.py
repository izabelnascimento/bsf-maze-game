from pyamaze import maze, agent
from search import search_bsf

maze = maze(100, 100)
maze.CreateMaze()

player = agent(maze, filled=True, footprints=True)

cells = maze.grid
print("\nCelulas: ", cells)

destination = (1, 1)
path = search_bsf(maze, destination)
print("\nCaminho: ", path)

maze.tracePath({player: path}, delay=10)

print("\nTotal de células:", len(maze.maze_map.keys()))

maze.run()
