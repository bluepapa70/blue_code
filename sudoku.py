import random

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid(board, num, pos):
    row, col = pos
    # Check row
    for i in range(9):
        if board[row][i] == num and col != i:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num and row != i:
            return False
    # Check box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def fill_board(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find
    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if valid(board, num, (row, col)):
            board[row][col] = num
            if fill_board(board):
                return True
            board[row][col] = 0
    return False

def remove_numbers(board, attempts=40):
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        backup = board[row][col]
        board[row][col] = 0
        board_copy = [r[:] for r in board]
        if not solve(board_copy):
            board[row][col] = backup
        attempts -= 1

def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    remove_numbers(board)
    return board

def main():
    board = generate_sudoku()
    print("--- SUDOKU ---")
    print_board(board)
    while True:
        inp = input("입력 (row col num) 또는 'q'로 종료: ")
        if inp.lower() == 'q':
            break
        try:
            row, col, num = map(int, inp.split())
            if board[row][col] == 0 and valid(board, num, (row, col)):
                board[row][col] = num
                print_board(board)
                if not find_empty(board):
                    print("축하합니다! 스도쿠를 완성했습니다.")
                    break
            else:
                print("잘못된 입력입니다.")
        except Exception:
            print("입력 형식이 올바르지 않습니다. 예: 0 1 5")

if __name__ == "__main__":
    main()
