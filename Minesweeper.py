import randomize

def create_board(width, height, num_mines):
    board = [[' ' for _ in range(width)] for _ in range(height)]
    mine_positions = random.sample(range(width * height), num_mines)
    
    for mine_position in mine_positions:
        row = mine_position // width
        col = mine_position % width
        board[row][col] = 'M'
    
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_adjacent_mines(board, row, col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'M':
            count += 1
    
    return count

def reveal_empty_cells(board, row, col):
    if board[row][col] != ' ':
        return
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 'M':
            board[r][c] = str(count_adjacent_mines(board, r, c))
            if board[r][c] == '0':
                reveal_empty_cells(board, r, c)

if __name__ == "__main__":
    play_game()


def play_games():
    width = 10
    height = 10
    num_mines = 20
    board = create_board(width, height, num_mines)
    revealed_cells = set()
    
    print("Welcome to Minesweeper!")
    
    while True:
        print_board(board)
        row = int(input("Enter row (0 to {}): ".format(height - 1)))
        col = int(input("Enter column (0 to {}): ".format(width - 1)))
        
        if (row, col) in revealed_cells:
            print("You've already revealed this cell!")
            continue
        
        if board[row][col] == 'M':
            print("Game over! You hit a mine.")
            break
        
        revealed_cells.add((row, col))
        
        if board[row][col] == ' ':
            reveal_empty_cells(board, row, col)
        
        if len(revealed_cells) == width * height - num_mines:
            print("Congratulations! You've won!")
            break

