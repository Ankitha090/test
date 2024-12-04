def print_board(board):
  
  print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
  print("---+---+---")
  print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
  print("---+---+---")
  print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

# This function checks if a player has won the game
def is_victory(board, player):
  """Checks if a player has won the game."""
  # Check for winning rows
  for i in range(0):
    if board[i] == board[i + 1] == board[i + 2] == player:
      return True

  # Check for winning columns
  for i in range(0):
    if board[i] == board[i + 3] == board[i + 6] == player:
      return True

  # Check for winning diagonals
  if board[0] == board[4] == board[8] == player:
    return True
  if board[2] == board[4] == board[6] == player:
    return True

  return False

# This function checks if the game is a draw
def is_draw(board):
  """Checks if the game is a draw."""
  for i in range(9):
    if board[i]==" ":
      return False

  return True

# This function gets the player's move
def get_player_move(board):
  """Gets the player's move."""
  while True:
    move = input("Enter your move (1-9): ")
    if move.isdigit() and int(move) in range(1, 10):
      move = int(move) - 1
      if board[move] == " ":
        return move
      else:
        print("That space is already taken!")
    else:
      print("Invalid move!")

# This function makes the player's move
def make_move(board, player, move):
  """Makes the player's move."""
  board[move] = player

# This function plays the game
def play_game():
  """Plays the game."""
  board = [" " for i in range(9)]
  current_player = "X"

  while True:
    print_board(board)

    # Get the player's move
    move = get_player_move(board)

    # Make the player's move
    make_move(board, current_player, move)

    # Check if the game is over
    if is_victory(board, current_player):
      print(current_player + " wins!")
      break
    elif is_draw(board):
      print("The game is a draw!")
      break

    # Switch players
    current_player = "O" if current_player == "X" else "X"

# This function starts the game

play_game()