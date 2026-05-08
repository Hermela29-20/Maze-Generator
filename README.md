# Maze Generator and Solver (Backtracking DFS Algorithm)

Demo recording(loom recording): https://www.loom.com/share/fc210e53d0b2494a9a50be579d50b662

## Overview of the Project

The presented project represents a visually represented maze generator and solver made in Python and Python Turtle Graphics library.

The application:

1. Creates a random rectangular maze using the stack-based DFS backtracking algorithm.
2. Generates the maze with a live animation, where an orange-colored "mouse" creates the passage between the cells by deleting walls.
3. Uses another DFS algorithm to solve the maze.
4. Visualizes the following items:
   - Mouse movement
   - Dead ends
   - Correct solution path

The maze created through this project is a **proper maze** because:
- Every cell is connected
- There exists a single unique path from any point to another
- It contains no isolated areas


# Used Technologies

- Python 3
- Turtle Graphics
- DFS (Depth First Search)
- Stack


# Maze Representation

The maze consists of two wall arrays:

 python
northWall[r][c]
eastWall[r][c]