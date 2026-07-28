class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left","upper center","upper right",
        "middle left","center","middle right",
        "lower left","lower center","lower right"
    ]

    def __init__(self):
        self.board_array = [[" "]*3 for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.last_move = (row, column)
        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        b = self.board_array

        for r in range(3):
            if b[r][0] != " " and b[r][0] == b[r][1] == b[r][2]:
                return (True, f"{b[r][0]} has won.")

        for c in range(3):
            if b[0][c] != " " and b[0][c] == b[1][c] == b[2][c]:
                return (True, f"{b[0][c]} has won.")

        if b[1][1] != " ":
            if b[0][0] == b[1][1] == b[2][2]:
                return (True, f"{b[1][1]} has won.")
            if b[0][2] == b[1][1] == b[2][0]:
                return (True, f"{b[1][1]} has won.")

        full = all(b[r][c] != " " for r in range(3) for c in range(3))
        if full:
            return (True, "Cat's Game.")

        return (False, f"{self.turn}'s turn.")

board = Board()
print(board)

while True:
    print(f"{board.turn}'s move.")
    move = input("Enter move: ")

    try:
        board.move(move)
    except TictactoeException as e:
        print(e.message)
        continue

    print(board)
    done, msg = board.whats_next()
    print(msg)
    if done:
        break
