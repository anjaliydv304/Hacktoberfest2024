GRID_SIZE = 9

def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def is_valid(board, row, col, num):
    for x in range(GRID_SIZE):
        if board[row][x] == num:
            return False
    for x in range(GRID_SIZE):
        if board[x][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty_location(board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
