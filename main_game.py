import random


def assign_marker():
    """
    Gets and returns the players' assigned markers (X, O).
    """
    user_marker = input("Please choose a marker, Player 1 (X or O): ")
    while user_marker != "X" and user_marker != "O":
        user_marker = input(
            "That is not a X or O. Please try again, Player 1. ")

    if user_marker == "X":
        print("Player 1 is X and Player 2 is O.")
    else:
        print("Player 1 is O and Player 2 is X.")
    return user_marker


def is_player1_first():
    """
    Determines which player goes first.
    """
    first = random.randint(1, 2)

    if first == 1:
        print("Player 1 goes first!")
        return True
    else:
        print("Player 2 goes first!")
        return False


def is_board_full(input_nums):
    """
    Checks if the board is full and returns true if full.
    """
    return " " not in input_nums


def print_board(input_nums):
    """
    Prints the Tic-Tac-Toe board.
    """
    print("""
                  ┃           ┃
            {6}     ┃     {7}     ┃    {8}   
                  ┃           ┃          
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  ┃           ┃
            {3}     ┃     {4}     ┃    {5}    
                  ┃           ┃
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                  ┃           ┃
            {0}     ┃     {1}     ┃    {2}    
                  ┃           ┃
            """.format(input_nums[0], input_nums[1], input_nums[2],
                       input_nums[3], input_nums[4], input_nums[5],
                       input_nums[6], input_nums[7], input_nums[8]))


def get_player_choice(input_nums, marker):
    """
    Takes and returns the player's choice of position.
    """
    prompt = "Where would you like to place {}? Input a number between 1-9 based on the below grid."
    prompt += "\n7|8|9\n4|5|6\n1|2|3\n"
    player_position = input(prompt.format(marker))
    while player_position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        player_position = input(
            "That is not a valid position. Please try again. ")
    player_position = int(player_position)

    if input_nums[player_position-1] == " ":
        return player_position
    else:
        while not (input_nums[player_position-1] == " "):
            player_position = input(
                "This spot is full. Please enter an empty position. ")
            while player_position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                player_position = input(
                    "That is not a valid position. Please try again. ")
            player_position = int(player_position)
            continue

        return player_position


def has_won(input_nums, marker):
    """
    Checks if a player has won. Also checks for a tie.
    """

    condition = (
        input_nums[0] == input_nums[1] == input_nums[2] == marker
        or input_nums[3] == input_nums[4] == input_nums[5] == marker
        or input_nums[6] == input_nums[7] == input_nums[8] == marker
        or input_nums[0] == input_nums[3] == input_nums[6] == marker
        or input_nums[1] == input_nums[4] == input_nums[7] == marker
        or input_nums[2] == input_nums[5] == input_nums[8] == marker
        or input_nums[0] == input_nums[4] == input_nums[8] == marker
        or input_nums[2] == input_nums[4] == input_nums[6] == marker
    )

    if marker == "X" and condition:
        print("Congratulations! You won!")
        return True
    elif marker == "O" and condition:
        print("Congratulations! You won!")
        return True
    elif is_board_full(input_nums):
        print("It's a tie!")
        return True
    else:
        return False


def play_game():
    """
    Sets up the game for playing.
    """
    print("Welcome to Tic-Tac-Toe!")
    player1_marker = assign_marker()
    player2_marker = "O" if player1_marker == "X" else "X"
    if is_player1_first():
        first_player, second_player = player1_marker, player2_marker
    else:
        first_player, second_player = player2_marker, player1_marker

    has_a_player_won = False
    while not has_a_player_won:
        input_nums = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        while not is_board_full(input_nums):
            print_board(input_nums)
            position = get_player_choice(input_nums, first_player)
            # Insert the player's marker at position.
            input_nums[position-1] = first_player
            print_board(input_nums)
            if has_won(input_nums, first_player):
                has_a_player_won = True
                break

            position = get_player_choice(input_nums, second_player)
            input_nums[position-1] = second_player
            if has_won(input_nums, second_player):
                has_a_player_won = True
                break

    print("Thank you for playing!")


play_game()