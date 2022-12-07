# Creating gaming variables

# This list is to check the status of the game
ps = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game_on = True
turn = 1

# This board is for the output
board = f"""
  -------------
  | {ps[0]} | {ps[1]} | {ps[2]} |
  -------------
  | {ps[3]} | {ps[4]} | {ps[5]} |
  -------------
  | {ps[6]} | {ps[7]} | {ps[8]} |
  -------------  
"""

winning_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                   [1, 4, 7], [2, 5, 8], [3, 6, 9],
                   [1, 5, 9], [3, 5, 7]]
x_list = []
o_list = []


# Checking if anyone manages to win
def check_winner():
    for nr in winning_numbers:
        checking_o = all(n in o_list for n in nr)
        checking_x = all(m in x_list for m in nr)
        if checking_o:
            print("\nO is the winner")
            return True
        elif checking_x:
            print("\nX is the winner")
            return True


# Loop through the game until it's done
while game_on:
    print(board)
    if turn % 2 != 0:
        try:
            choice = int(input("Which position you wanna draw X ?: "))
        except ValueError as error:
            print(f"\nPosition must be a number between 0 and 10: {error}")
            continue
        if choice < 1 or choice > 9:
            print(f"\nPosition must be greater than 0 and less than 10, got: {choice}")
            continue
        elif ps[choice-1] == "X" or ps[choice-1] == "O":
            print("\nSeat is already taken..")
            continue
        elif ps[choice-1] == " " and 0 < choice < 10:
            ps[choice-1] = "X"
            x_list.append(choice)
    else:
        try:
            choice = int(input("Which position you wanna draw O ?: "))
        except ValueError as error:
            print(f"\nPosition must be a number between 0 and 10: {error}")
            continue
        if choice < 1 or choice > 9:
            print(f"\nPosition must be greater than 0 and less than 10, got: {choice}")
            continue
        elif ps[choice - 1] == "X" or ps[choice - 1] == "O":
            print("\nSeat is already taken..")
            continue
        elif ps[choice - 1] == " " and 0 < choice < 10:
            ps[choice - 1] = "O"
            o_list.append(choice)

    turn += 1
    board = f"""
      -------------
      | {ps[0]} | {ps[1]} | {ps[2]} |
      -------------
      | {ps[3]} | {ps[4]} | {ps[5]} |
      -------------
      | {ps[6]} | {ps[7]} | {ps[8]} |
      -------------  
    """
    if check_winner():
        print(board)
        game_on = False
    elif " " not in ps:
        print(board + "\nIt's a draw")
        game_on = False
