Here we generates a random N×N grid (where N is between 4 and 7) with obstacles and open paths, then performs Depth-First Search (DFS) to find a path from a randomly placed source to a goal. The program prints the grid, movement steps, the DFS path, and the topological order of traversal.

We are doing:

Generating a random grid with obstacles (0) and paths (1).
Ensuring the source and goal are placed on valid non-obstacle positions.
Using DFS to find a path while tracking traversal order and backtracking correctly.
Printing the grid, movement steps, DFS path, and topological order.
