# players board
play_board = ["-","-","-",
              "-","-","-",
              "-","-","-"]


game_on = True
current_player = "X" # X player goes first
winner = None
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# display players board
def display_play_board():
  print(play_board[0] + " | " + play_board[1] + " | " + play_board[2])
  print(play_board[3] + " | " + play_board[4] + " | " + play_board[5])
  print(play_board[6] + " | " + play_board[7] + " | " + play_board[8])


def handle_turn(current_player):
  global numbers
  print(current_player + "'s turn.")
  selection = input("Choose your favorite number from 1 to 9: ")

  valid = False

  while not valid:
    while selection not in numbers:
      selection = input("Choose a number from 1 to 9: ")
    selection = int(selection) - 1
    # do not over write a filled in position
    if play_board[selection] == "-":
      valid = True
    else:
      print("You cannot over write a current selection. Go again.")
  play_board[selection] = current_player
  display_play_board()


def check_rows():
  global game_on
  # check if any rows have the same value and they are not empty
  row_1 = play_board[0] == play_board[1] == play_board[2] != "-"
  row_2 = play_board[3] == play_board[4] == play_board[5] != "-"
  row_3 = play_board[6] == play_board[7] == play_board[8] != "-"
  # flag winner if any row has a match
  if row_1 or row_2 or row_3:
    game_on = False
  # return the winner "X" or "O"
  if row_1:
    return play_board[1]
  elif row_2:
    return play_board[4]
  elif row_3:
    return play_board[7]
  return


def check_columns():
  global game_on
  # check if any columns have the same value and they are not empty
  column_1 = play_board[0] == play_board[3] == play_board[6] != "-"
  column_2 = play_board[1] == play_board[4] == play_board[7] != "-"
  column_3 = play_board[2] == play_board[5] == play_board[8] != "-"
  # flag winner if any column has a match
  if column_1 or column_2 or column_3:
    game_on = False
  # return the winner "X" or "0"
  if column_1:
    return play_board[0]
  elif column_2:
    return play_board[1]
  elif column_3:
    return play_board[2]
  return


def check_diagonals():
  global game_on
  # check if any columns have the same value and they are not empty
  diagonal_1 = play_board[2] == play_board[4] == play_board[6] != "-"
  diagonal_2 = play_board[0] == play_board[4] == play_board[8] != "-"
  # flag winner if any column has a match
  if diagonal_1 or diagonal_2:
    game_on = False
  # return the winner "X" or "0"
  if diagonal_1:
    return play_board[2]
  elif diagonal_2:
    return play_board[0]
  return


def check_win():
  global winner
  # check rows
  row_winner = check_rows()
  # check columns
  column_winner = check_columns()
  # check diagonals
  diagonal_winner = check_diagonals()
  # flag winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_tie():
  global game_on
  if "-" not in play_board:
    game_on = False
    return True
  return


def switch_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return


def check_game_over():
  check_win()
  check_tie()


def play_game():
  display_play_board()
  # loop over until the player turns are done
  while game_on:
    # handle a single turn of a player
    handle_turn(current_player)
    # check if the game has ended
    check_game_over()
    # switch to another player
    switch_player()
  # check if game has ended
  if winner == "O" or winner == "X":
    print("Tadaa... player " + winner + " Won!")
  elif winner == None:
    print("Hooraay, some brains here. This is a Tie!") 

play_game()
