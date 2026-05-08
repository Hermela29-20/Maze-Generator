import turtle
import random
import time

# ---------------- CONFIG ---------------- #
ROWS, COLS = 20, 25        # Maze size
CELL_SIZE = 24             # Size of each cell

# ---------------- SCREEN ---------------- #
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Generator & Solver")
wn.setup(1300, 700)
wn.tracer(0)  

# ---------------- TURTLES ---------------- #

# Draws maze walls
wall_t = turtle.Turtle()
wall_t.hideturtle()
wall_t.speed(0)
wall_t.color("white")
wall_t.penup()

#  Generation mouse (will build maze later)
gen_mouse = turtle.Turtle()
gen_mouse.shape("circle")
gen_mouse.color("orange")
gen_mouse.penup()
gen_mouse.speed(0)

#  Solver mouse (will solve maze later)
solver_mouse = turtle.Turtle()
solver_mouse.shape("circle")
solver_mouse.color("red")
solver_mouse.penup()
solver_mouse.speed(0)

# Dead-end marker (for solver)
dead_t = turtle.Turtle()
dead_t.shape("square")
dead_t.color("blue")
dead_t.penup()
dead_t.speed(0)

#  Final path marker
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

# Start and End positions
start = (0,0)
end = (ROWS - 1, COLS - 1)

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

# ---------------- DRAW MAZE ---------------- #
def draw_maze():
    """Draw the entire maze based on wall arrays"""
    wall_t.clear()

    for r in range(ROWS):
        for c in range(COLS):
            x, y = cell_to_screen(r, c)

            # Draw NORTH wall
            if northWall[r][c] == 1:
                draw_line(x, y, x + CELL_SIZE, y)

            # Draw EAST wall
            if eastWall[r][c] == 1:
                draw_line(x + CELL_SIZE, y, x + CELL_SIZE, y - CELL_SIZE)

    # Draw bottom border
    for c in range(COLS):
        x, y = cell_to_screen(ROWS-1, c)
        draw_line(x, y - CELL_SIZE, x + CELL_SIZE, y - CELL_SIZE)

    # Draw left border
    for r in range(ROWS):
        x, y = cell_to_screen(r, 0)
        draw_line(x, y, x, y - CELL_SIZE)

# ---------------- MAZE GENERATION ---------------- #
def generate_maze():
    """
    Generate maze using DFS + stack (backtracking).
    This simulates the "mouse eating walls".
    """

    stack = []

    # Start from a random cell
    r = random.randint(0, ROWS-1)
    c = random.randint(0, COLS-1)

    visited[r][c] = True
    stack.append((r, c))

    while stack:
        r, c = stack[-1]

        # Move generation mouse
        x, y = cell_to_screen(r, c)
        gen_mouse.goto(x + CELL_SIZE/2, y - CELL_SIZE/2)

        neighbors = []

        # Check all 4 directions for unvisited neighbors
        if r > 0 and not visited[r-1][c]:
            neighbors.append((r-1, c, "N"))
        if c < COLS-1 and not visited[r][c+1]:
            neighbors.append((r, c+1, "E"))
        if r < ROWS-1 and not visited[r+1][c]:
            neighbors.append((r+1, c, "S"))
        if c > 0 and not visited[r][c-1]:
            neighbors.append((r, c-1, "W"))

        if neighbors:
            # Choose random neighbor
            nr, nc, d = random.choice(neighbors)

            # Remove wall between cells ("eat wall")
            if d == "N":
                northWall[r][c] = 0
            elif d == "E":
                eastWall[r][c] = 0
            elif d == "S":
                northWall[nr][nc] = 0
            elif d == "W":
                eastWall[nr][nc] = 0

            visited[nr][nc] = True
            stack.append((nr, nc))
        else:
            # Dead end → backtrack
            stack.pop()

       
        draw_maze()
        wn.update()
        time.sleep(0.02)
        
    
    # ---------------- SOLVER ---------------- #
def solve_maze():
    """Solve maze using backtracking (DFS)"""

    stack = [start]
    visited2 = set()

    while stack:
        r, c = stack[-1]
        visited2.add((r, c))

        # Move solver mouse
        x, y = cell_to_screen(r, c)
        solver_mouse.goto(x + CELL_SIZE/2, y - CELL_SIZE/2)

        wn.update()
        time.sleep(0.05)

        # Goal reached
        if (r, c) == end:
            return stack

        moved = False
        directions = ["N","E","S","W"]
        random.shuffle(directions)

        for d in directions:
            nr, nc = r, c

            if d == "N" and r > 0 and northWall[r][c] == 0:
                nr -= 1
            elif d == "E" and c < COLS-1 and eastWall[r][c] == 0:
                nc += 1
            elif d == "S" and r < ROWS-1 and northWall[r+1][c] == 0:
                nr += 1
            elif d == "W" and c > 0 and eastWall[r][c-1] == 0:
                nc -= 1

            if (nr, nc) not in visited2:
                stack.append((nr, nc))
                moved = True
                break

        if not moved:
            # Dead end → mark blue
            dx, dy = cell_to_screen(r, c)
            dead_t.goto(dx + CELL_SIZE/2, dy - CELL_SIZE/2)
            dead_t.stamp()
            stack.pop()

    return []
  
# ---------------- DRAW FINAL PATH ---------------- #
def draw_path(path):
    """Draw the final solution path (green)"""
    for (r, c) in path:
        x, y = cell_to_screen(r, c)
        path_t.goto(x + CELL_SIZE/2, y - CELL_SIZE/2)
        path_t.stamp()

        wn.update()
        time.sleep(0.01)
        
# ---------------- RUN ---------------- #
generate_maze()
draw_maze()
wn.update()

solution = solve_maze()
draw_path(solution)
wn.mainloop()