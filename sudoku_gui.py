import tkinter as tk
from tkinter import messagebox
import random

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Game")
        self.board = self.generate_sudoku()
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.draw_board()
        self.create_buttons()

    def draw_board(self):
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(self.master, borderwidth=1, relief="solid")
                frame.grid(row=i, column=j, padx=(2 if j % 3 == 0 else 0, 2 if j == 8 else 0), pady=(2 if i % 3 == 0 else 0, 2 if i == 8 else 0))
                value = self.board[i][j]
                if value != 0:
                    entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center", disabledforeground="black")
                    entry.insert(0, str(value))
                    entry.config(state="disabled")
                else:
                    entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=0, column=0)
                self.cells[i][j] = entry

    def create_buttons(self):
        check_btn = tk.Button(self.master, text="정답 확인", command=self.check_solution)
        check_btn.grid(row=9, column=0, columnspan=4, sticky="ew", pady=10)
        reset_btn = tk.Button(self.master, text="초기화", command=self.reset_board)
        reset_btn.grid(row=9, column=5, columnspan=4, sticky="ew", pady=10)

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].get()
                if not val.isdigit() or not (1 <= int(val) <= 9):
                    messagebox.showerror("오류", f"{i+1}행 {j+1}열에 올바른 숫자를 입력하세요.")
                    return
                self.board[i][j] = int(val)
        if self.is_valid_solution():
            messagebox.showinfo("성공", "축하합니다! 스도쿠를 완성했습니다.")
        else:
            messagebox.showerror("오답", "정답이 아닙니다. 다시 시도하세요.")

    def reset_board(self):
        self.board = self.generate_sudoku()
        for i in range(9):
            for j in range(9):
                entry = self.cells[i][j]
                entry.config(state="normal")
                entry.delete(0, tk.END)
                value = self.board[i][j]
                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(state="disabled")
                else:
                    entry.config(state="normal")

    def is_valid_solution(self):
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if self.board[i][j] in row or self.board[j][i] in col:
                    return False
                row.add(self.board[i][j])
                col.add(self.board[j][i])
        for box_y in range(3):
            for box_x in range(3):
                nums = set()
                for i in range(box_y*3, box_y*3+3):
                    for j in range(box_x*3, box_x*3+3):
                        if self.board[i][j] in nums:
                            return False
                        nums.add(self.board[i][j])
        return True

    def generate_sudoku(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_board(board)
        self.remove_numbers(board)
        return board

    def fill_board(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        row, col = find
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if self.valid(board, num, (row, col)):
                board[row][col] = num
                if self.fill_board(board):
                    return True
                board[row][col] = 0
        return False

    def remove_numbers(self, board, attempts=40):
        while attempts > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while board[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            backup = board[row][col]
            board[row][col] = 0
            board_copy = [r[:] for r in board]
            if not self.solve(board_copy):
                board[row][col] = backup
            attempts -= 1

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def valid(self, board, num, pos):
        row, col = pos
        for i in range(9):
            if board[row][i] == num and col != i:
                return False
        for i in range(9):
            if board[i][col] == num and row != i:
                return False
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        row, col = find
        for i in range(1, 10):
            if self.valid(board, i, (row, col)):
                board[row][col] = i
                if self.solve(board):
                    return True
                board[row][col] = 0
        return False

def main():
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
