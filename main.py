from uib_inf100_graphics import *
import random
import PIL
import algorithms


def add_entity_at_random_location(grid, type):
    while True:
        i = random.choice(range(len(grid)))
        j = random.choice(range(len(grid[0])))
        if grid[i][j] == 0:
            grid[i][j] = type
            return (i, j)


def draw_board(canvas, x1, y1, x2, y2, board, color_set):
    step_x = (x2 - x1)/len(board[0])
    step_y = (y2 - y1)/len(board)
    # canvas.create_rectangle(x1-1, y1-1, x2 ,y2, fill=color_set["background"], outline=color_set["outline"])
    for i, r in enumerate(board):
        for j, n in enumerate(r):
            start_x, end_x = (x1 + step_x*j, x1 + step_x*(j+1))
            start_y, end_y = (y1 + step_y*i, y1+step_y*(i+1))
            canvas.create_rectangle(start_x, start_y, end_x, end_y,
                                    fill=color_set[f"cell{board[i][j]}"], outline=color_set["outline"])


def app_started(app):
    app.board_width = 40
    app.board_height = 70
    app.board = []
    for i in range(app.board_width):
        app.board.append([])
        for _ in range(app.board_height):
            app.board[i].append(0)
    app.start_pos = add_entity_at_random_location(app.board, 1)
    app.end_pos = add_entity_at_random_location(app.board, 2)
    for _ in range(1000):
        add_entity_at_random_location(app.board, 100)
    app.timer_delay = 100
    app.transparent_background = PIL.ImageTk.PhotoImage(
        PIL.Image.new(mode="RGBA", size=(1000, 750), color=(255, 255, 255, 40)))
    app.color_set = {
        "background": "#283546",
        "cell100": "#000",
        "cell101": "darkred",
        "cell103": "gray",
        "cell0": "#283546",
        "cell1": "red",
        "cell2": "yellow",
        "cell3": "green",
        "outline": "#1f2c37",
        "wall": "#e34534",
        "visited": "#2e8ed4"
    }


def timer_fired(app):
    ...


def key_pressed(app, event):
    if event.key == "Space":
        print("testing")
        algorithms.aStar(app.board, app.start_pos)
    if event.key == "r":
        run_app(width=1440, height=750, title="Pathfinding app")


def redraw_all(app, canvas):
    draw_board(canvas, 0, 0, app.width, app.height, app.board, app.color_set)


run_app(width=1440, height=750, title="Pathfinding app")
