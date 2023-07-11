from queue import Queue
from queue import PriorityQueue


def out_of_bounds(board, row, col):
    return len(board) <= row or len(board[0]) <= col or row < 0 or col < 0


def distance_between_points(p1, p2):
    return ((abs(p1[0]-p2[0])**2)+(p1[1]-p2[1])**2)**0.5


def bfs(board, initial):
    directions = []
    for i in range(len(board)):
        directions.append([])
        for _ in range(len(board[0])):
            directions[i].append(None)
    directions[initial[0]][initial[1]] = "start"
    q = Queue()
    q.put(initial)
    while q.qsize() != 0:
        row, col = q.get()
        for direction in ("up", "down", "left", "right"):
            match direction:
                case "up":
                    next_row, next_col = (row, col-1)
                case "down":
                    next_row, next_col = (row, col+1)
                case "left":
                    next_row, next_col = (row-1, col)
                case "right":
                    next_row, next_col = (row+1, col)
            if out_of_bounds(board, next_row, next_col):
                continue
            if board[next_row][next_col] == 1 or board[next_row][next_col] == 100:
                continue
            if board[next_row][next_col] == 2:
                print("YESYESYES")
                print(directions)
                while direction != "start":
                    match direction:
                        case "up":
                            next_col += 1
                        case "down":
                            next_col -= 1
                        case "left":
                            next_row += 1
                        case "right":
                            next_row -= 1
                    direction = directions[next_row][next_col]
                    board[next_row][next_col] += 2
                print("YESYESYES")
                return True
            board[next_row][next_col] = 1
            directions[next_row][next_col] = direction
            q.put((next_row, next_col))
    return False


def dijkstra(board, initial):
    distance = []
    directions = []
    processed = []
    q = PriorityQueue()
    q.put((0, initial))
    for i in range(len(board)):
        distance.append([])
        directions.append([])
        processed.append([])
        for _ in range(len(board[0])):
            distance[i].append(float("inf"))
            directions[i].append(None)
            processed[i].append(False)
    distance[initial[0]][initial[1]] = 0
    directions[initial[0]][initial[1]] = "start"
    board[initial[0]][initial[1]] = 0
    while q.qsize() != 0:
        row, col = q.get()[1]
        if processed[row][col]:
            continue
        processed[row][col] = True
        board[row][col] += 1
        for direction in ("north", "south", "west", "east"):
            match direction:
                case "north":
                    next_row, next_col = (row-1, col)
                case "south":
                    next_row, next_col = (row+1, col)
                case "west":
                    next_row, next_col = (row, col-1)
                case "east":
                    next_row, next_col = (row, col+1)
            if out_of_bounds(board, next_row, next_col):
                continue
            if board[next_row][next_col] == 2:
                while direction != "start":
                    match direction:
                        case "north":
                            next_row += 1
                        case "south":
                            next_row -= 1
                        case "west":
                            next_col += 1
                        case "east":
                            next_col -= 1
                    board[next_row][next_col] += 2
                    direction = directions[next_row][next_col]
                return
            if distance[row][col] + board[next_row][next_col] < distance[next_row][next_col]:
                distance[next_row][next_col] = distance[row][col] + \
                    board[next_row][next_col]
                q.put((distance[next_row][next_col], (next_row, next_col)))
                directions[next_row][next_col] = direction


def aStar(board, initial):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                target = (i, j)
                break
    distance = []
    directions = []
    processed = []
    q = PriorityQueue()
    q.put((0, initial))
    for i in range(len(board)):
        distance.append([])
        directions.append([])
        processed.append([])
        for _ in range(len(board[0])):
            distance[i].append(float("inf"))
            directions[i].append(None)
            processed[i].append(False)
    distance[initial[0]][initial[1]] = 0
    directions[initial[0]][initial[1]] = "start"
    board[initial[0]][initial[1]] = 0
    while q.qsize() != 0:
        row, col = q.get()[1]
        if processed[row][col]:
            continue
        processed[row][col] = True
        board[row][col] += 1
        for direction in ("north", "south", "west", "east"):
            match direction:
                case "north":
                    next_row, next_col = (row-1, col)
                case "south":
                    next_row, next_col = (row+1, col)
                case "west":
                    next_row, next_col = (row, col-1)
                case "east":
                    next_row, next_col = (row, col+1)
            if out_of_bounds(board, next_row, next_col):
                continue
            if board[next_row][next_col] == 2:
                while direction != "start":
                    match direction:
                        case "north":
                            next_row += 1
                        case "south":
                            next_row -= 1
                        case "west":
                            next_col += 1
                        case "east":
                            next_col -= 1
                    board[next_row][next_col] += 2
                    direction = directions[next_row][next_col]
                return
            heur = distance_between_points((next_row, next_col), target)
            if board[next_row][next_col] + heur*5 < distance[next_row][next_col]:
                distance[next_row][next_col] = board[next_row][next_col] + heur*5
                q.put((distance[next_row][next_col], (next_row, next_col)))
                directions[next_row][next_col] = direction
