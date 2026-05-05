import turtle
import random
import time

# ---------------- CONFIG ---------------- #
ROWS, COLS = 20, 25        # Maze size
CELL_SIZE = 24             # Size of each cell

# ---------------- SCREEN ---------------- #
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Generator & Solver (DFS - Animated)")
wn.setup(1300, 700)
wn.tracer(0)  

# ---------------- TURTLES ---------------- #

# Draws maze walls
wall_t = turtle.Turtle()
wall_t.hideturtle()
wall_t.speed(0)
wall_t.color("white")
wall_t.penup()

# 🟠 Generation mouse (will build maze later)
gen_mouse = turtle.Turtle()
gen_mouse.shape("circle")
gen_mouse.color("orange")
gen_mouse.penup()
gen_mouse.speed(0)

# 🔴 Solver mouse (will solve maze later)
solver_mouse = turtle.Turtle()
solver_mouse.shape("circle")
solver_mouse.color("red")
solver_mouse.penup()
solver_mouse.speed(0)

# 🔵 Dead-end marker (for solver)
dead_t = turtle.Turtle()
dead_t.shape("square")
dead_t.color("blue")
dead_t.penup()
dead_t.speed(0)

# 🟢 Final path marker
path_t = turtle.Turtle()
path_t.shape("square")
path_t.color("green")
path_t.penup()
path_t.speed(0)

# ---------------- DATA STRUCTURE ---------------- #
"""
Maze Representation :

northWall[r][c]:
    = 1 → the cell (r, c) has a solid NORTH wall
    = 0 → the north wall has been removed

eastWall[r][c]:
    = 1 → the cell (r, c) has a solid EAST wall
    = 0 → the east wall has been removed

- Only store TWO walls per cell (North and East)
- This avoids redundancy and saves memory

Wall relationships:
- SOUTH wall of (r, c) = northWall[r+1][c]
- WEST wall of (r, c)  = eastWall[r][c-1]

"""

# Initialize all walls as PRESENT (1 = wall exists)
northWall = [[1]*COLS for _ in range(ROWS)]
eastWall  = [[1]*COLS for _ in range(ROWS)]

# Track visited cells during maze generation
visited = [[False]*COLS for _ in range(ROWS)]

# Start and End placeholders (will be set later)
start = None
end = None

# ---------------- HELPERS ---------------- #

def cell_to_screen(r, c):
    """
    Converts grid coordinates (row, col)
    into screen coordinates (x, y)
    """
    x = -600 + c * CELL_SIZE
    y = 300 - r * CELL_SIZE
    return x, y


def draw_line(x1, y1, x2, y2):
    """
    Draws a single wall segment on screen
    using the wall turtle
    """
    wall_t.goto(x1, y1)
    wall_t.pendown()
    wall_t.goto(x2, y2)
    wall_t.penup()

wn.mainloop()