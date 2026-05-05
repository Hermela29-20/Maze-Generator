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


wn.mainloop()