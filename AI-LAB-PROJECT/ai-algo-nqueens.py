class NQueenSolver:
    def __init__(self, N):
        self.N = N
        self.queens = [-1] * N
        self.cols = set()
        self.diag1 = set()
        self.diag2 = set()
        self.solutions = []

    def is_safe(self, r, c):
        return c not in self.cols and (r - c) not in self.diag1 and (r + c) not in self.diag2

    def place_queen(self, r, c):
        self.queens[r] = c
        self.cols.add(c)
        self.diag1.add(r - c)
        self.diag2.add(r + c)

    def remove_queen(self, r, c):
        self.queens[r] = -1
        self.cols.remove(c)
        self.diag1.remove(r - c)
        self.diag2.remove(r + c)

    def solve(self, row=0):
        if row == self.N:
            self.solutions.append(self.queens[:])
            return
        for col in range(self.N):
            if self.is_safe(row, col):
                self.place_queen(row, col)
                self.solve(row + 1)
                self.remove_queen(row, col)

    def display_solutions(self):
        if not self.solutions:
            print(f"\nNo solutions exist for {self.N}-Queens.\n")
            return

        print(f"\nTotal Solutions for {self.N}-Queens: {len(self.solutions)}\n")
        for idx, solution in enumerate(self.solutions, start=1):
            print(f"Solution {idx}: {solution}")
            self.print_board(solution)
            print()

    def print_board(self, solution):
        for r in range(self.N):
            row = ""
            for c in range(self.N):
                row += "Q " if solution[r] == c else ". "
            print(row.strip())


if __name__ == "__main__":
    try:
        size = int(input("Enter board size (e.g., 2 for 2x2, 4 for 4x4): "))
        if size < 1:
            print("Board size must be at least 1.")
        else:
            solver = NQueenSolver(size)
            solver.solve()
            solver.display_solutions()
    except ValueError:
        print("Please enter a valid integer.")
